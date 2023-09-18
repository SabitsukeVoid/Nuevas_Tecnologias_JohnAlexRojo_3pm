# age = 9
# height = 160

# if height > 150 or age > 17:
#     print("You can enter")

i = 0
while ( i < 1):
    pay = int(input("Desea hacer su pago? 1.Si 2.No"))
    if(pay == 1):
        pay_amount=float (input ("Ingrese el monto a pagar"))
        pay_service = int(input ("Desea agregar el servicio? (10%) 1.Si 2.No"))
        if (pay_service == 1):
            pay_amount += float((pay_amount * .1))
            print("El valor a pagar con el servicio es:",pay_amount)
        elif (pay_service ==2):
            print("El valor a pagar es:",pay_amount)
        else:
            print("Ingrese un valor valido")
    elif (pay == 2):
        pay=int(input("Desea hacer otro pedido? 1.Si 2.No"))
        if(pay == 2):
            i+=1
        elif(pay !=1):
            print("Ingrese un valor valido")
    else:
        print("Ingrese un valor valido")
