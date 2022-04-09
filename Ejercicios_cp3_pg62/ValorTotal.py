import math

print("Digite el capital")
c=int(input())
print("Digite el interes")
interes=float(input())
print("Digite la cantidad de años")
age=int(input())
total= c*(1+(interes)/100)**age
print("El valor total de los interes segun la cantidad de tiempo es ", total)
