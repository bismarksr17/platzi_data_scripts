# funsion lambda definida como variable
palindromo = lambda x : x == x[::-1]

def run():
    # probar si es palindromo
    if palindromo('1ANA'):
        print('Es palindromo')
    else:
        print('No es palindromo')
    

if __name__ == '__main__':
    run()
