# CalculaCom

O **CalculaCom** é um programa desenvolvido para validar cálculos de comissões em um sistema de comissão personalizado no SAP B1. Ele auxilia na conferência, ao final do mês, se o fator de cálculo de comissão de integração entre o CRM e o SAP está correto.

## Funcionalidades

- **Cálculo de Comissão**: Realiza o cálculo do fator de comissão com base nos valores inseridos (Preço Geral, Preço Unitário, ICMS e Encargos).
- **Validação de Fator**: Compara o fator calculado com uma lista de referência armazenada em um arquivo Excel (`dados.xlsx`).
- **Interface Simples**: Interface gráfica intuitiva e fácil de usar, desenvolvida com a biblioteca `flet`.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal.
- **Flet**: Biblioteca para criação da interface gráfica.
- **Pandas**: Biblioteca para manipulação de dados, utilizada para ler e processar o arquivo Excel (`dados.xlsx`).

## Como Usar

### Pré-requisitos

- Python 3.x instalado.
- Bibliotecas necessárias: `flet` e `pandas`.

### Instalação

1. Clone o repositório ou faça o download dos arquivos.
2. Instale as dependências necessárias:

   ```bash
   pip install flet pandas

Desenvolvido por
Fábio Furtili
