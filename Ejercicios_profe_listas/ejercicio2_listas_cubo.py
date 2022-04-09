n=int(input("Digite un numero de para obtener el rango maximo: "))
a=list(range(1,n))
b=[]
i=1

while i in a:
    r=i**3
    b.append(r)
    i+=1
print(b)