tabla_control=('TRWAGMYFPDXBNUZSQVHLCKE')

digito='12345678'
digito_control=tabla_control[int(digito) % 23]
print(f"su digito de control es: 12345678{digito_control}")