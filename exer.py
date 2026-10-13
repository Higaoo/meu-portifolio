print("Jogo de adivinhacao")

numero_secreto = 45

chute_str = input("Digite o seu numero: ")

print(f"Você digitou {chute_str}")

try:
    chute = int(chute_str)
except ValueError:
    print("Por favor, digite apenas números!")
    exit()

if numero_secreto == chute:
    print("Você acertou")
elif chute > numero_secreto:
    print("Você errou! O seu chute foi maior que o número secreto.")
else:
    print("Você errou! O seu chute foi menor que o número secreto.")

print("Fim de Jogo!")
