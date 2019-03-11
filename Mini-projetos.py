#Importamos a biblioteca random para usarmos as suas funções
import random

#Geremos um número secreto entre 1 e 100. Para randrange(a, b + 1)
numero_secreto = random.randint(1, 100)

#Número de tentativas que o jogador terá.
chances = 5

#O jogador continuará  "Enquanto" (while) as chances forem maiores que zero
while chances > 0:
    #Informação sobre a quantidade de chances e o input, transformado em número por int()
    print("Tem {} chances" .format(chances))
    chute = int(input("Chute um número de 1 a 100: "))

    #Verificação se o input foi um número entre 1 e 100. Se não for, ele executa o else
    if(chute >= 1 and chute <= 100):

        maior = chute > numero_secreto
        menor = chute < numero_secreto
        igual = chute == numero_secreto

        #Funções para definir o que fazer em cada situação. O break foi usado em caso de acerto.
        if(maior):
            chances = chances - 1
            print("O número secreto é menor que {}" .format(chute), end="\n \n" )

        elif(menor):
            chances = chances - 1
            print("O número secreto é maior que {}".format(chute), end="\n \n")

        elif(igual):
            print("Parabéns! Você acertou. O número secreto era {}".format(chute), end="\n \n")
            break
    #else é executado quando for digitado um valor fora de 1~100, retirando uma chance. o While é reiniciado
    else:
        chances = chances - 1
        print("Você deve digitar um número entre 1 e 100", end="\n \n")

print("Você perdeu! O número secreto era {}".format(numero_secreto))


