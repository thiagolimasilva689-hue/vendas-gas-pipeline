from modulos.leitura import ler_csv
from modulos.processamento import  calcular_faturamento, gerar_relatorio

if __name__ == "__main__":
    caminho = r'C:\Users\Thiago\OneDrive\Desktop\teiu\projeto_gas\dados_vendas.csv'
    # 1. Lê o arquivo
    df = ler_csv(caminho)

    # 2. Verifica se não está vazio (se o arquivo não existiu, o ler_csv retorna vazio)
    if not df.empty:
        # 3. Processa
         df = calcular_faturamento(df)
    # 4. Gera o relatório e mostra na tela
    relatorio = gerar_relatorio(df)
    print(relatorio)

    #Salvar no TXT:
    with open("resultado.txt", "w", encoding="utf-8") as arquivo:
         arquivo.write(relatorio)
         print("Relatório salvo em resultado.txt!")
else:
     print("Não foi possível processar porque o arquivo está vazio ou não existe.")

         



