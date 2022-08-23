
# funcion generadora
def my_gen():
    """Un ejemplo de generadores"""

    print('Hello work!')
    n = 0
    yield n

    print('Hello heaven!')
    n = 1
    yield n

    print('hello hell!')
    n = 2
    yield n

# se instancia la documentacióm
a = my_gen()

print(next(a))
print(next(a))
print(next(a))
print(next(a)) # StopIteration

# la funcion generadora solo tiene 3 elemtos, 
# en el ultimo print ya no hay elememtos, 
# por ello se eleva el error StopIteration

