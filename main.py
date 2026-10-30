import tkinter as tk
from interface import InterfaceJogo

def main():
    janela = tk.Tk()

    InterfaceJogo(janela)

    janela.mainloop()

if __name__ == "__main__":
    main()