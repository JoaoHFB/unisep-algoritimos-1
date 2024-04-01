n_vendedor = input("Digite o nome do vendedor: ")
carros_vendidos = int(input("Digite a quantidade de carros vendidos: "))
total_de_vendas = float(input("Digite o valor total de carros vendidos em reais: R$"))

salario = 500.00
comissão = 50.00
comissão_por_venda = total_de_vendas * 0.05
salario_final = salario + (carros_vendidos * comissão) + comissão_por_venda
print("O salario o vendedor", n_vendedor ,"este mês é de: R$", salario_final)