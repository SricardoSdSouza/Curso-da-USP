segundos_str = input("Por favor, entre com o número de segundos que deseja converter:")
total_segs = int(segundos_str)
"dando uma quantidade de segundos me retorna h/m/s"
horas = total_segs //3600
"variavel horas vai guardar as horas inteiras"
segs_restantes = total_segs % 3600
"variavel segundos vai guardar os segundos "
minutos = segs_restantes //60
"variável minutos vai guardar os minutos "
segs_restantes_final = segs_restantes % 60

print(horas,"horas, ",minutos, "minutos e", segs_restantes_final, "segundos.")
