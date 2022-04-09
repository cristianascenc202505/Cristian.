palabra='ordenador'

palabra_l=len(palabra)
a=palabra.count('a')
e=palabra.count('e')
i=palabra.count('i')
o=palabra.count('o')
u=palabra.count('u')

metrica=palabra_l*(a+e+i+o+u)
print(f'total de vocales: {metrica}')