numero_seg = int(input("Digite um nuemro inteiro em segundos: "))

horas = numero_seg // 3600
segundos_restantes =  numero_seg % 3600
minuto = segundos_restantes // 60
segundos_restantes_f = segundos_restantes % 60

print("horas", horas)
print("minutos", minuto)
print("segundos", segundos_restantes_f)