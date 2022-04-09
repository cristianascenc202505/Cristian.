tecla1=input("digite la primera tecla: ")
tecla2=input("digite la segunda tecla: ")
tecla3=input("digite la tercera tecla: ")

if tecla1=='Ctrl' and tecla2=='Alt' and tecla3=='Del':
    print("cerrar cesion")
elif tecla1=='Super':
    print("Abre la búsqueda de actividades")
elif tecla1=='Ctrl' and tecla2=='Alt' and tecla3=='T':
    print("Atajo de terminal de Ubuntu")
elif tecla1=='Ctrl' and tecla2=='Alt' and tecla3=='L' or tecla1=='Super' and tecla2=='L':
    print("Bloquea la pantalla")
elif tecla1=='Ctrl' and tecla2=='Alt' and tecla3=='D' or tecla1=='Super' and tecla2=='D':
    print("Mostrar escritorio")
elif tecla1=='Super' and tecla2=='A':
    print("Muestra el menú de la aplicación")
elif tecla1=='Super' and tecla2=='Tab' or tecla1=='Alt' and tecla2=='Tab':
    print("Cambiar entre aplicaciones en ejecución")
elif tecla1=='Super' and tecla2=='<' or tecla1=='Super' and tecla2=='>' :
    print("Ajustar ventanas")
elif tecla1=='Super' and tecla2=='M':
    print("Alternar bandeja de notificación")
elif tecla1=='Super' and tecla2=='Space':
    print("Cambiar teclado de entrada (para configuración multilingüe)")
elif tecla1=='Alt' and tecla2=='F2':
    print("Ejecutar consola")
elif tecla1=='Ctrl' and tecla2=='Q' or tecla1=='Ctrl' and tecla2=='W' or tecla1=='Alt' and tecla2=='F4' :
    print("Cerrar una ventana de aplicación")
elif tecla1=='Ctrl' and tecla2=='Alt' and tecla3=='Flecha':
    print("Moverse entre espacios de trabajo") 
else:
    print("Error")