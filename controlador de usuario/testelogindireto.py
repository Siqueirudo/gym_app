from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database
import subprocess
import sys

# Pegar o argumento do nome de usuário
username = sys.argv[1] if len(sys.argv) > 1 else "Usuário desconhecido"


#criar nossa janela
janela = Tk()
#titulo da janela
janela.title("Painel de acesso")
#tamanho da janela
janela.geometry("800x600")
#fundo branco
janela.configure(background="white")
#tirar a opçao de mudar o tamanho da janela
janela.resizable(width=False, height=False)
#transparencia da janela
janela.attributes("-alpha",0.9)
#icone da janela
janela.iconbitmap(default="icone.ico")

#logo na label esquerda
logo = PhotoImage(file="logocsf.png")

#widgets
#frameazul da esquerda
leftframe = Frame(janela, width=305,height=600,bg="MIDNIGHTBLUE", relief="raise")
#posiçao da frame
leftframe.pack(side=LEFT)

#frameazuldireita
leftframe = Frame(janela, width=490,height=600,bg="MIDNIGHTBLUE", relief="raise")
#posiçao da frame
leftframe.pack(side=RIGHT)
#a logo
logolabel = Label(janela, image=logo,bg="MIDNIGHTBLUE")
#posiçao
logolabel.place(x=25, y=200)

def sair():
    janela.destroy()
    subprocess.Popen(["python", "controladordeusuario.py"])

botaosair = Button(janela, text="Sair", width=20, command=sair)
botaosair.place(x=320, y=20)

# Exibir o nome do usuário logado
nomelabel = Label(janela, text=username, font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white")
nomelabel.place(x=780, y=30, anchor="e")

pesolabel = Label(janela,text="peso(kg):",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
pesolabel.place(x=400,y=200)

alturalabel= Label(janela,text="altura(cm):",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
alturalabel.place(x=400,y=300)

imclabel= Label(janela,text="IMC:",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
imclabel.place(x=400,y=400)

botaotreino = Button(janela, text="Treino", width=20, command=sair)
botaotreino.place(x=400, y=500)

janela.mainloop()