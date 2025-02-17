# Calculadora de MS (Média de Nota Semestral)

Este projeto é uma aplicação simples de **calculadora de MS** (Média de Nota Semestral), onde o usuário insere as notas e o sistema calcula a média ponderada. A aplicação salva os dados digitados em um arquivo JSON e oferece a opção de resetar as informações salvas.

## Funcionalidades

- **Cálculo da MS**: O programa calcula a média ponderada com base nas notas dos três componentes:
  - NP1 (Nota da Prova 1)
  - NP2 (Nota da Prova 2)
  - PIM (Nota do PIM - Projeto Integrador)
  
  A fórmula usada é:  
  `MS = (NP1 * 4 + PIM * 2 + NP2 * 4) / 10`
  
  Se a média for inferior a 7.0, a aplicação indica que o aluno precisa se aplicar a MF (Recuperação).

- **Salvar Dados**: Sempre que o usuário digitar algo nos campos de entrada, os dados são automaticamente salvos em um arquivo JSON.

- **Carregar Dados**: Quando o aplicativo é aberto, os valores salvos anteriormente são carregados automaticamente, poupando o usuário de ter que digitar novamente.

- **Resetar Dados**: Existe a opção de **resetar** os dados e apagar o arquivo JSON, se necessário, através de um botão dedicado.

## Funcionalidades do Código

- Validação de entradas: O código garante que o usuário insira apenas valores numéricos válidos (ou vírgulas para decimais).
- Interface gráfica simples e limpa feita com a biblioteca **Tkinter**.
- Armazenamento persistente dos dados em **JSON**.
- Função de **resetar** os dados.

## Requisitos

Certifique-se de ter o Python 3.x instalado no seu computador. O projeto utiliza a biblioteca **Tkinter**, que já vem instalada com o Python.

## Como Usar

1. Clone o repositório ou baixe os arquivos do projeto.
2. Abra o terminal ou prompt de comando e navegue até a pasta do projeto.
3. Execute o arquivo Python:

```bash
python calculadora_ms.py
