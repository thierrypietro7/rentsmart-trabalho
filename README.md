# RentSmart - Sistema de Orçamento de Locação

Trabalho prático desenvolvido para a disciplina de Algorithmic Thinking & Introduction to Object-Oriented Programming do 2º semestre do curso de Análise e Desenvolvimento de Sistemas (ADS).

## Aluno
* **Nome:** Thierry Pietro Martin dos Reis
* **RA:** 236041

## Sobre o Projeto
O RentSmart é um sistema desenvolvido em Python com o objetivo de automatizar os cálculos de orçamentos de locação para a imobiliária (estudo de caso R.M Imóveis). A aplicação lida com valores base de diferentes tipos de imóveis (apartamentos, casas e estúdios), adicionais por quartos e vagas de garagem, descontos comerciais e o parcelamento da taxa contratual, exportando os resultados em um relatório em formato CSV.

## Funcionalidades
* Seleção de tipo de imóvel (Apartamento, Casa ou Estúdio).
* Cálculo dinâmico de adicionais por quartos e vagas de garagem.
* Aplicação de regras condicionais (como desconto de 5% para apartamentos sem crianças).
* Parcelamento da taxa contratual fixa de R$ 2.000,00 (em até 5 vezes).
* Exibição de resumo financeiro no terminal.
* Geração automática do arquivo de projeção de 12 meses (`projecao_12_meses.csv`).

## Como Executar o Código
1. Certifique-se de ter o Python instalado no seu computador.
2. Baixe ou clone este repositório contendo o arquivo `main.py`.
3. Abra o terminal ou prompt de comando na pasta do projeto.
4. Execute o comando:
   ```bash
   python main.py
