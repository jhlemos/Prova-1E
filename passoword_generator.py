import random
import string

def passoword_generator(Len_pass = 8):
    ascii_options = string.ascii_letters
    number_options =  string.digits
    punt_options = string.punctuation
    options = ascii_options + number_options + punt_options

    password_user = ""
    
    for i in range(0, Len_pass):
        passoword_user = (options)
def new_func(options):
    digit = random.choice(options)     
    passoword_user = passoword_user + digit

    return passoword_user

choice_user = input("Quantos digitos na senha?")

if choice_user.isdigit():
    choice_user = int(choice_user)
else:   
       print ("Entrada invalida!")
       quit()

response = passoword_generator(Len_pass = choice_user)
print(f"Senha gerada:\n{response}")