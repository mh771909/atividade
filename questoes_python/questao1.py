def f(nums, alvo):
    mapa = {}
    for i, n in enumerate(nums):
        dif = alvo - n
        if dif in mapa:
            return (mapa[dif], i)
        mapa[n] = i
