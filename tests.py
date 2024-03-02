# --a) Cree una función en Python para calcular la sucesión hasta el n-esimo termino (siendo n un argumento de entrada)-- #
import matplotlib.pyplot as plt
import numpy as np

def fibonacci(nesimo_termino: int) -> int:
    """
    Calcula el n-ésimo término de la secuencia de Fibonacci.

    Parámetros:
    nesimo_termino: El índice del término de la secuencia de Fibonacci que se desea calcular.

    Devuelve:
    El n-ésimo término de la secuencia de Fibonacci.
    """
    # Los dos primeros términos de la secuencia de Fibonacci
    termino_0 = 0
    termino_1 = 1

    for _ in range(nesimo_termino):
        # Guarda el valor del término actual en una variable temporal
        temporal = termino_1

        # Calcula el próximo término de la secuencia como la suma de los dos términos anteriores
        termino_1 = termino_0 + termino_1

        # Actualiza el valor del término anterior para la próxima iteración
        termino_0 = temporal

    return termino_0

# --c) Haga un cambio de coordenadas y grafique la espira de Fibonacci-- #
def plot_fibonacci(secuencia: list[int]) -> None:
    """
    Grafica una espiral de Fibonacci.

    :param secuencia: Secuencia de Fibonacci.
    """
    # Calcular la razón áurea entre los dos últimos términos de la secuencia
    proporcion_aurea = secuencia[-1] / secuencia[-2]
    print(f"Proporción Áurea: {proporcion_aurea}")

    # Generar ángulos para la espiral
    angulos = np.linspace(0, 6 * np.pi, num=len(secuencia))  # Reducir el multiplicador a 4 para una mejor visualización

    # Calcular el radio para la espiral logarítmica
    radio = proporcion_aurea ** (angulos / np.pi)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.plot(angulos, radio, label="Espiral de Fibonacci")
    ax.set_rticks([])  # Eliminar las etiquetas radiales
    ax.grid(True)

    ax.set_title("Una espiral de Fibonacci en un eje polar", va='top')
    plt.show()

plot_fibonacci([fibonacci(n) for n in range(1, 100)])  # Reducir el rango a 30 para una mejor visualización