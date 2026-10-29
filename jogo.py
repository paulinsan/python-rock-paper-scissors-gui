import random


OPCOES = ["Pedra", "Papel", "Tesoura"]


def escolher_computador():
    """Retorna uma escolha aleatória para o computador."""
    return random.choice(OPCOES)


def verificar_vencedor(jogador, computador):
    """Compara as escolhas e retorna o resultado da rodada."""

    if jogador == computador:
        return "empate"

    elif jogador == "Pedra" and computador == "Tesoura":
        return "jogador"

    elif jogador == "Papel" and computador == "Pedra":
        return "jogador"

    elif jogador == "Tesoura" and computador == "Papel":
        return "jogador"

    else:
        return "computador"


def criar_placar():
    """Cria e retorna um placar zerado."""
    return {
        "jogador": 0,
        "computador": 0,
        "empates": 0,
        "rodadas": 0
    }


def atualizar_placar(placar, resultado):
    """Atualiza o placar de acordo com o resultado da rodada."""

    placar["rodadas"] += 1

    if resultado == "jogador":
        placar["jogador"] += 10

    elif resultado == "computador":
        placar["computador"] += 10

    else:
        placar["empates"] += 1