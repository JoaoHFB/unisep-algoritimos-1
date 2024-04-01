print("Adicione abaixo o horario atual")
Horas = int(input("Horas: "))
Minutos = int(input("Minutos: "))
Segundos = int(input("segundos: "))
Duração_ev = int(input("\nDuração do evento (segundos): "))
Segundos_finais = (Segundos + Duração_ev) % 60
Minutos_finais = (Minutos + (Segundos+Duração_ev) // 60) % 24
Horas_finais = (Horas + (Minutos + (Segundos + Duração_ev) // 60) // 60) % 24
print(f"O fim do evento se dará as {Horas_finais}-hr {Minutos_finais}-min e {Segundos_finais}-seg")