def desafio1(n):
    aux = 0
    if n in range(0, 10000):
        for n in range(n + 2):
            aux += n
    else:
        return 'erro'
    return aux


def desafio2a(n):
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


def desafio2b(n1, n2):
    fat1 = 1
    fat2 = 1
    if n1 > 0 or n2 > 0:
        while n1:
            fat1 *= n1
            n1 -= 1
        while n2:
            fat2 *= n2
            n2 -= 1
        return fat1 + fat2
    else:
        return "falhou"


print("desafio 1 = ", desafio1(6))
print("desafio 2a = ", desafio2a(25))
print("desafio 2b= ", desafio2b(-1, -1))
