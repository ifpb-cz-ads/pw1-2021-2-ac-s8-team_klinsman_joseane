import random
n = random.randint(1, 10)

for x in range(3, 0, -1):
    escolha = int(input(f"Escolha um número entre 1 e 10, você tem {x} chances:"))
    if (escolha == n):
        print("Você acertou!")
        break
    else:
        print("Você errou.")

