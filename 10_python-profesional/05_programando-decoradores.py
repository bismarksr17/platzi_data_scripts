from datetime import datetime

# decorador para calcular tiempo de ejecucion de una función
# se usa *args y **kwargs para validad cualquier numero de parametros
def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print('Pasaron ' + str(time_elapsed.total_seconds()) + ' segundos')
    return wrapper

# se decora la funcion
@execution_time
def random_func():
    for _ in range(1, 1000000000):
        pass

# se ejecuta la funcion
random_func()

# se decora otra funcion con parametros
@execution_time
def sumar(a, b):
    return a + b

# se ejecuta la funcion con parametros
sumar(13, 43)
