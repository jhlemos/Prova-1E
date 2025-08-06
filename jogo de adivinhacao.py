print("Nycollas Perichi Feitosa")
print("Joao Henrique lemos")
def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    max_tentativas = 10

    print("Bem-vindo ao Jogo de Adivinhação!")
    print(f"Estou pensando em um número entre 1 e 100. Você tem {max_tentativas} tentativas.")

    while tentativas < max_tentativas:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número entre 1 e 100.")
                continue

            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
                return
            elif palpite < numero_secreto:
                print("Muito baixo! Tente um número maior.")
            else:
                print("Muito alto! Tente um número menor.")
            
            print(f"Restam {max_tentativas - tentativas} tentativas.")

        except ValueError:
            print("Por favor, digite apenas números inteiros.")
    
    print(f"Game Over! O número era {numero_secreto}.")

if __name__ == "__main__":
    jogo_adivinhacao()

