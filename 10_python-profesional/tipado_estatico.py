# se define funcion con argumento y retorno con tipado estatico
def is_palindrome(string: str) -> bool:
    string = string.replace(' ', '').lower()
    return string == string[::-1]

def run():
    # se envia un entero en lugar de una cadena para 
    # que se genere en error
    print(is_palindrome(2000))


if __name__ == '__main__':
    run()