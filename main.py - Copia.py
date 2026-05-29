userCorreta = "louis"
senhaCorreta = "louis123"

user = str(input("Digite o user:")) 
senha = str(input("Digite a senha:"))
 
if user == userCorreta and senha == senhaCorreta:
    print("Login feito com sucesso." ) 
    print(f"Olá {userCorreta} seja bem-vindo ao jogo de adivinhação, nesse jogo você tera 3 tentativas para acertar o numero correto ")
else:
    print("Dados incorrretos.")
    print("Acesso negado.")

    
import random

valor_aleatorio = random.randint(1,10)
acertou = False
tentativas = 0

while tentativas < 3 and not acertou:


    chute = int(input("Chute um número aletorio:" ))

    tentativas += 1 

    if chute > valor_aleatorio:
         print("Chute um valor mais baixo")

    elif chute < valor_aleatorio:
        print("Chute um valor mais alto")

    else:
        print("Parabéns você acertou")
        acertou = True


if not acertou:
    print(f"Suas tentativas acabaram. O numremo era {valor_aleatorio}")

 