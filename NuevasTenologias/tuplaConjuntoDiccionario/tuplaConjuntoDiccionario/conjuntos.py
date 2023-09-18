#Los conjuntos son incambiables 
#Son no ordenados
#No permiten duplicados
#Son iterables
#Se construyen usando {}
#Si permiten agregar o eliminar items


usuarios = {"user1","user2","user3","user4"}

#usuario[1]="usern" Esto no se puede hacer ya que los conjuntos no poseen indices

usuarios.add("user5") #Agregar un valor al conjunto, no se puede repetir

print (usuarios) #Esto retorna los datos del conjunto en distintas posiciones


print("________________________________________________________________")

#Se puede validar si un elemento existe o no en el conjunto
print("user2" in usuarios)
print("user6" in usuarios)

#Se pueden remover elementos
print("________________________________________________________________")
usuarios.remove("user2")
print(usuarios)

for i in usuarios:
    print(i)



##Unir dos conjuntos distintos
print("________________________________________________________________")
usuariosNuevos = {"user6","user7"}

usuarios.union(usuariosNuevos)

for i in usuarios:
    print(i)



print("________________________________________________________________")
##Se pueden unir conjuntos con datos repetidos usando update
otrosUsuario = {"user1","user3","user9","user8","user7"}

usuarios.update(otrosUsuario)

for i in usuarios:
    print(i)


print("________________________________________________________________")

#Tambien se pueden crear subconjuntos

usuariosSubConjunto = frozenset(["user1","user2","user10"])

usuarios2 = {usuariosSubConjunto ,"user11", "user12"}


print(usuarios2)
