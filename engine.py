def c_para_f(c):
    return c * 1.8 + 32


def f_para_c(f):
    return (f - 32) / 1.8


def c_para_k(c):
    return c + 273.15


def k_para_c(k):
    return k - 273.15


def f_para_k(f):
    return (f - 32) * (5 / 9) + 273.15


def k_para_f(k):
    return (k - 273.15) * (5 / 9) + 32


def conversaoUnidades(valor, origem, destino):
    return valor * (origem / destino)
