import pandas as pd

def run():
    print("\n[EX02] DataFrame simples\n")
    df = pd.DataFrame({
        "nome": ["Ana", "João", "Carlos"],
        "idade": [23, 31, 45],
        "cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
    })
    print(df)
    print("\nIdade:")
    print(df["idade"])
    print("\nDescribe:")
    print(df["idade"].describe())
