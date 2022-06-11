class Cuenta:    
    def __init__(self,numero,fecha_apertura,saldo):
        self.numero = numero
        self.fecha_apertura = fecha_apertura
        self.saldo = saldo

#metodo Retiro
    def retiro(self):
        print("----------------------------------------------------------------")
        while True:
            self.retiro=int(input(f'Digite el valor a retirar: '))
            if self.saldo>=self.retiro:
                self.saldo-=self.retiro
                return f"""Su retiro ha sido ¡Exitoso!
                        Saldo Actual {self.saldo}"""
            else:
                print('El valor que desea retirar es insuficiente')
                continue
#metodo consignar
    def consignar(self):
        print("----------------------------------------------------------------")
        self.consignar=int(input(f'Digite el valor a consignar: '))
        if self.consignar>0:
            self.saldo+=self.consignar
            return f"""Su consignaciòn ha sido ¡Exitosa! 
                    Saldo actual {self.saldo}"""

#informaciòn de la cuenta
    def informacion(self):
            print("------------------------------------------------------------")
            return(f'Número de cuenta: {self.numero}\nFecha de apertura: {self.fecha_apertura}\nSaldo total: {self.saldo}')

#clase hija llamada cuentaCorriente, con su atrubuto denominado cheque
class cuentaCorriente(Cuenta):
    def __init__(self, numero, fecha_apertura, saldo,cheque):
        super().__init__(numero, fecha_apertura, saldo)
        self.cheque=cheque
    def corriente(self):
        return(f'Número de cheque: {self.cheque}')