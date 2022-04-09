n1=int(input("Ingrese 1er numero: "))
n2=int(input("Ingrese 2do numero: "))
n3=int(input("Ingrese 3er numero: "))
if n1<n2 and n1<n3:
    print(f"el valor minimos es {n1}")
elif n2<n1 and n2<n3:
    print(f"el valor minimos es {n2}")
elif n3<n1 and n3<n2:
    print(f"el valor minimos es {n3}")    
elif n1==n3 and n3<n2:
    print(f"Existen 2 valores minimos es {n3},{n1}")
elif n2==n3 and n3<n1:
    print(f"Existen 2 valores minimos es {n3},{n2}")
elif n1==n2 and n2<n3:
    print(f"Existen 2 valores minimos es {n2},{n1}")    
elif n3==n1 and n3==n2 and n1==n2:
    print("los numeros son iguales")
