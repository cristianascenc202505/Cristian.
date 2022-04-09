b=[]
i=1

while i in range(1,6):
    num= int(input("Digite el numero: "))
    if num >=1:        
        n= num
        b.append(n)
    else:
        n=0
        b.append(n)
    i+=1
print(b)    