hamburguer = 3.00
cheeseburguer = 2.50
fritas = 2.50
refrigerante = 1.00
milshake = 3.00

quantidade_ham = int(input('Digite a quantidade ed hamburgueres consumidos: '))
qunatidade_cheesebur = int(input('Digite a quantidade de cheeseburguer consumidos: '))
quantidade_fritas = int(input('Digite a quantidade de fritas consumidas: '))
quantidade_refrigerantes = int(input('Digite a quantidade de refrigerantes consumidos: '))
quantidade_milkshakes = int(input('Digite a quantidade de milkshakes consumidos: '))

preço_final = (quantidade_ham * hamburguer) + (qunatidade_cheesebur * cheeseburguer) + (quantidade_fritas * fritas) + (quantidade_refrigerantes * refrigerante) + (quantidade_milkshakes * milshake)
print("A conta final será: R$", preço_final)