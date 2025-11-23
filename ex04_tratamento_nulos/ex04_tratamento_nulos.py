from pathlib import Path
import pandas as pd

def run():
    print("\n[EX04] Tratamento de nulos\n")
    raiz = Path(__file__).resolve().parents[1]
    caminho = raiz / "data" / "dados_exemplo.csv"
    df = pd.read_csv(caminho)
    print("\nNulos:")
    print(df.isna().sum())
    print("\nDropna:")
    print(df.dropna())
    media = df["idade"].mean()
    df["idade"] = df["idade"].fillna(media)
    print("\nImputado:")
    print(df)
