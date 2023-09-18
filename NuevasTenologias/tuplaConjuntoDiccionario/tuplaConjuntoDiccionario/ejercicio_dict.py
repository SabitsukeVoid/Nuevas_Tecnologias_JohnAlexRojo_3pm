## Ejercicio usando dicccionario y funciones en el que creemos un producto
## Con las siguientes claves:
## id, nombre, costo, cantidad, margendeganancia
## Se deben almacenar los productos con dos campos adicionales calculados
## precioventa = costo/(1-margenganancia) y valor de inventarios = cantidad * costo

mercado = {}
salir = True


while salir:
    print("__________________________________________________________________________")
    print("Agregar productos de Mercado")
    print("__________________________________________________________________________")
    respuesta = int(input("Quiere Agregar un nuevo producto? 1.Si 2.No"))
    if(respuesta == 1):
        mercado[salir] 
            
    elif(respuesta == 2):
        salir = False
        else:



def calculate_price(costo,margenganancia):
    precioventa = costo/(1-margenganancia)
    return precioventa

def calculate_inventory_value (cantidad,costo):
    valor_inv = cantidad * costo
    return valor_inv
