def listar():
    estudiantes.sort()
    est=','.join(estudiantes)
    print (est)
    
def promedio():
    prome=(nota1+nota2)/2
    return prome

def modificar():
    student={}
    
    for i in range(len(codigoEstudiante)):
        student[codigoEstudiante[i]]=estudiantes[i]
    print(student)
        
    # while True:
    #     modifica=input("Desea modificar alguna nota de un estudiante si/no")
    #     if modifica=="si":
    #         modificaNota1=input("Modificar nota 1 si/no")
    #         if  modificaNota1=="si":            
    #             cambionota1=float(input("Digite la nueva nota 1: "))
    #             if cambionota1>=0.0 and cambionota1<=5.0:                    
    #                 nota1[0]=cambionota1
    #         elif modificaNota1=="no":
    #                 modificaNota2=input("Modificar nota 1 si/no")
                
    #     elif modifica=="no":
    #         pass

estudiantes=[]
codigoEstudiante=[]
nota1=[]
nota2=[]
for i in range(2):
    nombre=input("Digite el nombre completo del estudiante: ")
    estudiantes.append(nombre)    
    cod_Estudiante=int(input("Digite el codigo del estudiante: "))
    codigoEstudiante.append(cod_Estudiante)
    nota1_Estudiante=float(input("Digite la nota 1: "))
    nota1.append(nota1_Estudiante)
    nota2_Estudiante=float(input("Digite la nota 2: "))
    nota2.append(nota2_Estudiante)
    
    

listar()
modificar()
print(estudiantes,codigoEstudiante)



