import numpy as np

def run():
    print("\n[EX01] NumPy básico – arrays e operações vetorizadas\n")
    lista = [1, 2, 3, 4]
    print("Lista:", lista)
    arr = np.array(lista)
    print("Array:", arr)
    print("arr * 2 =", arr * 2)
    print("Média =", arr.mean())
    print("Soma Python puro:", sum(lista))
    print("Soma NumPy:", arr.sum())
