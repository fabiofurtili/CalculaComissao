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

3. Certifique-se de que o arquivo `dados.xlsx` esteja no mesmo diretório do script. Este arquivo deve conter uma planilha chamada `dados` com as colunas `Fator` e `Lista`.

### Executando o Programa

1. Navegue até o diretório do projeto.
2. Execute o script Python:

   ```bash
   python calculacom.py
   ```

3. Insira os valores solicitados na interface:
   - Preço Geral
   - Preço Unitário
   - ICMS (se houver)
   - Encargos (se houver)

4. Clique em **Calcular** para obter o fator de comissão e a lista de referência correspondente.

### Exemplo de Uso

1. Preencha os campos com os valores desejados.
2. O programa exibirá:
   - Fator de comissão com 3 casas decimais.
   - Fator de comissão com 8 casas decimais.
   - Lista de referência correspondente ao fator calculado.

## Estrutura do Projeto

- `calculacom.py`: Script principal do programa.
- `dados.xlsx`: Arquivo Excel contendo a lista de fatores e referências.

## Contribuição

Contribuições são bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`).
3. Commit suas mudanças (`git commit -m 'Adicionando NovaFeature'`).
4. Push para a branch (`git push origin feature/NovaFeature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## Desenvolvido por

**Fábio Furtili**  
[GitHub](https://github.com/fabiofurtili)
