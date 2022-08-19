class EvenNumbers:
    """Clase que implementa un iterador 
    de todos los numeros pares, o los numeros
    pares hasta un maximo"""

    # constructor de la clase
    def __init__(self, max=None):
        self.max = max
    
    # contine e inicializa elementos o atributos 
    # que se nececitan para que el iterador funcione
    def __iter__(self):
        self.num = 0
        return self

    # retorna, extrae cada uno de los elememtos del iterador
    # en este caso, todos los numeros pares hasta un maximo (si existe)
    def __next__(self):
        if not self.max or self.num <= self.max:
            result = self.num
            self.num += 2
            return result
        else:
            # se eleva el error StopIteration
            raise StopIteration
