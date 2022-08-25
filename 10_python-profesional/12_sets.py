# ================================================================
# CREAR UN SET
# ================================================================
# set con numeros
my_set = {3, 4, 5}
print('my_set = ', my_set)

# set con diferentes tipos de datos
# al imprimir el set, se muestra en otro orden
my_set2 = {'hola', 23.3, False, True}
print('my_set2 = ', my_set2)

# al repetir numeros en un set, 
# python elimina los repetidos
my_set3 = {3, 3, 2}
print('my_set3 = ', my_set3)

# al tener un elemento inmutable,
# python aroja un error
my_set4 = {[1, 2, 3], 4}
print('my_set4 = ', my_set4)


# ==================================================================
# CREAR UN SET VACIO
# ==================================================================
# al usar llaves, se crea un dict
empty_set = {}
print(type(empty_set))

# se usa el built-in 'set'
empty_set = set()
print(type(empty_set))

# ==================================================================
# CASTING CON SETS
# ==================================================================
# al usar una lista con elementos repetidos, 
# 'set' eliminara todos los repetidos
my_list = [1, 1, 2, 3, 4, 4, 5]
my_set = set(my_list)
print(my_set)

# ==================================================================
# AÑADIR ELEMENTOS A UN SET
# ==================================================================
my_set = {1, 2, 3}
# agrega un elemento al set
my_set.add(4)
# agrega varios elementos al set
# se recorre la lista y va agragando todos los elementos
my_set.update([1, 2, 5])
# # agrega varios elementos de varias estructuras
# se recorre las estructuras, y va agragando todos los elementos
my_set.update([1, 7, 2], {6, 8})
# si algun elemento se repite, es eliminado


# ==================================================================
# ELIMINAR ELEMENTOS DEL SET
# ==================================================================
my_set = {1, 2, 3, 4, 5, 6, 7}
# elimina el elemento indicado,
# si el elemento indicado no existe, no pasa nada
my_set.discard(1)
# elimina el elemento indicado,
# si el elemento indicado no existe, se genera un KeyError
my_set.remove(2)
# elimina un elemento aleatorio del set, 
# el elemento eliminado es retornado
my_set.pop()
# limpia el set
my_set.clear()