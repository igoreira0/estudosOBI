def desafio1(n):
    aux = 0
    if n in range(0, 10000):
        for n in range(n + 2):
            aux += n
    else:
        return 'erro'
    return aux


print(desafio1(6))
