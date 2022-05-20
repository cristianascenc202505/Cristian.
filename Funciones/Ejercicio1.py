def frutas():
     fruits.sort()
     fruta= ','.join(fruits)        
     print(fruta)
     
def buscador():
     i=0
     while i<=len(fruits):  
          buscar=str(input("Buscar: "))
          for j  in range(len(fruits)):               
               if buscar != '':               
                    if buscar != fruits[j]:
                         print("Elemento no encontrado")
                    else:
                         textBusqueda=fruits.index(buscar)
                         print(textBusqueda)
                         continue
               else:
                    print("No a digitado algun elemento para la busquedad")
          i+=1     
     print(f"la longitud de la lista es de {len(fruits)}")
     
fruits=[]
for i in range(0,3):
     fruit=str(input("ingrese una frutas: "))
     fruits.append(fruit)  

print(fruits)
frutas()
buscador()

