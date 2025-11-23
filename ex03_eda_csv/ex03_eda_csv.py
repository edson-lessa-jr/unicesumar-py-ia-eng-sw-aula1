from pathlib import Path
import pandas as pd

def run():
    print("\n[EX03] EDA CSV\n")

    raiz = Path(__file__).resolve().parents[1]
    caminho = raiz / "data" / "dados_exemplo.csv"

    df = pd.read_csv(caminho)

    print("\nPrimeiras linhas:")
    print(df.head())

    print("\nInfo:")
    print(df.info())

    print("\nDescribe (somente colunas numéricas):")
    print(df.select_dtypes(include="number").describe())

    print("\nShape:")
    print(df.shape)
