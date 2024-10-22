num = 0

for n in range(2):
    n = int(input("Digite um número"))
    num += n
    if n < 0:
        break
print(f"A soma dos numeros é {num}")
