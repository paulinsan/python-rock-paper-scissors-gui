# === importações aplicadas ===
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import random

# === cores ===
co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"   # green / verde
co5 = "#e85151"   # red / vermelha
fundo = "#3b3b3b"

# === configuração da janela ===

janela = Tk()
janela.title('')
janela.geometry('320x360')
janela.configure(bg=fundo)

# === divisão das janelas ===
# --- parte de cima ---
frame_cima = Frame(
    janela,
    width=320,
    height=130,
    bg=co1,
    relief='raised'
)
frame_cima.grid(row = 0, column = 0, sticky = NW)

# --- parte de baixo ---
frame_baixo = Frame(
    janela,
    width=320,
    height=380,
    bg=co0,
    relief='flat'
)
frame_baixo.grid(row = 1, column = 0, sticky = NW)

# --- estilo da janela ---
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# === configuração do "frame_cima" ===
# --- jogador 1 ---
jogador1 = Label(
    frame_cima,
    text= "Você",
    height=1,
    anchor='center',
    font=('Ivy 10 bold'),
    bg=co1,
    fg=co0
)
jogador1.place(x=66, y=100)
jogador1_linha = Label(
    frame_cima,
    text= "",
    height=10,
    anchor='center',
    font=('Ivy 10 bold'),
    bg=co0,
    fg=co0
)
jogador1_linha.place(x=0, y=0)
jogador1_pontos = Label(
    frame_cima,
    text= "0",
    height=1,
    anchor='center',
    font=('Ivy 40 bold'),
    bg=co1,
    fg=co0
)
jogador1_pontos.place(x=70, y=35)

# --- divisão dos pontos ---
jogo_doispontos = Label(
    frame_cima,
    text= ":",
    height=1,
    anchor='center',
    font=('Ivy 30 bold'),
    bg=co1,
    fg=co0
)
jogo_doispontos.place(x=145, y=37)

# --- jogador 2 ---
jogador2_pontos = Label(
    frame_cima, 
    text= "0",
    height=1,
    anchor='center',
    font=('Ivy 40 bold'),
    bg=co1,
    fg=co0
)
jogador2_pontos.place(x=207, y=35)
jogador2 = Label(
    frame_cima,
    text= "Computador",
    height=1,
    anchor='center',
    font=('Ivy 10 bold'),
    bg=co1,
    fg=co0
)
jogador2.place(x=186, y=100)
jogador2_linha = Label(
    frame_cima,
    text= "",
    height=10,
    anchor='center',
    font=('Ivy 10 bold'),
    bg=co0,
    fg=co0
)
jogador2_linha.place(x=314, y=0)

# --- canto do placar ---
jogo_linha = Label(
    frame_cima,
    text= "",
    width=314,
    anchor='center',
    font=('Ivy 1 bold'),
    bg=co3,
    fg=co0
)
jogo_linha.place(x=0, y=125)

# === funções ===
global voce
global computador
global rodadas
global pnt_voce
global pnt_computador

pnt_voce = 0
pnt_computador = 0
rodadas = 5

# --- logica do jogo --- (==== funções ===)
def jogar(b):
    global rodadas
    global pnt_voce
    global pnt_computador

    if rodadas > 0:
        print(rodadas)
        opcoes = ["Pedra", "Papel", "Tesoura"]
        computador = random.choice(opcoes)
        voce = b
    # --- caso seja igual ---
        if voce == computador:
                print("Empate")
                jogador1_linha['bg'] = co0
                jogador2_linha['bg'] = co0
                jogo_linha['bg'] = co3

     # --- caso voce vença ---
        elif voce == "Pedra" and computador == "Tesoura":
                print("Você venceu")
                jogador1_linha['bg'] = co4
                jogador2_linha['bg'] = co0
                jogo_linha['bg'] = co0

                pnt_voce += 10
        
        elif voce == "Papel" and computador == "Pedra":
                print("Você venceu")
                jogador1_linha['bg'] = co4
                jogador2_linha['bg'] = co0
                jogo_linha['bg'] = co0

                pnt_voce += 10
        
        elif voce == "Tesoura" and computador == "Papel":
                print("Você venceu")
                jogador1_linha['bg'] = co4
                jogador2_linha['bg'] = co0
                jogo_linha['bg'] = co0

                pnt_voce += 10

        # --- caso voce perca ---
        else:
                print("Você perdeu")
                jogador1_linha['bg'] = co0
                jogador2_linha['bg'] = co4
                jogo_linha['bg'] = co0

                pnt_computador += 10

        # --- pontuação atual ---
        jogador1_pontos['text'] = pnt_voce
        jogador2_pontos['text'] = pnt_computador

        # --- rodadas atual ---
        rodadas -= 1

    
    else:
        fim_do_jogo()


# --- iniciar jogo --- (=== funções ===)
def iniciar_jogo():
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

# --- botão pedra --- (=== configuração do "frame_baixo" ===)
    icon_1 = Image.open("imagens/pedra.png")
    icon_1 = icon_1.resize((70, 70), Image.Resampling.LANCZOS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    b_icon_1 = Button(
        frame_baixo,
        command=lambda: jogar("Pedra"),
        width=70,
        image=icon_1,
        compound=CENTER,
        bg=co0,
        fg=co0,
        font=('Ivy 10 bold'),
        anchor=CENTER,
        relief=FLAT
    )
    b_icon_1.place(x=30, y=50)

# --- botão papel --- (=== configuração do "frame_baixo" ===)  
    icon_2 = Image.open("imagens/papel.png")
    icon_2 = icon_2.resize((70, 70), Image.Resampling.LANCZOS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    b_icon_2 = Button(
        frame_baixo,
        command=lambda: jogar("Papel"),
        width=70,
        image=icon_2,
        compound=CENTER,
        bg=co0,
        fg=co0,
        font=('Ivy 10 bold'),
        anchor=CENTER,
        relief=FLAT
    )
    b_icon_2.place(x=120, y=50)

# --- botão tesoura --- (=== configuração do "frame_baixo" ===)
    icon_3 = Image.open("imagens/tesoura.png")
    icon_3 = icon_3.resize((70, 70), Image.Resampling.LANCZOS)
    icon_3 = ImageTk.PhotoImage(icon_3)
    b_icon_3 = Button(
        frame_baixo,
        command=lambda: jogar("Tesoura"),
        width=70,
        image=icon_3,
        compound=CENTER,
        bg=co0,
        fg=co0,
        font=('Ivy 10 bold'),
        anchor=CENTER,
        relief=FLAT
    )
    b_icon_3.place(x=210, y=50)


# --- finalizar jogo --- (=== funções ===)

def fim_do_jogo():
    print("Jogo terminou! ")


# === configuração do "frame_baixo" ===
# --- botão jogar ---
b_jogar = Button(
    command=iniciar_jogo,
    width=20,
    text="Jogar",
    bg=fundo,
    fg=co0,
    font=('Ivy 10 bold'),
    anchor=CENTER,
    relief=FLAT
)
b_jogar.place(x=75, y=295)


janela.mainloop()
