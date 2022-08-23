
my_list = [1, 2, 3, 4, 5, 6]

# lista generada con list comprehensions
list_second_list = [i**2 for i in my_list]

# generador con generator expression
list_second_gen = (i**2 for i in my_list)

print(next(list_second_gen))
print(next(list_second_gen))
print(next(list_second_gen))