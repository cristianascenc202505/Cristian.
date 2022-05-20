def listaCreada():    
    nombrelista=str(input("Digite el nombre de la lista a crear: "))
    nombrelista=[]
    rango=int(input("Digite la longitud de la lista: "))
    
    for i in range(rango-1):
        
        elemento=input("digite el elemento para la lista a crear: ")
        nombrelista.append(elemento)
    print(nombrelista)
    
listaCreada()
    