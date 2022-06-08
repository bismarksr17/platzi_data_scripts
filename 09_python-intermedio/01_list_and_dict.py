def run():
    # lista y dict normal
    my_list = [1, 'hello', True, 4.5]
    my_dict = {'firstname': 'Facundo', 'lastname': 'Garcia'}
 
    # lista de diccionarios
    super_list = [
        {'firstname': 'Facundo', 'lastname': 'Garcia'},
        {'firstname': 'Bismark', 'lastname': 'Socompi'},
        {'firstname': 'Arturo', 'lastname': 'Flores'},
    ]
 
    # diccionario de listas
    super_dict = {
        'natural_nums' : [1,2,3,4,5],
        'integer_nums' : [-1,-2,0,1,2],
        'float_nums' : [1.1, 4.5, 6.4]
    }
   
    for key, value in super_dict.items():
        print(key, '-', value)
   
    for i in super_list:
        print(i)
 
# punto de entrada
if __name__ == '__main__':
    run()
