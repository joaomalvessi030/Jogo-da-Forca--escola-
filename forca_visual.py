import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import random as rnd

# Definindo a palavra e o tema da vez

países = ['argentina', 'brasil', 'chile', 'peru', 'bolivia', 'uruguai', 'paraguai', 'jamaica', 'venezuela', 'frança', 'dinamarca', 'finlandia',       'alemanha', 'portugal', 'espanha', 'grecia', 'inglaterra', 'egito', 'angola', 'cingapura', 'madagascar', 'china']
frutas = ['maça', 'banana', 'melancia', 'uva', 'morango', 'abacaxi','framboesa','mirtilo', 'abacate', 'tomate', 'acerola', 'bergamota', 'amora', 'caqui', 'kiwi', 'cereja'] 
instrumentos = ['violao', 'guitarra', 'bateria', 'teclado', 'piano', 'baixo', 'ukulele', 'cavaco', 'tambor', 'gaita', 'violino', 'viola', 'harpa', 'flauta', 'trompete', 'saxofone', 'tuba', 'clarinete']
times = ['corinthians', 'flamengo', 'gremio', 'vasco', 'botafogo', 'paysandu', 'bahia', 'criciuma', 'chapecoense', 'juventude', 'caxias', 'fluminense', 'fortaleza', 'cuiaba']
animais = ['cachorro', 'gato', 'papagaio', 'ornitorrinco', 'elefante', 'iguana', 'avestruz', 'flamingo', 'coala', 'baleia', 'capivara', 'chimpanze', 'aranha', 'dromedario', 'hipopotano', 'guaxinim', 'tubarao', 'golfinho']

# Função para gerar a palavra
def gerar_palavra():
    listas = [países, frutas, instrumentos, times, animais]

    tema = listas[rnd.randint(0, 4)]
    palavra = tema[rnd.randint(0, len(tema) - 1)]

    if tema == países:
        nome_tema = 'PAÍSES'
    elif tema == frutas:
        nome_tema = 'FRUTAS'
    elif tema == instrumentos:
        nome_tema = 'INSTRUMENTOS MUSICAIS'
    elif tema == times:
        nome_tema = 'TIMES DE FUTEBOL'
    elif tema == animais:
        nome_tema = 'ANIMAIS'

    return palavra, nome_tema

palavra, nome_tema = gerar_palavra()

    # Resposta
resposta = ['_'] * len(palavra)

    # Erros
erros = []

    # Tentativas
tentativas = 10

    # Criando a janela principal
janela = tk.Tk()
janela.title("Jogo da Forca")

    # Classe para gerenciar as imagens
class App:
        def __init__(self, master):
            self.master = master
            self.imagens = {}  # Dicionário para armazenar as imagens
            self.label_imagem = tk.Label(master)
            self.label_imagem.pack()
            self.carregar_imagens()  # Carrega todas as imagens no dicionário

        def carregar_imagens(self):
            caminho_base = 'imagem'
            for i in range(1, 11):  # Loop de 1 a 10
                caminho_imagem = f'{caminho_base}{11-i}.png'  # Inverte a ordem das imagens
                self.imagens[11-i] = PhotoImage(file=caminho_imagem)

        def atualizar_imagem(self, tentativas):
            # Atualiza a imagem com base no número de tentativas
            imagem_index = 11 - tentativas  # Inverte o índice da imagem
            if imagem_index in self.imagens:
                self.label_imagem.config(image=self.imagens[imagem_index])

    # Instancia a classe App
app = App(janela)
app.atualizar_imagem(tentativas)  # Atualiza a imagem inicial

    # Função para sair
def sair():
     janela.destroy()

    # Função para atualizar a palavra secreta, os erros e as imagens
def atualizar_display():
        label_palavraSecreta.config(text=' '.join(resposta))
        label_erros.config(text='Erros: ' + ' '.join(erros))
        app.atualizar_imagem(tentativas)

# Sair depois do pedido denovo

    # Função para verificar a letra inserida
def testar_letra():
        global tentativas
        letra = entry_letra.get().lower()
        entry_letra.delete(0, tk.END)

        if letra in palavra:
            for idx, char in enumerate(palavra):
                if char == letra:
                    resposta[idx] = letra
        else:
            if letra not in erros:
                erros.append(letra)
                tentativas -= 1

        atualizar_display()

        if tentativas <= 0:
            messagebox.showinfo("Jogo da Forca", f"Você perdeu!!! (A resposta era {palavra})")

            jogar_denovo = tk.Tk()
            jogar_denovo.title("Deseja jogar denovo?")

            def sairDnv():
                janela.destroy()
                jogar_denovo.destroy()

            def comecarDnv():
                 gerar_palavra()
                 tentativas = 10
                 atualizar_display()
                 jogar_denovo.destroy()

                 return tentativas
                 

            deseja = tk.Label(jogar_denovo, text='Deseja jogar novamente?')
            deseja.pack()

            botaoSim = tk.Button(jogar_denovo, text='Sim', command=comecarDnv)
            botaoSim.pack()
            botaoNao = tk.Button(jogar_denovo, text='Não', command=sairDnv)
            botaoNao.pack()


        elif '_' not in resposta:
            messagebox.showinfo("Jogo da Forca", "Você acertou!!!!")

            jogar_denovo = tk.Tk()
            jogar_denovo.title("Deseja jogar denovo?")

            def sairDnv():
                janela.destroy()
                jogar_denovo.destroy()

            def comecarDnv():
                 gerar_palavra()
                 tentativas =+ 10
                 atualizar_display()
                 jogar_denovo.destroy()

                 return tentativas
                 

            deseja = tk.Label(jogar_denovo, text='Deseja jogar novamente?')
            deseja.pack()

            botaoSim = tk.Button(jogar_denovo, text='Sim', command=comecarDnv)
            botaoSim.pack()
            botaoNao = tk.Button(jogar_denovo, text='Não', command=sairDnv)
            botaoNao.pack()

    # Adicionando o tema
label_tema = tk.Label(janela, text=f'O TEMA É: {nome_tema}')
label_tema.pack()

    # Adicionando as '_' para a palavra secreta
label_palavraSecreta = tk.Label(janela, text=' '.join(resposta))
label_palavraSecreta.pack()

    # Adicionando o rótulo e campo de entrada para as letras
label_letra = tk.Label(janela, text="Insira uma letra:")
label_letra.pack()
entry_letra = tk.Entry(janela)
entry_letra.pack()

    # Adicionando o botão para testar a letra
botao_testar = tk.Button(janela, text="Testar", command=testar_letra)
botao_testar.pack(padx=10, pady=10)

    # Erros
label_erros = tk.Label(janela, text='Erros: ' + ' '.join(erros))
label_erros.pack()

    # Botão de saída
botao_sair = tk.Button(janela, text="Sair", command=sair)
botao_sair.place(relx=1.0, rely=0.0, anchor='ne')

    # Inicia a janela principal
janela.mainloop()