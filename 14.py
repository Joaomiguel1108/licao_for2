num2 = 0
num3 = 0
num = 0

for n in range(20):
    n = int(input("Digite um número"))
    if n >= 1 and n <=100:
        num +=1
    elif n >= 101 and n <=200:
        num3 +=1
    elif n > 200:
        num2 +=1
print(f"tem {num} números entre 1 e 100, {num3} números entre 101 e 200, e {num2} maiores que 200")
