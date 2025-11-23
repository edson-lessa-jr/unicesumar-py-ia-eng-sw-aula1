from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

def run():
    print("\n[EX05] Matplotlib – histograma\n")
    raiz = Path(__file__).resolve().parents[1]
    caminho = raiz / "data" / "dados_exemplo.csv"
    df = pd.read_csv(caminho)
    plt.hist(df["idade"].dropna())
    plt.title("Distribuição de Idades")
    plt.xlabel("Idade")
    plt.ylabel("Frequência")
    plt.show()
