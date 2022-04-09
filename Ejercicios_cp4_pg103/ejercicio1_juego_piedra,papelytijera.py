menu=print("""Vamos a jugar piedra, papel y tijera
        elija una Opcion:
        1-- piedra
        2-- papel
        3-- tijera""")
p1=int(input("Persona  uno: "))
p2=int(input("Persona  dos: "))

if p1==p2:
    print(" Hay un empate por que eligieron el mismo ojeto")
elif p1==1 and p2 ==3:
    print("Gana persona 1 porque la piedra daña la tijera")
elif  p1==3 and p2 ==1:
    print("Gana persona 2 porque la piedra daña la tijera")  
elif p1==2 and p2 ==1: 
    print("Gana persona 1 porque el papel envuelve la piedra")
elif p1==1 and p2 ==2:
    print("Gana persona 2 porque el papel envuelve la piedra")    
elif p1==3 and p2 ==2:
    print("Gana persona 1 porque la tijera corta el papel")
elif p1==2 and p2 ==3:
    print("Gana persona 2 porque la tijera corta el papel")