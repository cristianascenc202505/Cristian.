ingreso= str(input('Desea ingresar?: '))
ch=0
cm=0
acu_h=0
acu_m=0
e_min=999

if ingreso=='si'or ingreso=='Si' or ingreso=='SI':
    
    while ingreso=='si' or ingreso=='Si' or ingreso=='SI':
        print('\nNuevo usuario')
        edad= int(input('Que edad tiene: '))
        t_h_m=ch+cm        

        if edad>= 18:
            nombre=str(input('Nombre completo: '))
            genero=str(input('genero: '))
            
            if edad<e_min and edad !=0:
                e_min=edad
                
            if genero=='hombre':            
                ch +=1
                acu_h=acu_h+edad
                pro_h=int(acu_h/ch)
            elif  genero=='mujer':
                cm +=1
                acu_m=acu_m+edad
                pro_m=int(acu_m/cm)

        elif edad>0 and edad<18:
            print('No puedes ingresar, no tiene la edad requirida para el ingreso')
        else: 
            break        
    print(f"""\nTotal asistentes a la fiesta: {t_h_m}\nTotal asistentes hombres: {ch}.\nTotal mujeres: {cm}
            \nPromedio edad hombre: {pro_h} \nPromedio edad mujeres: {pro_m}
            \nEdad minima de personas que asistieron: {e_min}""")
else:
    print('salir de pagina')   