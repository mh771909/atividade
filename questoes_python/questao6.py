def f(x):
    nums = "123456789"
    ops = ["", "+", "-"]
    resultados = []
    def gerar(i, expressao):
        if i == 9:
            if eval(expressao) == x:
                resultados.append(expressao + "==" + str(x))
            return
        for op in ops:
            gerar(i+1, expressao + op + nums[i])
    gerar(1, "1")
    return resultados
