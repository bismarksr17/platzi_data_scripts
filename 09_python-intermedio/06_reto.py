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

# extraccion de nombres con MAP que sean devs de python
def extraer_nombres():
    # se filtra a los devs python
    python_dev = list(filter(lambda x: x['language']=='python', DATA))
    # se aplica MAP para extraer el nombre de cada trabajador
    names = list(map(lambda x: x['name'], python_dev))
    return names

# mayor de 18 con list comprehensins
def mayores_de_18():
    nombres = [i['name'] for i in DATA if i['age']>18]
    return nombres

# agrega el parametro OLD si es mayor de 70
# suma de diccionarios {**x, **y}, solo funciona en python 3.8 e inferiores
def add_old():
    dic = [{**i, **{'old': i['age']>70}} for i in DATA]
    return dic

def run():
    print(add_old())

if __name__ == '__main__':
    run()