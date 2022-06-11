import cuenta
#objetos
print('\n|Cuenta|')
cuenta1=cuenta.Cuenta(123456,'25/Mayo/2020',1000000)
print(cuenta1.retiro())
print(cuenta1.consignar())
print(cuenta1.informacion())
print("--------------------------------------------------------------------------")
print("|Cuenta corriente|")
corriente1=cuenta.cuentaCorriente(23455678,'01/Septiembre/1997',800000,8901)
print(corriente1.retiro())
print(corriente1.consignar())
print(corriente1.informacion())
print(corriente1.corriente())