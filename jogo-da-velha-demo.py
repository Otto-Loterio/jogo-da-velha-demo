import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()

janela.title("Seja bem vindo ao meu programa!")
janela.geometry("500x500")

frame1 = tk.Frame(janela)
frame1.pack(expand=True, fill="both")

botao1 = tk.Button(frame1, text="POS 1", command=lambda: aoClique())
botao1.pack(side="left", expand=True, fill="both")
botao2 = tk.Button(frame1, text="POS 2", command=lambda: aoClique())
botao2.pack(side="left", expand=True, fill="both")
botao3 = tk.Button(frame1, text="POS 3", command=lambda: aoClique())
botao3.pack(side="left", expand=True, fill="both")

frame2 = tk.Frame(janela)
frame2.pack(expand=True, fill="both")

botao4 = tk.Button(frame2,text="POS 4", command=lambda: aoClique())
botao4.pack(side="left", expand=True, fill="both")
botao5 = tk.Button(frame2,text="POS 5", command=lambda: aoClique())
botao5.pack(side="left", expand=True, fill="both")
botao6 = tk.Button(frame2,text="POS 6", command=lambda: aoClique())
botao6.pack(side="left", expand=True, fill="both")

frame3 = tk.Frame(janela)
frame3.pack(expand=True, fill="both")

botao7 = tk.Button(frame3,text="POS 7", command=lambda: aoClique())
botao7.pack(side="left",expand=True, fill="both")
botao8 = tk.Button(frame3,text="POS 8", command=lambda: aoClique())
botao8.pack(side="left",expand=True, fill="both")
botao9 = tk.Button(frame3,text="POS 9", command=lambda: aoClique())
botao9.pack(side="left",expand=True, fill="both")

def aoClique():
    messagebox.showinfo("AVISO!!", "Em desenvolvimento!!")

janela.mainloop()