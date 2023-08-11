def tower_builder(n_floors):
    tower = list()
    k = 1
    for i in range(n_floors):
        tower.append(((n_floors-i-1)*' ')+k*'*'+((n_floors-i-1)*' '))
        k+=2
    return tower
