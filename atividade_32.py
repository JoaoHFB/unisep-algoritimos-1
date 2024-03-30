valor_produto = float(input("Digite o valor total do produto: R$"))
total_com_desconto = valor_produto * 0.9
valor_parcela = valor_produto / 3
comissao_avista = total_com_desconto * 0.05
comissao_parcelado = valor_produto * 0.05
print("O valor total a pagar com desconto de 10% é: R$", total_com_desconto)
print("O valor de cada parcela será: R$", valor_parcela)
print("A comissão o vendedor, caso ele consiga vender a vista é: R$", comissao_avista)
print("A comissão do vendeor, caso ele venda parcelado é: R$", comissao_parcelado)