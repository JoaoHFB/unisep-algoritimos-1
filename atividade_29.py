dias_trabalhados = int(input("Digite a quantidade de dias trabalhados: "))
Qnt_bruta = dias_trabalhados * 30.00
desc_prev = Qnt_bruta * 0.11
qnt_previdencia = Qnt_bruta - desc_prev
desc_imp = qnt_previdencia * 0.08
qnt_liquida =  qnt_previdencia - desc_imp
print("O encanador ganhara bruto: R$", Qnt_bruta)
print("O encanador ganhara liquido: R$", qnt_liquida)