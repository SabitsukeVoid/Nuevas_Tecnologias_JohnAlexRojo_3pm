# Las tuplas se encierran en parentesis 
# Son inmutables
# Si se requiere que tenga algun cambio se debe castear a lista
# Se puede acceder a los elementos
# Las tuplas permiten duplicados
# Permiten distintos tipos de datos

colores = ("amarillo", "azul", "rojo")

print(type(colores)) #Mostrar el tipo de clase
print(len(colores)) #Tamaño de la tupla

print (colores[0]) #Acceder a una posicion especifica en la tupla

coloresList = list(colores) #Convertir una tupla en lista para modificarla


print ("________________________________________________________________")
print (type(coloresList)) #Mostrar el tipo de la tupla casteada a lista

coloresList.append("verde") #Agregar un dato a la lista

print (coloresList[0:]) #Imprimir los datos de la lista

colores = tuple(coloresList) #Recastear la tupla para agregarle la lista modificada y poder modificar la tupla original

print("________________________________________________________________")

for i in range(len(colores)):
    print(colores[i]) #Recorrer por completo la tupla


#Slicing

print(colores[1:4]) #Slice que retorna todo menos amarillo
print(colores[:-1]) #Slice desde atras, imprimiendo todo menos la ultima posicion siendo verde