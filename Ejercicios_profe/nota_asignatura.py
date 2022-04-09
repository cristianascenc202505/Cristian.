print("Digite las notas  segun corresponda")
nf=float(input("digite la nota de la evaluacion final: "))
nota_quiz1=float(input("digite la nota del 1er quiz: "))
nota_quiz2=float(input("digite la nota del 2do quiz: "))
nota_quiz3=float(input("digite la nota del 3er quiz: "))
ntq=(nota_quiz1+nota_quiz2+nota_quiz3)/3
trabajo_final=float(input("Digite la nota del trabajo final: "))
total_nota_asignatura=float(nf*0.5)+(ntq*0.20)+(trabajo_final*0.30)
print(total_nota_asignatura)
