# TRABALHO DE ADS - 2º SEMESTRE
# ALUNO: Thierry Pietro Martin dos Reis | RA: 236041
# SISTEMA: RentSmart - R.M Imóveis

import csv

def main():
    print("=== SISTEMA RENTSMART - R.M IMÓVEIS ===")
    print("Aluno: Thierry Pietro Martin dos Reis (RA: 236041)\n")

    # 1. ENTRADAS DO USUÁRIO
    print("Selecione o tipo de imóvel:")
    print("1 - Apartamento")
    print("2 - Casa")
    print("3 - Estúdio")
    tipo = int(input("Digite a opção (1, 2 ou 3): "))

    quartos = 1
    if tipo == 1 or tipo == 2:
        quartos = int(input("Quantidade de quartos (1 ou 2): "))

    vagas = 0
    if tipo == 1 or tipo == 2:
        tem_vaga = input("Deseja vaga de garagem? (s/n): ").strip().lower()
        if tem_vaga == 's':
            vagas = 1
    elif tipo == 3:
        vagas = int(input("Informe o número de vagas de estacionamento: "))

    possui_criancas = True
    if tipo == 1:
        criancas = input("O imóvel terá crianças morando? (s/n): ").strip().lower()
        if criancas == 'n':
            possui_criancas = False

    parcelas_taxa = int(input("Em quantas vezes deseja parcelar a taxa contratual de R$ 2.000,00 (1 a 5)? "))
    if parcelas_taxa < 1:
        parcelas_taxa = 1
    elif parcelas_taxa > 5:
        parcelas_taxa = 5

    # 2. PROCESSAMENTO / CÁLCULOS
    aluguel = 0.0

    # Regras para Apartamento
    if tipo == 1:
        aluguel = 700.0
        if quartos == 2:
            aluguel += 200.0
        if vagas > 0:
            aluguel += 300.0
        if not possui_criancas:
            aluguel = aluguel * 0.95  # 5% de desconto

    # Regras para Casa
    elif tipo == 2:
        aluguel = 900.0
        if quartos == 2:
            aluguel += 250.0
        if vagas > 0:
            aluguel += 300.0

    # Regras para Estúdio
    elif tipo == 3:
        aluguel = 1200.0
        if vagas > 0:
            aluguel += 250.0  # Pacote inicial de 2 vagas
            if vagas > 2:
                vagas_extras = vagas - 2
                aluguel += vagas_extras * 60.0

    taxa_contratual_total = 2000.0
    valor_parcela_taxa = taxa_contratual_total / parcelas_taxa

    # 3. EXIBIÇÃO DO RESUMO NA TELA
    print("\n" + "="*40)
    print("          RESUMO DO ORÇAMENTO")
    print("="*40)
    print(f"Aluguel Mensal do Imóvel: R$ {aluguel:.2f}")
    print(f"Taxa Contratual Total: R$ {taxa_contratual_total:.2f}")
    print(f"Parcelamento da Taxa: {parcelas_taxa}x de R$ {valor_parcela_taxa:.2f}")
    print("-" * 40)
    print(f"Valor Total Mensal (Meses 1 a {parcelas_taxa}): R$ {(aluguel + valor_parcela_taxa):.2f}")
    if parcelas_taxa < 12:
        print(f"Valor Total Mensal (Meses {parcelas_taxa + 1} a 12): R$ {aluguel:.2f}")
    print("="*40)

    # 4. GERAÇÃO DO ARQUIVO CSV (PROJEÇÃO 12 MESES)
    nome_arquivo = "projecao_12_meses.csv"
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo, delimiter=';')
        escritor.writerow(["Mes", "Valor Aluguel", "Parcela Taxa", "Total Mensal"])

        for mes in range(1, 13):
            if mes <= parcelas_taxa:
                taxa_mes = valor_parcela_taxa
            else:
                taxa_mes = 0.0

            total_mes = aluguel + taxa_mes
            escritor.writerow([
                f"Mês {mes}",
                f"R$ {aluguel:.2f}",
                f"R$ {taxa_mes:.2f}",
                f"R$ {total_mes:.2f}"
            ])

    print(f"\n[SUCESSO] Arquivo '{nome_arquivo}' gerado com sucesso na pasta do projeto!")

if __name__ == "__main__":
    main()
