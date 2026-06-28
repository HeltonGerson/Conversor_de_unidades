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
    ("C", "F"): engine.c_para_f,
    ("F", "C"): engine.f_para_c,
    # K e C
    ("C", "K"): engine.c_para_k,
    ("K", "C"): engine.k_para_c,
    # F e K
    ("F", "K"): engine.f_para_k,
    ("K", "F"): engine.k_para_f,
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
    "Euro": 1.13,
    "yuan": 0.14,
}
