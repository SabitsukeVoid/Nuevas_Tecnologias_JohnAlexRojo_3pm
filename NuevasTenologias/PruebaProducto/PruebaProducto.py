usuarios = []

def crearUsuarioSistema():
    err = True
    while err:
        option = input("Quiere iniciar sesion o registrarse? 1.Login 2.Register 3.Salir ")
        if option == "1":
            print("------------Login------------")
            tempCorreoUser = input("Ingrese el correo: ")
            tempClave = input("Ingrese la clave de acceso: ")
            for i in usuarios:
                if i["correo"]== tempCorreoUser:
                    if i["clave"]== tempClave:
                        print("Bienvenido "+i["usuario"])
                        err2=True
                        while err2:
                            option2 = input("Que quieres hacer? 1. Tomar una cicla 2. Ver todos los prestamos 3. Salir ")
                            if option2 == "1":
                                for i in usuarios:
                                    if i["correo"] == tempCorreoUser:
                                        tempOrigen = input("Desde donde se hace el prestamo? ")
                                        tempDestino = input("Hacia donde va el prestamo? ")
                                        tempValor = float(input("Ingrese el valor del prestamo:"))
                                        tempPrestamo = {"origen":tempOrigen,"destino":tempDestino,"valor":tempValor}
                                        i["prestamos"] = []
                                        i["prestamos"].append(tempPrestamo)
                                        print("Prestamo realizado con exito")
                            elif option2 == "2":
                                for i in usuarios:
                                    if i["correo"] == tempCorreoUser:
                                        for j in i["prestamos"]:
                                            print("---------------------------------")
                                            print("Origen del prestamo: "+j["origen"])
                                            print("Destino del prestamo: "+j["destino"])
                                            print("Valor del prestamo: "+str(j["valor"]))
                                            print("---------------------------------")
                            
        elif option == "2":
            correo = input("ingrese un correo: ")
            found = buscarCorreo(correo)
            if found:
                usuario = input("Ingrese el usuario: ")
                numeroTarjeta = input("Ingrese el Numero de tarjeta: ")
                clave = input("Ingrese la clave: ")
                tempUser = {"correo":correo,"usuario":usuario,"numeroTarjeta":numeroTarjeta,"clave":clave}
                usuarios.append(tempUser)
        elif option == "3":
            print("Vuelva pronto")
            err = False
        else:
            print("ingrese una opcion valida")

def buscarCorreo(correo):
    if not usuarios:
        return True
    else:
        for i in usuarios:
            if i["correo"] == correo:
                return False
            else:
                return True