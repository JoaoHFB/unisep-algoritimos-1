valor_produto = float(input("Digite o valor total do produto: R$"))
Valor_com_desconto = valor_produto * 0.10
valor_total_com_desconto =  valor_produto - Valor_com_desconto
valor_parcelado = valor_produto / 3
comissão_com_desconto = Valor_com_desconto * 0.05
comissão_total_com_desconto = valor_total_com_desconto + comissão_com_desconto
comissão_parcelado = valor_produto * 0.05
comissão_total_parcelado = valor_produto + comissão_parcelado
print("O valor do produto com 10% de desconto sera: R$", valor_total_com_desconto)
print("O valor de cada parcela será: R$", valor_parcelado)
print("A comissão do vendedor da venda com desconto será: R$", comissão_total_com_desconto)
print("A comissão do vendedor caso a venda seja parcelada sera: R$", comissão_total_parcelado)