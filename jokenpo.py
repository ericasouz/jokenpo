import random

print("Bem-vindo ao Jokenpô!")
print("Digite 'pedra', 'papel' ou 'tesoura' para jogar.")
print("Ou digite 'sair' para encerrar o jogo.")

escolhas = ["pedra", "papel", "tesoura"]

while True:
    jogador = input("Sua escolha: ").lower()

    if jogador == "sair":
        print("Obrigado por jogar! Até a próxima")
        break

    if jogador not in escolhas:
        print("Opção inválida. Tente novamente.")
        continue

    computador = random.choice(escolhas)
    print(f"O Computador escolheu: {computador}")

    if jogador == computador:
        print("Empate!")
    elif (
        (jogador == "pedra" and computador == "tesoura") or
        (jogador == "papel" and computador == "pedra") or
        (jogador == "tesoura" and computador == "papel")
    ):
        print("Você Venceu! 🎉")
    else:
        print("Você Perdeu! 😢")