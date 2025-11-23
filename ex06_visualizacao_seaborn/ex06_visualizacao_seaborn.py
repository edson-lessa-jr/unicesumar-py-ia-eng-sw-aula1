from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def run():
    print("\n[EX06] Seaborn – countplot\n")
    raiz = Path(__file__).resolve().parents[1]
    caminho = raiz / "data" / "dados_exemplo.csv"
    df = pd.read_csv(caminho)
    sns.countplot(x="cidade", data=df)
    plt.title("Frequência por Cidade")
    plt.xticks(rotation=30)
    plt.show()
