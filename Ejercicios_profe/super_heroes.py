human= input("El personaje marvel es humano:  ")
can_fly= input("El personaje marvel puede volar: ")
has_mask= input("El personaje marvel tiene mascara: ")

if human  and can_fly and has_mask:
    print("Es airoman")
elif human and can_fly and  not has_mask:
    print("Es capitana marvel")
elif not human and can_fly and has_mask:
    print("Es Ronan Accuser")
elif not human  and can_fly and not has_mask:
    print("Es Vision")
elif not human  and can_fly=="si" and  has_mask=="no":
    print("Es Vision")
elif human =="si" and can_fly=="no" and has_mask=="si":
    print("Es Spiderman")
elif human =="si" and can_fly=="no" and has_mask=="no":
    print("Es hulk")
elif human =="no" and can_fly=="no" and has_mask=="si":
    print("Es Black bolt")
elif human =="no" and can_fly=="no" and has_mask=="no":
    print("Es Black Thanos")
else:   
    print("no hay un personaje de marvel con dichas caracteristicas")