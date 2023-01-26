import matplotlib.pyplot as plt
import math


def generate_polynomial_time_complexity_graph(resolution, darktheme):
    plt.figure(figsize=(10, 6), facecolor="#0d1117" if darktheme else "white")

    ax = plt.axes()
    ax.set_xlim([0, resolution])
    ax.set_ylim([0, resolution])
    plt.setp(ax.spines.values(), color="white" if darktheme else "black")
    ax.set_facecolor("#0d1117" if darktheme else "white")

    plt.title("Polynomial Time Complexity", c="white" if darktheme else "black")
    plt.xlabel("n", c="white" if darktheme else "black")
    plt.ylabel("time", c="white" if darktheme else "black")

    plt.xticks([])
    plt.yticks([])

    linear_sequence = [i for i in range(resolution)]

    # Quadratic Runtime
    plt.plot(linear_sequence, [math.pow(i, 2) for i in range(resolution)], label="Quadratic Runtime")
    # Quasilinear Runtime
    plt.plot(linear_sequence, [i * math.log2(i + 1) for i in range(resolution)], label="Quasilinear Runtime")
    # Linear Runtime
    plt.plot(linear_sequence, linear_sequence, label="Linear Runtime")
    # Logarithmic Runtime
    plt.plot(linear_sequence, [math.log2(i + 1) for i in range(resolution)], label="Logarithmic Runtime")
    # Constant Runtime
    plt.plot(linear_sequence, [1 for _ in range(resolution)], label="Constant Runtime")

    plt.savefig("polynomial_time_complexity_graph" + ("_dark.svg" if darktheme else "_light.svg"))
    plt.legend()
    plt.show()


if __name__ == '__main__':
    generate_polynomial_time_complexity_graph(20, True)
    generate_polynomial_time_complexity_graph(20, False)
