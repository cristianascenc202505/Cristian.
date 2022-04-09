b=[]
i=1

while i in range(1,21):
    num= int(input("Digite un numero: "))
    if num>=1:
        c= num
        b.append(c)
    else:
        print("el numero es negativo, por favor digite un numero positivo")
        continue
    i +=1    
print(b)       