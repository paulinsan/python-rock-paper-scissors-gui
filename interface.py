import random
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

# === MENSAGENS DOS RESULTADOS ===

MENSAGENS_VITORIA = [
    "Mandou bem! Você venceu!",
    "Boa jogada! Ponto para você!",
    "Excelente! Você levou essa!",
    "É isso aí! Mais uma vitória!",
    "Você está jogando muito!"
]

MENSAGENS_DERROTA = [
    "Dessa vez não! O computador venceu.",
    "O computador levou essa!",
    "Quase lá! Tente novamente.",
    "Essa rodada foi do computador!",
    "Não foi dessa vez!"
]

MENSAGENS_EMPATE = [
    "Foi por pouco! Deu empate.",
    "Ninguém levou vantagem!",
    "Vocês pensaram igual!",
    "Uma rodada equilibrada!",
    "Tudo igual por aqui!"
]

# === PALETA DE CORES ===

COR_FUNDO = "#0B1120"
COR_PAINEL = "#151F35"

COR_BOTAO = "#2563EB"
COR_DESTAQUE = "#60A5FA"

COR_BRANCO = "#F8FAFC"
COR_TEXTO_SECUNDARIO = "#94A3B8"

COR_VERDE = "#22C55E"
COR_VERMELHO = "#EF4444"
COR_LARANJA = "#F59E0B"


# === FONTES ===

FONTE_PADRAO = "Segoe UI"

FONTE_PLACAR = (FONTE_PADRAO, 32, "bold")
FONTE_DOIS_PONTOS = (FONTE_PADRAO, 28, "bold")
FONTE_TEXTO = (FONTE_PADRAO, 10)
FONTE_BOTAO = (FONTE_PADRAO, 10, "bold")
FONTE_RESULTADO = (FONTE_PADRAO, 11, "bold")


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

        # Guarda as imagens na memória
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
            bg=COR_PAINEL
        )
        self.frame_cima.pack()

        self.frame_baixo = tk.Frame(
            self.janela,
            width=320,
            height=290,
            bg=COR_PAINEL
        )
        self.frame_baixo.pack()

        # Mantém as dimensões definidas dos frames
        self.frame_cima.pack_propagate(False)
        self.frame_baixo.pack_propagate(False)

    # === PLACAR VISUAL ===

    def criar_placar(self):
        self.lbl_pontos_jogador = tk.Label(
            self.frame_cima,
            text="0",
            font=FONTE_PLACAR,
            bg=COR_PAINEL,
            fg=COR_BRANCO
        )
        self.lbl_pontos_jogador.place(x=65, y=25)

        self.lbl_dois_pontos = tk.Label(
            self.frame_cima,
            text=":",
            font=FONTE_DOIS_PONTOS,
            bg=COR_PAINEL,
            fg=COR_DESTAQUE
        )
        self.lbl_dois_pontos.place(x=150, y=30)

        self.lbl_pontos_computador = tk.Label(
            self.frame_cima,
            text="0",
            font=FONTE_PLACAR,
            bg=COR_PAINEL,
            fg=COR_BRANCO
        )
        self.lbl_pontos_computador.place(x=215, y=25)

        tk.Label(
            self.frame_cima,
            text="Você",
            font=FONTE_TEXTO + ("bold",),
            bg=COR_PAINEL,
            fg=COR_TEXTO_SECUNDARIO
        ).place(x=75, y=85)

        tk.Label(
            self.frame_cima,
            text="Computador",
            font=FONTE_TEXTO + ("bold",),
            bg=COR_PAINEL,
            fg=COR_TEXTO_SECUNDARIO
        ).place(x=190, y=85)

        # Linhas laterais do placar
        self.lbl_linha_jogador = tk.Label(
            self.frame_cima,
            bg=COR_DESTAQUE,
            width=2
        )
        self.lbl_linha_jogador.place(
            x=0, y=0, width=5, height=130
        )

        self.lbl_linha_computador = tk.Label(
            self.frame_cima,
            bg=COR_DESTAQUE,
            width=2
        )
        self.lbl_linha_computador.place(
            x=315, y=0, width=5, height=130
        )

        # Barra inferior: muda de cor ao final da partida
        self.lbl_linha_inferior = tk.Label(
            self.frame_cima,
            bg=COR_DESTAQUE
        )
        self.lbl_linha_inferior.place(
            x=0, y=125, width=320, height=5
        )

    # === ÁREA PRINCIPAL ===

    def criar_area_jogo(self):
        self.lbl_mensagem = tk.Label(
            self.frame_baixo,
            text="Escolha sua jogada!",
            font=FONTE_RESULTADO,
            bg=COR_PAINEL,
            fg=COR_BRANCO
        )
        self.lbl_mensagem.place(
            x=0, y=15, width=320
        )

        self.lbl_escolha_computador = tk.Label(
            self.frame_baixo,
            text="",
            font=FONTE_TEXTO,
            bg=COR_PAINEL,
            fg=COR_TEXTO_SECUNDARIO
        )
        self.lbl_escolha_computador.place(
            x=0, y=42, width=320
        )

        # Área dos botões de escolha
        self.frame_botoes = tk.Frame(
            self.frame_baixo,
            bg=COR_PAINEL
        )
        self.frame_botoes.place(x=28, y=85)

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
                bg=COR_PAINEL,
                activebackground=COR_PAINEL,
                relief=tk.FLAT,
                cursor="hand2",
                borderwidth=0,
                highlightthickness=0
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
            font=FONTE_TEXTO,
            bg=COR_PAINEL,
            fg=COR_TEXTO_SECUNDARIO
        )
        self.lbl_rodadas.place(
            x=0, y=175, width=320
        )

        self.btn_reiniciar = tk.Button(
            self.frame_baixo,
            text="Jogar novamente",
            command=self.reiniciar_jogo,
            width=20,
            bg=COR_BOTAO,
            fg=COR_BRANCO,
            activebackground=COR_DESTAQUE,
            activeforeground=COR_FUNDO,
            font=FONTE_BOTAO,
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

        # Atualiza o placar
        self.lbl_pontos_jogador.config(
            text=self.placar["jogador"]
        )
        self.lbl_pontos_computador.config(
            text=self.placar["computador"]
        )

        # Mostra a escolha do computador
        self.lbl_escolha_computador.config(
            text=f"Computador escolheu: {escolha_computador}"
        )

        self.lbl_rodadas.config(
            text=f"Rodadas restantes: {self.rodadas_restantes}"
        )

        self.atualizar_resultado_visual(resultado)

        # Encerra automaticamente após a última rodada
        if self.rodadas_restantes == 0:
            self.finalizar_jogo()

    # === RESULTADO VISUAL DA RODADA ===

    def atualizar_resultado_visual(self, resultado):
        self.lbl_linha_jogador.config(bg=COR_DESTAQUE)
        self.lbl_linha_computador.config(bg=COR_DESTAQUE)

        if resultado == "jogador":
            mensagem = random.choice(MENSAGENS_VITORIA)

            self.lbl_mensagem.config(
                text=mensagem,
                fg=COR_VERDE
            )

            self.lbl_linha_jogador.config(bg=COR_VERDE)

        elif resultado == "computador":
            mensagem = random.choice(MENSAGENS_DERROTA)

            self.lbl_mensagem.config(
                text=mensagem,
                fg=COR_VERMELHO
            )

            self.lbl_linha_computador.config(bg=COR_VERMELHO)

        else:
            mensagem = random.choice(MENSAGENS_EMPATE)

            self.lbl_mensagem.config(
                text=mensagem,
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

        # Atualiza a barra inferior conforme o resultado final
        self.lbl_linha_inferior.config(bg=cor)

        self.lbl_mensagem.config(
            text=mensagem,
            fg=cor
        )

        self.lbl_rodadas.config(
            text="Partida finalizada!"
        )

        self.btn_reiniciar.place(
            x=75, y=227
        )

    # === REINICIAR PARTIDA ===

    def reiniciar_jogo(self):
        self.placar = criar_placar()
        self.rodadas_restantes = TOTAL_RODADAS

        self.lbl_pontos_jogador.config(text="0")
        self.lbl_pontos_computador.config(text="0")

        self.lbl_mensagem.config(
            text="Escolha sua jogada!",
            fg=COR_BRANCO
        )

        self.lbl_escolha_computador.config(text="")

        self.lbl_rodadas.config(
            text=f"Rodadas restantes: {self.rodadas_restantes}"
        )

        # Restaura as cores neutras
        self.lbl_linha_jogador.config(bg=COR_DESTAQUE)
        self.lbl_linha_computador.config(bg=COR_DESTAQUE)
        self.lbl_linha_inferior.config(bg=COR_DESTAQUE)

        for botao in self.botoes_opcoes:
            botao.config(state=tk.NORMAL)

        self.btn_reiniciar.place_forget()
