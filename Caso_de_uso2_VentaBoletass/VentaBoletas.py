com= str(input("Bienvenidos: Este es un programa para vena de boletas.\nDesea realizar la compra: "))
numeroDoc=[]
nBDo=[]
boleta=10
acu_b=0

if com=="si" or com=="Si" or com=="SI" or com=="sI":        
    for i in range(0,2):
        TipoDoc= str(input("Cual es su tipo de documento: "))   
        nDoc=int(input("Cual es su numero de cedula: "))
        #condiciono el Tipo de documento y # de documento    
        if TipoDoc== "cc" and nDoc>0:            
            numeroDoc.append(nDoc)            
            #validacion # de documento
            if numeroDoc.count(nDoc) >1:                
                print("Usuario ya adquirio boletas")
                break   
            nBol=int(input("Cuantas boletas va a comprar?"))  
            #validacion  y guardado de cantidad boleta
            if nBol >0 and nBol<=4:        
                acu_b= acu_b+nBol          
                if acu_b<= boleta :
                    tb=boleta-acu_b
                    nBDo.append(nBol)
                    print(f"Venta exitosa\n")
                elif acu_b>boleta :                               
                    acu_b=acu_b-nBol
                    nm=boleta-acu_b
                    print(f"lo sentimos en el  NO momento contamos con la cantidad de bolestas requeridas, contamos con {nm} boletas")                        
                if tb == 0 : 
                    print(f"\nBoleteria agotada")
                    break
            else:
                print(f"Lo sentimos, la cantidad de boletas solictadas por ususario son {nBol}, recuerde que la cantidad maxima autorizada para su compra es de 4 boletas")
            
        else:              
            print("Debe ingresar un tipo de documento valido")   