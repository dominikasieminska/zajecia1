def suma_dzielnikow(n):

    suma = 0
    for i  in range(1, n):
        if n % i == 0:
            suma = suma + i

    return suma


print(suma_dzielnikow(6))
print(suma_dzielnikow(8))