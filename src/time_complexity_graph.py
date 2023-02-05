import matplotlib.pyplot as plt
import math


def define_base_graph(darktheme: bool, title: str):
    plt.figure(figsize=(10, 6), facecolor="#0d1117" if darktheme else "white")

    ax = plt.axes()
    ax.set_xlim([0, resolution])
    ax.set_ylim([0, resolution])
    plt.setp(ax.spines.values(), color="white" if darktheme else "black")
    ax.set_facecolor("#0d1117" if darktheme else "white")

    plt.title(title, c="white" if darktheme else "black")
    plt.xlabel("n", c="white" if darktheme else "black")
    plt.ylabel("time", c="white" if darktheme else "black")

    plt.xticks([])
    plt.yticks([])


def generate_polynomial_time_complexity_graph(darktheme: bool):
    define_base_graph(darktheme, "Polynomial Time Complexity")

    # Quadratic Runtime
    plt.plot(linear_sequence, quadratic_sequence, label="Quadratic Runtime")
    # Quasilinear Runtime
    plt.plot(linear_sequence, quasilinear_sequence, label="Quasilinear Runtime")
    # Linear Runtime
    plt.plot(linear_sequence, linear_sequence, label="Linear Runtime")
    # Logarithmic Runtime
    plt.plot(linear_sequence, logarithmic_sequence, label="Logarithmic Runtime")
    # Constant Runtime
    plt.plot(linear_sequence, constant_sequence, label="Constant Runtime")

    plt.legend()
    plt.savefig("polynomial_time_complexity_graph" + ("_dark.svg" if darktheme else "_light.svg"))
    plt.show()


def generate_exponential_time_complexity_graph(darktheme: bool):
    define_base_graph(darktheme, "Exponential/Combinatorial Time Complexity")

    # Exponential Runtime
    plt.plot(linear_sequence, exponential_sequence, label="Exponential Runtime")
    # Factorial/Combinatorial Runtime
    plt.plot(linear_sequence, factorial_sequence, label="Factorial/Combinatorial Runtime")

    plt.legend()
    plt.savefig("exponential_time_complexity_graph" + ("_dark.svg" if darktheme else "_light.svg"))
    plt.show()


def generate_full_time_complexity_graph(darktheme: bool):
    define_base_graph(darktheme, "Polynomial and Exponential Time Complexity")

    # Quadratic Runtime
    plt.plot(linear_sequence, quadratic_sequence, label="Quadratic Runtime")
    # Quasilinear Runtime
    plt.plot(linear_sequence, quasilinear_sequence, label="Quasilinear Runtime")
    # Linear Runtime
    plt.plot(linear_sequence, linear_sequence, label="Linear Runtime")
    # Logarithmic Runtime
    plt.plot(linear_sequence, logarithmic_sequence, label="Logarithmic Runtime")
    # Constant Runtime
    plt.plot(linear_sequence, constant_sequence, label="Constant Runtime")

    # Exponential Runtime
    plt.plot(linear_sequence, exponential_sequence, label="Exponential Runtime")
    # Factorial/Combinatorial Runtime
    plt.plot(linear_sequence, factorial_sequence, label="Factorial/Combinatorial Runtime")

    plt.legend()
    plt.savefig("full_time_complexity_graph" + ("_dark.svg" if darktheme else "_light.svg"))
    plt.show()


if __name__ == '__main__':
    resolution = int(input("Input Graph Resolution: "))

    while resolution > 100:
        print("Resolution can not be greater than 100.")
        resolution = int(input("Input Graph Resolution: "))

    constant_sequence = [1 for _ in range(resolution)]
    logarithmic_sequence = [math.log2(i + 1) for i in range(resolution)]
    linear_sequence = [i for i in range(resolution)]
    quasilinear_sequence = [i * math.log2(i + 1) for i in range(resolution)]
    quadratic_sequence = [math.pow(i, 2) for i in range(resolution)]

    exponential_sequence = [math.pow(2, i) for i in range(resolution)]
    factorial_sequence = [math.factorial(i) for i in range(resolution)]

    generate_polynomial_time_complexity_graph(True)
    generate_polynomial_time_complexity_graph(False)
    generate_exponential_time_complexity_graph(True)
    generate_exponential_time_complexity_graph(False)
    generate_full_time_complexity_graph(True)
    generate_full_time_complexity_graph(False)
