import tkinter as tk
from pathlib import Path
from PIL import Image, ImageTk

from jogo import (
    OPCOES,
    escolher_computador,
    verificar_vencedor,
    criar_placar,
    atualizar_placar
)


# === CORES ===

COR_BRANCO = "#FFFFFF"
COR_PRETO = "#333333"
COR_LARANJA = "#FCC058"
COR_VERDE = "#34EB3D"
COR_VERMELHO = "#E85151"
COR_FUNDO = "#3B3B3B"


# === CONFIGURAÇÕES ===

TOTAL_RODADAS = 5

PASTA_IMAGENS = Path(__file__).parent / "imagens"


class InterfaceJogo:

    def __init__(self, janela):
        self.janela = janela

        self.janela.title("Pedra, Papel ou Tesoura")
        self.janela.geometry("320x420")
        self.janela.resizable(False, False)
        self.janela.configure(bg=COR_FUNDO)

        # Estado da partida
        self.placar = criar_placar()
        self.rodadas_restantes = TOTAL_RODADAS

        # Guarda as imagens para que não sejam removidas da memória
        self.imagens = {}

        # Cria as áreas da interface
        self.criar_frames()
        self.criar_placar()
        self.criar_area_jogo()

    # === ESTRUTURA DA JANELA ===

    def criar_frames(self):
        self.frame_cima = tk.Frame(
            self.janela,
            width=320,
            height=130,
            bg=COR_PRETO
        )
        self.frame_cima.pack()

        self.frame_baixo = tk.Frame(
            self.janela,
            width=320,
            height=290,
            bg=COR_BRANCO
        )
        self.frame_baixo.pack()

        # Impede que os frames mudem de tamanho
        self.frame_cima.pack_propagate(False)
        self.frame_baixo.pack_propagate(False)

    # === PLACAR VISUAL ===

    def criar_placar(self):
        self.lbl_pontos_jogador = tk.Label(
            self.frame_cima,
            text="0",
            font=("Arial", 32, "bold"),
            bg=COR_PRETO,
            fg=COR_BRANCO
        )
        self.lbl_pontos_jogador.place(x=65, y=25)

        self.lbl_dois_pontos = tk.Label(
            self.frame_cima,
            text=":",
            font=("Arial", 28, "bold"),
            bg=COR_PRETO,
            fg=COR_BRANCO
        )
        self.lbl_dois_pontos.place(x=150, y=30)

        self.lbl_pontos_computador = tk.Label(
            self.frame_cima,
            text="0",
            font=("Arial", 32, "bold"),
            bg=COR_PRETO,
            fg=COR_BRANCO
        )
        self.lbl_pontos_computador.place(x=215, y=25)

        tk.Label(
            self.frame_cima,
            text="Você",
            font=("Arial", 10, "bold"),
            bg=COR_PRETO,
            fg=COR_BRANCO
        ).place(x=75, y=85)

        tk.Label(
            self.frame_cima,
            text="Computador",
            font=("Arial", 10, "bold"),
            bg=COR_PRETO,
            fg=COR_BRANCO
        ).place(x=190, y=85)

        self.lbl_linha_jogador = tk.Label(
            self.frame_cima,
            bg=COR_BRANCO,
            width=2
        )
        self.lbl_linha_jogador.place(x=0, y=0, width=5, height=120)

        self.lbl_linha_computador = tk.Label(
            self.frame_cima,
            bg=COR_BRANCO,
            width=2
        )
        self.lbl_linha_computador.place(
            x=315, y=0, width=5, height=120
        )

        self.lbl_linha_inferior = tk.Label(
            self.frame_cima,
            bg=COR_LARANJA
        )
        self.lbl_linha_inferior.place(
            x=0, y=125, width=320, height=5
        )

    # === ÁREA PRINCIPAL ===

    def criar_area_jogo(self):
        self.lbl_mensagem = tk.Label(
            self.frame_baixo,
            text="Escolha sua jogada!",
            font=("Arial", 11, "bold"),
            bg=COR_BRANCO,
            fg=COR_PRETO
        )
        self.lbl_mensagem.place(x=0, y=15, width=320)

        self.lbl_escolha_computador = tk.Label(
            self.frame_baixo,
            text="",
            font=("Arial", 10),
            bg=COR_BRANCO,
            fg=COR_PRETO
        )
        self.lbl_escolha_computador.place(
            x=0, y=42, width=320
        )

        self.frame_botoes = tk.Frame(
            self.frame_baixo,
            bg=COR_BRANCO
        )
        self.frame_botoes.place(x=15, y=85)

        self.botoes_opcoes = []

        for indice, opcao in enumerate(OPCOES):
            imagem = Image.open(
                PASTA_IMAGENS / f"{opcao.lower()}.png"
            )
            imagem = imagem.resize(
                (70, 70),
                Image.Resampling.LANCZOS
            )

            self.imagens[opcao] = ImageTk.PhotoImage(imagem)

            botao = tk.Button(
                self.frame_botoes,
                image=self.imagens[opcao],
                command=lambda escolha=opcao: self.jogar(escolha),
                bg=COR_BRANCO,
                activebackground=COR_BRANCO,
                relief=tk.FLAT,
                cursor="hand2"
            )
            botao.grid(
                row=0,
                column=indice,
                padx=5
            )

            self.botoes_opcoes.append(botao)

        self.lbl_rodadas = tk.Label(
            self.frame_baixo,
            text=f"Rodadas restantes: {self.rodadas_restantes}",
            font=("Arial", 10),
            bg=COR_BRANCO,
            fg=COR_PRETO
        )
        self.lbl_rodadas.place(
            x=0, y=175, width=320
        )

        self.btn_reiniciar = tk.Button(
            self.frame_baixo,
            text="Jogar novamente",
            command=self.reiniciar_jogo,
            width=20,
            bg=COR_FUNDO,
            fg=COR_BRANCO,
            font=("Arial", 10, "bold"),
            relief=tk.FLAT,
            cursor="hand2"
        )

    # === EXECUTAR UMA RODADA ===

    def jogar(self, escolha_jogador):
        if self.rodadas_restantes <= 0:
            return

        escolha_computador = escolher_computador()

        resultado = verificar_vencedor(
            escolha_jogador,
            escolha_computador
        )

        atualizar_placar(self.placar, resultado)
        self.rodadas_restantes -= 1

        # Atualiza as informações da tela
        self.lbl_pontos_jogador.config(
            text=self.placar["jogador"]
        )
        self.lbl_pontos_computador.config(
            text=self.placar["computador"]
        )

        self.lbl_escolha_computador.config(
            text=f"Computador escolheu: {escolha_computador}"
        )

        self.lbl_rodadas.config(
            text=f"Rodadas restantes: {self.rodadas_restantes}"
        )

        self.atualizar_resultado_visual(resultado)

        if self.rodadas_restantes == 0:
            self.finalizar_jogo()

    # === RESULTADO VISUAL DA RODADA ===

    def atualizar_resultado_visual(self, resultado):
        # Reseta as cores antes de mostrar o novo resultado
        self.lbl_linha_jogador.config(bg=COR_BRANCO)
        self.lbl_linha_computador.config(bg=COR_BRANCO)

        if resultado == "jogador":
            self.lbl_mensagem.config(
                text="Você venceu a rodada!",
                fg=COR_VERDE
            )
            self.lbl_linha_jogador.config(bg=COR_VERDE)

        elif resultado == "computador":
            self.lbl_mensagem.config(
                text="Você perdeu a rodada!",
                fg=COR_VERMELHO
            )
            self.lbl_linha_computador.config(bg=COR_VERDE)

        else:
            self.lbl_mensagem.config(
                text="A rodada terminou empatada!",
                fg=COR_LARANJA
            )

    # === FINALIZAR PARTIDA ===

    def finalizar_jogo(self):
        for botao in self.botoes_opcoes:
            botao.config(state=tk.DISABLED)

        if self.placar["jogador"] > self.placar["computador"]:
            mensagem = "Você ganhou a partida!"
            cor = COR_VERDE

        elif self.placar["jogador"] < self.placar["computador"]:
            mensagem = "Você perdeu a partida!"
            cor = COR_VERMELHO

        else:
            mensagem = "A partida terminou empatada!"
            cor = COR_LARANJA

        self.lbl_mensagem.config(
            text=mensagem,
            fg=cor
        )

        self.lbl_rodadas.config(
            text="Partida finalizada!"
        )

        self.btn_reiniciar.place(
            x=55, y=230
        )

    # === REINICIAR PARTIDA ===

    def reiniciar_jogo(self):
        self.placar = criar_placar()
        self.rodadas_restantes = TOTAL_RODADAS

        self.lbl_pontos_jogador.config(text="0")
        self.lbl_pontos_computador.config(text="0")

        self.lbl_mensagem.config(
            text="Escolha sua jogada!",
            fg=COR_PRETO
        )

        self.lbl_escolha_computador.config(text="")

        self.lbl_rodadas.config(
            text=f"Rodadas restantes: {self.rodadas_restantes}"
        )

        self.lbl_linha_jogador.config(bg=COR_BRANCO)
        self.lbl_linha_computador.config(bg=COR_BRANCO)

        for botao in self.botoes_opcoes:
            botao.config(state=tk.NORMAL)

        self.btn_reiniciar.place_forget()