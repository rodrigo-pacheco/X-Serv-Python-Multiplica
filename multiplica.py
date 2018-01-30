#!/usr/bin/python3
# Rodrigo Pacheco Martinez-Atienza
# Doble Grado Ing. Tecnología de las Telecomunicaciones e Ing. Aeroespacial en Aeronavegación

numeros = list(range(1,11))

for i in numeros:
    print("\nTabla del ", i)
    for a in numeros:
        print(i, " por ", a, " es ", a*i)
