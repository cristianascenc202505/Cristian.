print("Bienvenido.\nCon las siguientes preguntas evaluaremos si eres apto para el proceso de donacion danguinea.\nAgradecemos tu aporte ")
age=int(input("Que edad tiene: "))

if age > 18:
    ps=float(input("Cual es su peso: "))
    fc=int(input("Segun el dispositivo colocado en su mano, cuantos latidos cardiacos tiene: "))
    rp=float(input("Segun prueba rapida realizada por el personal de salud, ¿Cual es la cantidad de plaquetas que tiene?"))

    if ps < 55 :
        print("Lo sentimos no cuenta con el peso estipulado para continuar el proceso de donacion")
    elif  fc<60 :
        print("Lo sentimos no cuenta con una frecuencia cardiaca adecuada segun el protocolo estipulado para continuar el proceso de donacion")
    elif rp<150.000:
        print("Lo sentimos no cuenta con el recuento plaquetario estipulado para continuar el proceso de donacion")
    else:
        print("Nuevamente agradecemos tu voluntad de donar sangre.\nPuedes continuar con el proceso de donacion sanguinea")
else:
    print("Lo sentimos no cuentas con la edad autirizada para continuar el proceso.")