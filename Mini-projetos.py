#Importamos a biblioteca random para usarmos as suas funções
import random

#Geremos um número secreto entre 1 e 100. Para randrange(a, b + 1)
numero_secreto = random.randint(1, 100)

#Pontos para o placar do jogador
pontos = 1000

#Escolher o nível de dificuldade
print("Escolha o nível: (1) Fácil, (2) Médio, (3) Difícil")
nivel = int(input("Nível: "))

#As chances que o jogador terá de acordo com o nível escolhido
if(nivel == 1):
    chances = 8
elif(nivel == 2):
    chances = 6
elif(nivel == 3):
    chances = 4
elif(nivel < 1 or nivel > 3):
    print("Valor {} não é um nível válido.".format(nivel))
    chances = 0


#O jogador continuará  "Enquanto" (while) as chances forem maiores que zero
while chances > 0:
    #Informação sobre a quantidade de chances e o input, transformado string em número por int()
    print("Tem {} chances" .format(chances))
    chute = int(input("Chute um número de 1 a 100: "))

    #Verificação se o input foi um número entre 1 e 100. Se não for, ele executa o else
    if(chute >= 1 and chute <= 100):

        maior = chute > numero_secreto
        menor = chute < numero_secreto
        igual = chute == numero_secreto



        #Funções para definir o que fazer em cada situação. O break foi usado em caso de acerto.
        if(igual):

            print("Parabéns! Você acertou. O número secreto era {}".format(chute), end="\n \n")
            print("Você fez {} pontos".format(pontos))
            break
        #Caso erre as mensagens para cada situação
        else:
            if(maior):
                chances = chances - 1
                print("O número secreto é menor que {}" .format(chute), end="\n \n" )

            if(menor):
                chances = chances - 1
                print("O número secreto é maior que {}".format(chute), end="\n \n")

        #pontos serão retirados a cada jogada.
        pontos = pontos - (abs(numero_secreto - chute) * chances)


    #else é executado quando for digitado um valor fora de 1~100, retirando uma chance. o While é reiniciado
    else:
        chances = chances - 1
        print("Você deve digitar um número entre 1 e 100", end="\n \n")

if(chances == 0):
    print("Você perdeu! O número secreto era {}".format(numero_secreto))


