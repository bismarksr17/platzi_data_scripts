
# se crea un iterador
my_list = [1,2,3,4,5]

# convertir el iterable en interador (casting)
my_iter = iter(my_list)

# recorrer el iterador con la buil-in function
while True:
    try:
        element = next(my_iter)
        print(element)
    except StopIteration:
        break

# el ciclo for no existe en Python, 
# internamente Python lo maneja como un iterador
for element in my_list:
    print(element)