# Los diccionarios estan compuestos de clave:valor
# Son mutables
# No admiten claves repetidas 
# Desde python 3.7 los diccionarios son ordenados

user1 = {"name": "John", "email": "john@example.com", "password": "example123"}

#mostrar el tamaño del diccionario

print(len(user1))

#mostrar el tipo de dato

print(type(user1))


#Agregar clave

user1["lastName"] = "Alex"

#Imprimir solo claves

print(user1.keys())

#Imprimir solo valores

print(user1.values())

#Imprimir clave:valor

print(user1.items())


#Obtener valor con la clave

print(user1.get('name'))


#Borrar la clave proporcionada clave:valor

user1.pop("email")

print(user1.items())


#Podemos usar for para imprimir el diccionario ya sea solo claves, solo valores o ambos


for x,y in user1.items():
    print("Soy key "+x)
    print("Soy value "+y)
    print(x+" : "+y)


#Hacer diccionario de diccionario
Colores = {"yellow":"amarillo","green":"verde","orange":"naranja"}
Materiales = {"colores":Colores}
Materias = {"Artistica": Materiales}

print(Materias)