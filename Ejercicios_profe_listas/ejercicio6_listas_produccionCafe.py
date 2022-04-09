Meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
v_i=[]

for i in Meses:
    Valores=int(str(input("Ingrese los valores de la produccion de cafe de {} ".format(i))))
    v_i.append(Valores)
    
promedio=sum(v_i)/len(Meses)
mayor=max(v_i)
minimo=min(v_i)

#Mostrar promedio
print("el promedio de los valores es {} ".format(promedio))

#Mes y valor con mayor produccion
index_max=max(range(len(v_i)), key=v_i.__getitem__)
print("el valor mayor es {}, corresponde al mes de {}".format(mayor,Meses[index_max]))

#Mes y valor con menor produccion
index_min=min(range(len(v_i)), key=v_i.__getitem__)
print("el valor menor es {}, corresponde al mes de {}".format(minimo,Meses[index_min]))
#Meses mayores al promedio
print("valores mayores al promedio")
for i in range(len(v_i)):
    if v_i[i]> promedio:
        print(" {}, corresponde al mes de {}".format(v_i[i], Meses[i]))
#Meses menores al promedio
print("valores menores al promedio1")
for i in range(len(v_i)):
    if v_i[i]< promedio:
        print(" {}, corresponde al mes de {}".format(v_i[i], Meses[i]))
        


