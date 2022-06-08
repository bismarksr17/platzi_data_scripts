
# IMPRIMIR LOS CUADRADOS DE TODOS LOS NUMEROS DE 0 AL 100 Y MULTIPLOS DE 3
def run():
    lista = [i**2 for i in range(0, 101) if i % 3 == 0]
    print(lista)

# IMPRIMIR TODOS LOS NUMEROS MULTIPLOS DE 4, 6 Y 9, MENORES A 5 DIGITOS
def run_2():
    lista = [i for i in range(100000) if (i % 4 == 0 and i % 6 == 0 and i % 9 == 0)]
    print(lista)

if __name__ == '__main__':
    run_2()
