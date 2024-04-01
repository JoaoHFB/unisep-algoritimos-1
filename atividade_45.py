nome_A = input("Digite o nome do aluno: ")
nota_prova = float(input("Digite a nota do aluno na prova: "))
nota_prova_qualitativa = float(input("Digite a nota do aluno na prova qualitativa: "))
nota_final = (nota_prova * 2 + nota_prova_qualitativa) / 3
print("A nota do aluno", nome_A, "nesse semeste na materia de ED vai ser: ", nota_final)