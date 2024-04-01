Custo_fabrica = float(input("Dugite o valor de costo do veiculo, em rais: R$"))
distribuidora = 0.12
IMPOSTO = 0.45
valor_final = Custo_fabrica + Custo_fabrica * (distribuidora + IMPOSTO)
print("O o valor final do veiculo sera de: R$", valor_final)