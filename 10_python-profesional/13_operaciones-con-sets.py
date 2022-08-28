
my_set1 = {3, 4, 5}
my_set2 = {5, 6, 7}

# union de conjuntos
my_set3 = my_set1 | my_set2
print('Union: ', my_set3)

# interseccion de conjuntos
my_set4 = my_set1 & my_set2
print('Interseccion: ', my_set4)

# diferencia de conjuntos
my_set5 = my_set1 - my_set2
print('Diferencia set1 - set2: ', my_set5)
my_set6 = my_set2 - my_set1
print('Diferencia set2 - set1: ', my_set6)

# diferencia simetrica
# es el resultado inverso de la interseccion
my_set7 = my_set1 ^ my_set2
print('Diferencia simetrica: ', my_set7)
