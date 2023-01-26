import matplotlib.pyplot as plt
import math


def generate_polynomial_time_complexity_graph(resolution, darktheme):
    plt.figure(figsize=(10, 6), facecolor="#0d1117" if darktheme else "white")

    ax = plt.axes()
    ax.set_xlim([0, resolution])
    ax.set_ylim([0, resolution])
    plt.setp(ax.spines.values(), color="white" if darktheme else "black")
    ax.set_facecolor("#0d1117" if darktheme else "white")

    plt.xlabel("n", c="white" if darktheme else "black")
    plt.ylabel("time", c="white" if darktheme else "black")

    plt.xticks([])
    plt.yticks([])

    # Quadratic Runtime
    plt.plot([i for i in range(resolution)], [math.pow(i, 2) for i in range(resolution)])
    # Quasilinear Runtime
    plt.plot([i for i in range(resolution)], [i * math.log2(i + 1) for i in range(resolution)])
    # Linear Runtime
    plt.plot([i for i in range(resolution)], [i for i in range(resolution)])
    # Logarithmic Runtime
    plt.plot([i for i in range(resolution)], [math.log2(i + 1) for i in range(resolution)])
    # Constant Runtime
    plt.plot([i for i in range(resolution)], [1 for _ in range(resolution)])

    plt.savefig("polynomial_time_complexity_graph" + ("_dark.svg" if darktheme else "_light.svg"))
    plt.show()


if __name__ == '__main__':
    generate_polynomial_time_complexity_graph(20, True)
    generate_polynomial_time_complexity_graph(20, False)
