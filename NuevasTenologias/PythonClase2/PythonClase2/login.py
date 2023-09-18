import random

err = 0
mail =""
telefono =""
password = ""
loginmailphone = ""
loginpassword = ""
logincaptcha = ""
captcha = [r"""
 _   _      _ _       
| | | |    | | |      
| |_| | ___| | | ___  
|  _  |/ _ \ | |/ _ \ 
| | | |  __/ | | (_) |
\_| |_/\___|_|_|\___/ """,r"""
______            
| ___ \           
| |_/ /_   _  ___ 
| ___ \ | | |/ _ \
| |_/ / |_| |  __/
\____/ \__, |\___|
        __/ |     
       |___/      
""",r"""
 _____ _     
|  _  | |    
| | | | |__  
| | | | '_ \ 
\ \_/ / | | |
 \___/|_| |_|
             
             
"""]


while(err==0):
    select1 = int(input("Quieres ingresar o registrarte? 1.Registrarse 2.Login "))
    if (select1 == 1):
        print ("Ingresa tu correo electronico:")
        mail=input()
        print ("Ingresa la contraseña: ")
        password=input()
        print ("Ingrese el telefono: ")
        telefono=input()
    elif (select1 == 2):
        print ("Ingrese el mail o el telefono:")
        loginmailphone=input()
        print ("Ingrese la contraseña: ")
        loginpassword=input()
        if((loginmailphone == mail or loginmailphone == telefono) and loginpassword == password):
            print("Ingrese el siguiente captcha")
            print (captcha[random.randint(0,2)])
            logincaptcha = input()
            if (logincaptcha == "Hello" or logincaptcha == "Bye" or logincaptcha == "Oh"):
                print ("Iniciaste sesion correctamente")
                print ("Bienvenido",mail)

                err+=1
            else:
                print("Captcha invalido")
        else:
            print("Datos invalidos o no encontrados")

    else:
        print('Opcion invalida')