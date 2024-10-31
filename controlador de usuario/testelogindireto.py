from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database
import subprocess
import sys

# Pegar o argumento do nome de usuário
peso = sys.argv[1] if len(sys.argv) > 1 else "peso desconhecido"
altura =sys.argv[2] if len(sys.argv) > 2 else "altura desconhecido"
username = sys.argv[3] if len(sys.argv) > 3 else "Usuário desconhecido"


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
pesolabel.place(x=350,y=100)

pesouserlabel = Label(janela,text=peso,font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
pesouserlabel.place(x=475,y=100)

alturalabel= Label(janela,text="altura(cm):",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
alturalabel.place(x=350,y=200)

alturauserlabel= Label(janela,text=altura,font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
alturauserlabel.place(x=500,y=200)

imclabel= Label(janela,text="IMC:",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
imclabel.place(x=350,y=300)
try:
    imccalculo = float(peso) / (float(altura) ** 2)
    imcuserlabel= Label(janela,text=f"{imccalculo:.2f}",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    imcuserlabel.place(x=350,y=300)

    if imccalculo < 16.9:
        situaçaolabel = Label(janela,text="Muito Abaixo Do Peso",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=420,y=400)
    elif imccalculo >= 17 and imccalculo <= 18.4:
        situaçaolabel = Label(janela,text="Abaixo Do Peso",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=400,y=400)
    elif imccalculo >= 18.5 and imccalculo <= 24.9:
        situaçaolabel = Label(janela,text="Peso normal",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=400,y=400)
    elif imccalculo >= 25 and imccalculo <= 29.9:
        situaçaolabel = Label(janela,text="Acima Do Peso",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=400,y=400)
    elif imccalculo >= 30 and imccalculo <= 34.9:
        situaçaolabel = Label(janela,text="Obesidade Grau I",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=400,y=400)
    elif imccalculo >= 35 and imccalculo <= 40:
        situaçaolabel = Label(janela,text="Obesidade Grau II",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=400,y=400)
    elif imccalculo > 25:
        situaçaolabel = Label(janela,text="Obesidade Grau III",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=400,y=400)
except:
    imccalculo = "Dados inválidos"

    imcuserlabel= Label(janela,text=imccalculo,font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    imcuserlabel.place(x=420,y=300)

def treino():
    janela.destroy()  # Fechar a janela de login
    subprocess.Popen(["python", "treino.py"])


botaotreino = Button(janela, text="Treino", width=20, command=treino)
botaotreino.place(x=400, y=500)

janela.mainloop()