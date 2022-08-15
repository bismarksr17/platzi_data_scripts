
def make_division_by(n):
    def multiplicar(x):
        return n * x
    return multiplicar


division_by_3 = make_division_by(3)
print(division_by_3(18))