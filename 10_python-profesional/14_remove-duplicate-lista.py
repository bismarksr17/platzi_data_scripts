# function to remove duplicate element (not is)
def remove_duplicate(some_list):
    without_duplicate = []
    for element in some_list:
        if element not in without_duplicate:
            without_duplicate.append(element)
    return without_duplicate

def run():
    my_list = [1, 1, 3, 4, 5, 5, 6, 7, 8, 8]
    print(remove_duplicate(my_list))

if __name__ == '__main__':
    run()