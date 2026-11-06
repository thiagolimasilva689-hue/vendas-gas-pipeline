import pandas as pd

def calcular_faturamento(df: pd.DataFrame) -> pd.DataFrame:
    # Cria a coluna nova com a conta
    df["total_venda"] = df["quantidade"] * df["preco_unitario"]
    return df

def gerar_relatorio(df: pd.DataFrame) -> str:
    # Soma a coluna nova e formata como string
    resultado = df["total_venda"].sum()
    return f"O faturamento total foi de R$ {resultado:.2f}"

