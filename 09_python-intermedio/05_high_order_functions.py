# constante
DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

# extraer nombres de todos los trabajadores que saben python
def extraer_nombre():
    nombres = [i['name'] for i in DATA if i['language']=='python']
    return nombres

# estraer lo trabajadores mayores de 18 años
def mayores_a_18():
    # filtramos los mayores de 18
    lista_adultes = list(filter(lambda x:x['age']>18, DATA))
    # extraemos nombres
    nombres = list(map(lambda x:x['name'],lista_adultes))
    return nombres

# funcion que agrega el parametro 'old' al diccionatio si trabajador es mayor de 70
def add_old(x):
    if x['age'] > 70:
        x['old'] = True
    else:
        x['old'] = False
    return x

# agregar parametro 'old' si trabajador es mayor de 70
# se puede realizar de dos formas:
def old():
    # forma 1: con operador |, que agrega un diccionario a otro
    # solo funciona a partir de python 3.9
    # datos = list(map(lambda x: x | {'old':x['age']>70}, DATA))

    # forma 2: con una funcion secundaria que agrega el parametro 'old'
    datos = list(map(add_old, DATA))

    return datos

# principal
def run():
    print(old())


# punto de entrada
if __name__=='__main__':
    run()