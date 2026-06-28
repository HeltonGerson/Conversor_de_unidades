import engine

unidade_comprimento = {
    # Unidade base: metros
    "km": 1000.0,
    "m": 1.0,
    "cm": 0.01,
    "mm": 0.001,
}
unidade_massa = {
    # Unidade base: quilos
    "t": 1000.0,
    "kg": 1.0,
    "g": 0.001,
    "mg": 0.000001,
}
unidade_temperatura = {
    # C e F
    ("c", "f"): engine.c_para_f,
    ("f", "c"): engine.f_para_c,
    # K e C
    ("c", "k"): engine.c_para_k,
    ("k", "c"): engine.k_para_c,
    # F e K
    ("f", "k"): engine.f_para_k,
    ("k", "f"): engine.k_para_f,
}
unidade_tempo = {
    # unidade base: horas
    "dias": 24,
    "hr": 1,
    "m": 1 / 60,
    "s": 1 / 3600,
}

unidade_monetaria = {
    # moeda base: dólar
    "dólar": 1.00,
    "real": 0.19,
    "euro": 1.13,
    "yuan": 0.14,
}
