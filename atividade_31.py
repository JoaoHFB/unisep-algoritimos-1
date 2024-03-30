salario_base = float(input("digite o salario-base do funcionario: R$"))
gratificação = salario_base * 0.05
salario_gratificação = salario_base + gratificação
imposto = salario_base * 0.07
salario_total = salario_gratificação - imposto
print("O salario do funcionario sera: R$", salario_total)
