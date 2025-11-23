from ex01_numpy_basico.ex01_numpy_basico import run as ex01_run
from ex02_pandas_dataframe.ex02_pandas_dataframe import run as ex02_run
from ex03_eda_csv.ex03_eda_csv import run as ex03_run
from ex04_tratamento_nulos.ex04_tratamento_nulos import run as ex04_run
from ex05_visualizacao_matplotlib.ex05_visualizacao_matplotlib import run as ex05_run
from ex06_visualizacao_seaborn.ex06_visualizacao_seaborn import run as ex06_run

def menu():
    print("\n=== MENU ===")
    print("1 - NumPy básico")
    print("2 - DataFrame simples")
    print("3 - EDA inicial CSV")
    print("4 - Tratamento de nulos")
    print("5 - Visualização Matplotlib")
    print("6 - Visualização Seaborn")
    print("0 - Sair")

def main():
    while True:
        menu()
        op = input("Escolha: ")
        if op == "0":
            break
        elif op == "1":
            ex01_run()
        elif op == "2":
            ex02_run()
        elif op == "3":
            ex03_run()
        elif op == "4":
            ex04_run()
        elif op == "5":
            ex05_run()
        elif op == "6":
            ex06_run()
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
