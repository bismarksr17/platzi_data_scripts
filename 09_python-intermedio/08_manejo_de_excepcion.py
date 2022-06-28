def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors    

def run():
    try:
        num = int(input("Ingresa un número: "))
        if num < 0:
            raise TypeError('No se aceptan valores negativos')
        print(divisors(num))
        print("Termino el programa")
    except ValueError:
        print("Debes ingresar un numero")
    except TypeError as te:
        print(te)
        return False


if __name__ == "__main__":
    run()