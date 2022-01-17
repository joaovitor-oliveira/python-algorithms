def troco(l, target):
    strike = [False] * (target + 1)
    strike[0] = True

    for moeda in l:
        valor = target
        while valor >= moeda:
            if strike[valor - moeda]:
                strike[valor] = True
            valor -= 1

    return strike[target]


if __name__ == '__main__':
    print(troco([25, 10, 5, 1], 16))
    print(troco([33, 33, 32, 31, 30, 25, 20, 14, 7, 1], 35))
