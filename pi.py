import mpmath

mpmath.mp.dps = 1000  # Configurar la precisión arbitraria a 1000 decimales

def calcular_pi_ramanujan():
    suma = mpmath.mpf(0)
    for k in range(0, 10):  # Hacer la suma hasta un valor razonable (puedes aumentar este límite)
        numerador = mpmath.factorial(4*k) * (1103 + 26390*k)
        denominador = (mpmath.factorial(k)**4) * 396**(4*k)
        termino = numerador / denominador
        suma += termino
    return 1 / ((mpmath.sqrt(8) / 9801) * suma)

pi_aproximado = calcular_pi_ramanujan()
print(pi_aproximado)
