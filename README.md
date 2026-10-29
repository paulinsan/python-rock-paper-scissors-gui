# ✂️ Pedra, Papel ou Tesoura — GUI

**Status do projeto:** 🟡 **Em desenvolvimento**

## 📖 Sobre o projeto

Este projeto consiste em uma versão gráfica do clássico jogo **Pedra, Papel ou Tesoura**, desenvolvido em Python utilizando a biblioteca Tkinter.

O objetivo é praticar conceitos de programação, organização de código, criação de interfaces gráficas e separação de responsabilidades entre arquivos.

O projeto está sendo reorganizado para tornar o código mais legível, modular e fácil de manter.

## 🎮 Funcionalidades

- Interface gráfica desenvolvida com Tkinter.
- Botões com imagens para representar Pedra, Papel e Tesoura.
- Escolha aleatória do computador.
- Sistema de partidas com 5 rodadas.
- Placar para o jogador e o computador.
- Sistema de pontuação, com 10 pontos por vitória.
- Contabilização de empates.
- Indicação visual do resultado de cada rodada.
- Exibição da escolha do computador.
- Identificação do vencedor da partida.
- Opção para reiniciar o jogo e zerar o placar.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem de programação.
- **Tkinter:** criação da interface gráfica.
- **Pillow:** carregamento e redimensionamento das imagens.
- **Git e GitHub:** versionamento e armazenamento do projeto.

## 📂 Estrutura de arquivos

```text
pedra-papel-tesoura-gui/
│
├── main.py
├── jogo.py
├── interface.py
│
├── imagens/
│   ├── pedra.png
│   ├── papel.png
│   └── tesoura.png
│
├── README.md
└── requirements.txt
```

### 📄 Responsabilidade dos arquivos

| Arquivo | Descrição |
|---|---|
| `main.py` | Inicializa a aplicação e abre a janela principal. |
| `jogo.py` | Contém as regras, a escolha do computador e o gerenciamento do placar. |
| `interface.py` | Organiza a janela, os botões, as imagens, as mensagens e os elementos visuais. |
| `imagens/` | Armazena as imagens utilizadas nos botões do jogo. |
| `requirements.txt` | Lista as dependências externas necessárias para executar o projeto. |

## ⚙️ Como executar o projeto

### 1. Pré-requisitos

Certifique-se de ter o Python instalado no computador.

### 2. Clone o repositório

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Substitua `URL_DO_SEU_REPOSITORIO` pelo endereço real do repositório no GitHub.

### 3. Entre na pasta do projeto

```bash
cd pedra-papel-tesoura-gui
```

### 4. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 5. Execute o jogo

```bash
python main.py
```

## 📌 Regras do jogo

- O jogador escolhe entre Pedra, Papel e Tesoura.
- O computador realiza uma escolha aleatória.
- Pedra vence Tesoura.
- Tesoura vence Papel.
- Papel vence Pedra.
- Escolhas iguais resultam em empate.
- Cada vitória vale 10 pontos.
- Os empates são contabilizados separadamente e não adicionam pontos.
- A partida termina após 5 rodadas.
- Ao final, o jogo informa se o jogador venceu, perdeu ou empatou.
- É possível iniciar uma nova partida e zerar a pontuação.

## 📚 Conceitos praticados

- Variáveis e estruturas de dados.
- Dicionários para armazenar o placar.
- Funções e métodos.
- Condicionais (`if`, `elif` e `else`).
- Listas e escolha aleatória com `random`.
- Programação orientada a objetos com classes.
- Organização de código em módulos.
- Importação de funções e classes entre arquivos.
- Criação e manipulação de widgets com Tkinter.
- Manipulação de imagens com Pillow.
- Atualização dinâmica de elementos da interface.

## 🚧 Melhorias futuras

- [ ] Revisar e testar todas as funcionalidades após a reorganização dos arquivos.
- [ ] Melhorar o layout e a experiência visual da interface.
- [ ] Implementar tratamento de erros para arquivos de imagem ausentes.
- [ ] Melhorar as mensagens e os indicadores de resultado.
- [ ] Revisar a organização e a legibilidade do código.
- [ ] Realizar testes da lógica de vitória, derrota e empate.

## 👨‍💻 Autor

**Paulo Henrique dos Santos**

Projeto desenvolvido com fins educacionais durante meus estudos de programação e desenvolvimento de software.

---

*Este projeto continua em desenvolvimento e poderá receber novas funcionalidades, correções e melhorias conforme minha evolução nos estudos.*