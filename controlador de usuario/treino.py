from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database
import subprocess
import sys


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

#nome de usuario
nomelabel = Label(janela, text=username, font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white")
nomelabel.place(x=780, y=30, anchor="e")

#funçapsair
def sair():
    janela.destroy()
    subprocess.Popen(["python", "testelogindireto.py",username,username,username])

# Botão Sair
botaosair = Button(janela, text="Sair", width=20, command=sair)
botaosair.place(x=320, y=20)

#funçaotreino1

def treino1():
    janela.destroy()
    subprocess.Popen(["python", "treino1.py",username])

#treino1

botaotreino = Button(janela, text="triceps e peito", width=20, command=treino1)
botaotreino.place(x=450, y=200)

#funçaotreino2

def treino2():
    janela.destroy()
    subprocess.Popen(["python", "treino2.py",username])



#treino2

botaotreino1 = Button(janela, text="biceps e costas", width=20, command=treino2)
botaotreino1.place(x=450, y=300)

#funçaotreino3

def treino3():
    janela.destroy()
    subprocess.Popen(["python", "treino3.py",username])


#treino3

botaotreino2 = Button(janela, text="perna", width=20, command=treino3)
botaotreino2.place(x=450, y=400)


janela.mainloop()