
#Autor: Cristopher Obaco

#Crear una pila vacia  
calificaciones=[]

#PUSH: agregar elementos
calificaciones.append("10")
calificaciones.append("20")
calificaciones.append("30")
calificaciones.append("40")
calificaciones.append("50")
print("------------------------------------------------------------------")
print("Pila inicial:", calificaciones)

#PEEK: Consultar el ultimo elemento
print("Elementos en la cima:", calificaciones[-1],",", calificaciones[-2])

#POP: Retirar el ultimo elemento
retirado = calificaciones.pop(-1), calificaciones.pop(-1)
print("Elemento retirado:", retirado)

print("------------------------------------------------------------------")
#Mostrar la pila actualizada
print("Pila final:", calificaciones)

#PEEK: Consultar el ultimo elemento
print("Elementos en la cima:", calificaciones[-1],",", calificaciones[-2])

#POP: Retirar el ultimo elemento
retirado = calificaciones.pop(-1), calificaciones.pop(-1)
print("Elemento retirado:", retirado)

#Mostrar la pila actualizada
print("Pila final:", calificaciones)

