ganados=int(input("Ingrese cuantos partidos ha ganado: "))
resulganados= ganados*3
empatados=int(input("Ingrese cuantos partidos ha empatado: "))
resulempatados= ganados*1
perdidos=int(input("Ingrese cuantos partidos ha perdido: "))
resulperdidos= ganados*0
resul_total= resulganados+resulempatados+resulperdidos
print(f'''los resultados del equipo the champions son:
    Cantidad de puntos por partidos Ganados: {resulganados}
    Cantidad de puntos por partidos Empatados: {resulempatados}
    Cantidad de puntos por partidos Perdido: {resulperdidos} 
    Cantidad de puntos totales: {resul_total}''')

