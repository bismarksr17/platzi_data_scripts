
# CREA UN DICT, COMO LLAVE NUMEROS DE 1 AL 100, Y COMO VALOR EL CUBO DE LA LLAVE
# Y QUE NO SEAN DIVICIBLES ENTRA 3
def run():
    dic = {}
    for i in range(1, 101):
        if(i % 3 != 0):
             dic[i] = i**3
    print(dic)

def run_2():
    dic = { i : i**3 for i in range(1, 101) if i % 3 != 0 }
    print(dic)

if __name__ == '__main__':
    run_2()


