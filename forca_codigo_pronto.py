import os
os.system('cls')
import random as rnd

países = ['argentina','brasil','chile','peru','bolivia','uruguai','paraguai','jamaica','venezuela']
frutas = ['maça', 'banana', 'melancia', 'uva', 'morango', 'abacaxi']
instrumentos = ['violao','guitarra','bateria','teclado','piano','baixo','ukulele','cavaco']
listas = [países, frutas, instrumentos]

tema = listas[rnd.randint(0,2)]
palavra = tema[rnd.randint(0, len(tema))]

if tema == países:
    print('O TEMA É: PAÍSES')
elif tema == frutas:
    print('O TEMA É: FRUTAS')
elif tema == instrumentos:
    print('O TEMA É: INSTRUMENTOS MUSICAIS')

resposta = []

for r in range(len(palavra)):
    resposta.append('_')

erros = ["erros: "]

tentativas = 10 

for j in resposta:
        print(j,end="")
print()
while tentativas > 0:
    letra = input('Insira uma letra: ')
    print()


    if palavra.count(letra) == 0:
            tentativas -= 1
            erros.append(letra)

    for l in range(len(palavra)):

        if palavra[l] == letra:
            resposta[l] = palavra[l] 
        else:
            resposta[l] = resposta[l]

    for j in resposta:
        print(j,end="")
    print(" ")
    for p in erros:
        print(p, end=" ")

    print()    

    if resposta.count("_") == 0:

        print("Você acertou!!!!")
        break

if tentativas == 0:
    print("Você perdeu!!!")
