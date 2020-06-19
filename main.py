def desafio1(n):
    aux = 0
    if n in range(0, 10000):
        for n in range(n + 2):
            aux += n
    else:
        return 'erro'
    return aux


def desafio2(n):
    if n <= 25:
        return "intervalo [0..25]"
    elif n <= 50:
        return f"intervalo [25..50]"
    elif n <= 75:
        return "intervalo [50..75]"
    elif n <= 100:
        return "intervalo [75..100]"
    else:
        return "fora de intervalo"


print("desafio 1 = ", desafio1(6))
print("desafio 2 = ", desafio2(25))

