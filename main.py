salario_bruto = float(input("Insira seu salário bruto:"))

if salario_bruto < 0:
    raise ValueError("O salário bruto precisa ser um número positivo")

salario_intermediario = 0.00

faixas_contribuicao_inss = [(1320, 0.075),  # Faixa Salarial 1
                            (2571.29, 0.09),  # Faixa Salarial 2
                            (3856.94, 0.12),  # Faixa Salarial 3
                            (float("inf"), 0.14)]  # Faixa Salarial 4

faixas_contribuicao_irrf = [(2112, 0, 0),  # Faixa Salarial 1
                            (2826.65, 0.075, 158.4),  # Faixa Salarial 2
                            (3751.05, 0.15, 370.40),  # Faixa Salarial 3
                            (4664.68, 0.225, 651.73),  # Faixa Salarial 4
                            (float("inf"), 0.275, 884.96)]  # Faixa Salarial 5

def salario_liquido(salario_bruto):
    for limite, aliquota in faixas_contribuicao_inss:
        if salario_bruto <= limite:
            salario_intermediario = salario_bruto * (1 - aliquota)
            break

    for limite, aliquota, desconto in faixas_contribuicao_irrf:
        if salario_intermediario <= limite:
            return (salario_intermediario * (1 - aliquota)) + desconto

print("Seu salário líquido será de R$%.2f" % salario_liquido(salario_bruto))