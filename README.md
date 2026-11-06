# ⛽ Pipeline de Processamento de Vendas de Gás

Este é um projeto prático de engenharia de dados que simula um pipeline ETL (Extract, Transform, Load). O objetivo principal é ler dados brutos de vendas em formato CSV, realizar o cálculo de faturamento e gerar um relatório final consolidado.

Este projeto marca a transição de scripts simples para uma **arquitetura modular**, focada em boas práticas de programação.

## 🎯 Funcionalidades e Aprendizados
- **Arquitetura Modular:** Separação clara entre a lógica de extração de dados (`leitura.py`) e a lógica de negócios/transformação (`processamento.py`).
- **Tratamento de Erros:** Uso de blocos `try/except` para garantir que o programa não quebre caso o arquivo CSV não seja encontrado, retornando um DataFrame vazio de forma segura.
- **Manipulação de Dados (Pandas):** Criação de novas colunas baseadas em cálculos matemáticos (quantidade * preço unitário) e agregação de dados (`.sum()`).
- **Exportação de Resultados:** Geração automática de um arquivo de texto (`resultado.txt`) com o resumo do faturamento.

## 🛠️ Tecnologias Utilizadas
- **Python 3** (Lógica e orquestração)
- **Pandas** (Manipulação e análise de dados)
- **Pathlib / OS** (Manipulação de caminhos de arquivos)

## 📁 Estrutura do Projeto
A organização do código foi pensada para ser escalável e de fácil manutenção:

```text
projeto_gas/
├── modulos/
│   ├── __init__.py
│   ├── leitura.py          # Responsável por ler o CSV e tratar erros de arquivo
│   └── processamento.py    # Contém as regras de negócio (cálculos e relatórios)
├── dados_vendas.csv        # Base de dados de exemplo
├── main.py                 # Ponto de entrada que orquestra o pipeline
└── README.md
