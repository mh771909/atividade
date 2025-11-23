def f(prices):
    menor = float('inf')
    lucro = 0
    for p in prices:
        menor = min(menor, p)
        lucro = max(lucro, p - menor)
    return lucro
