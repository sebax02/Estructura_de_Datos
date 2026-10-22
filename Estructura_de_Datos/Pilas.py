#Crear una pila vacia  
pila=[]

#PUSH: agregar elementos
pila.append("Libro A")
pila.append("Libro B")
pila.append("Libro C")

print("Pila inicial:", pila)

#PEEK: Consultar el ultimo elemento
print("Elemento en la cima:", pila[-1])

#POP: Retirar el ultimo elemento
retirado = pila.pop()
print("Elemento retirado:", retirado)

#Mostrar la pila actualizada
print("Pila final:", pila)