while True:
    valores = input().split()
    m = int(valores[0])
    n = int(valores[1])

    if m <= 0 or n <= 0:
        break

    menor = min(m, n)
    maior = max(m, n)

    soma = 0
    for i in range(menor, maior + 1):
        print(i, end=' ')
        soma += i
    print(f"Sum={soma}")
