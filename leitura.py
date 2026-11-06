"""
Passo 2: O módulo de leitura (modulos/leitura.py)
Crie uma função chamada ler_csv(caminho).
Ela deve usar o Pandas (pd.read_csv) para ler o arquivo.
Use try/except FileNotFoundError para o caso do arquivo não existir. Se não existir, imprima "Erro: Arquivo não encontrado" e retorne um DataFrame vazio (pd.DataFrame()).
Se der certo, retorne o DataFrame.
"""
import pandas as pd
def ler_csv(caminho:str)->pd.DataFrame:
    try:
        df = pd.read_csv(caminho)
        return df
    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho}' não encontrado")
        return pd.DataFrame()
        


        