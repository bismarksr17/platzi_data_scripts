def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors    

def run():
    num = input("Ingresa un número: ")
    assert num.isnumeric(), "Tiene que ingresar un numero."
    num = int(num)
    assert num > 0, 'Solo se admiten numeros positivos'
    print(divisors(num))
    print("Termino el programa")
    

if __name__ == "__main__":
    run()