import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def graficar(
    x: np.array,
    y: np.array,
    titulo: str = None,
    xlabel: str = "Tamaño de la entrada",
    ylabel: str = "Tiempo de ejecución",
) -> None:
    sns.set_style("dark")
    sns.lineplot(x=x, y=y)
    plt.title(titulo)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
