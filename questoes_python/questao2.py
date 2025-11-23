def f(nums):
    n = len(nums)
    esperado = set(range(1, n+1))
    atual = set(nums)
    faltando = list(esperado - atual)[0]
    repetido = None
    vistos = set()
    for x in nums:
        if x in vistos:
            repetido = x
            break
        vistos.add(x)
    return (repetido, faltando)
