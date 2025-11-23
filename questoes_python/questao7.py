def f(x, y):
    import numpy as np
    x = np.array(x)
    y = np.array(y)
    m = np.cov(x, y, bias=True)[0][1] / np.var(x)
    b = y.mean() - m * x.mean()
    return [b, m]
