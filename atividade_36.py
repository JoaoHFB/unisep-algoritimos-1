numero = int(input("Digite um numero inteiro entre (1000 e 9999): "))

milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = numero % 10

print(milhar)
print(centena)
print(dezena)
print(unidade)