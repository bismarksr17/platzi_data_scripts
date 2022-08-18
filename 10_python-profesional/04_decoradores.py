# funcion decorador
def decorador(func):
    # envoltura
    def wrapper():
        print('Esto se añade a mi funcion original')
        func()
    return wrapper

# funcion normal
def saludo():
    print('Hola!')

# se ejecuta funcion normal, solo se escribira un hola!
saludo()

print('--------------------------------------------------------------------')

# se decora funcion normal
saludo = decorador(saludo)
saludo()

print('--------------------------------------------------------------------')
# las dos anteriores lineas, forman un patron,
# se puede crear la funcion y decorar de la siguiente manera:
@decorador
def saludo():
    print('Hola!')

# se ejecuta la funcion decorada
saludo()