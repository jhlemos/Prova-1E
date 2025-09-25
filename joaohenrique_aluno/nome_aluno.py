# Lista com alguns nomes de alunos já cadastrados
lista_alunos = ["Ana", "Bruno", "Carla", "Daniel"]

# Define o número máximo de tentativas
tentativas_max = 6
tentativas = 0

# Função para montar o nome letra por letra
def montar_nome_letra_por_letra():
    nome_montado = ""
    print("Digite uma letra por vez. Quando terminar, pressione Enter sem digitar nada.")
    while True:
        letra = input("Digite uma letra (ou Enter para finalizar): ")
        if letra == "":
            break
        if len(letra) == 1:  # Garante que é apenas uma letra
            nome_montado += letra
        else:
            print("Por favor, digite apenas uma letra por vez!")
    return nome_montado.strip().title()  # Normaliza o nome (remove espaços e formata)

# Pergunta ao usuário como ele quer inserir o nome
print("Escolha uma opção:")
print("1 - Digitar o nome completo")
print("2 - Montar o nome letra por letra")
opcao = input("Digite 1 ou 2: ")

# Loop para permitir até 6 tentativas
while tentativas < tentativas_max:
    tentativas += 1
    
    # Verifica a opção escolhida
    if opcao == "1":
        nome_digitado = input("Digite o nome do aluno: ").strip().title()
    elif opcao == "2":
        print(f"Tentativa {tentativas} de {tentativas_max}")
        nome_digitado = montar_nome_letra_por_letra()
    else:
        print("Opção inválida! Usando modo de digitar o nome completo.")
        nome_digitado = input("Digite o nome do aluno: ").strip().title()
    
    # Verifica se o nome está na lista
    if nome_digitado in lista_alunos:
        print("O nome", nome_digitado, "está na lista! Está correto!")
        break  # Sai do loop se o nome for encontrado
    else:
        print("O nome", nome_digitado, "não está na lista. Tentativas restantes:", tentativas_max - tentativas)
        
# Se esgotar as tentativas, exibe mensagem
if tentativas == tentativas_max and nome_digitado not in lista_alunos:
    print("Você esgotou todas as", tentativas_max, "tentativas. Tente novamente mais tarde!")