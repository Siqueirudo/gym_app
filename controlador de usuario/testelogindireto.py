import sqlite3
from tkinter import *
from tkinter import messagebox
import subprocess
import sys
import database

# Pegar o argumento do nome de usuário


username = sys.argv[3] if len(sys.argv) > 3 else "Usuário desconhecido"

# Função para obter peso e altura do banco de dados
def obter_dados_usuario(username):
    try:
        conn = sqlite3.connect('users.db')  # Substitua 'users.db' pelo caminho do seu banco
        cursor = conn.cursor()
        cursor.execute("SELECT Peso, Altura FROM USUARIO WHERE Login = ?", (username,))
        dados = cursor.fetchone()
        conn.close()
        return dados if dados else ("peso desconhecido", "altura desconhecida")
    except sqlite3.Error as e:
        messagebox.showerror("Erro de Banco de Dados", f"Erro ao acessar o banco de dados: {e}")
        return "peso desconhecido", "altura desconhecida"

# Obter peso e altura do banco se não estiverem nos argumentos
peso, altura = obter_dados_usuario(username)

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
#label de login
userlabel = Label(janela, text="Login:", font=("Century Gothic",20),bg="MIDNIGHTBLUE", fg="white" )
# Exibir o nome do usuário logado
nomelabel = Label(janela, text=username, font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white")
nomelabel.place(x=780, y=30, anchor="e")

# Exibir peso e altura
pesolabel = Label(janela, text="Peso (kg):", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
pesolabel.place(x=350, y=100)
pesouserlabel = Label(janela, text=peso, font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
pesouserlabel.place(x=475, y=100)

alturalabel = Label(janela, text="Altura (m):", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
alturalabel.place(x=350, y=200)
alturauserlabel = Label(janela, text=altura, font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
alturauserlabel.place(x=500, y=200)
imclabel = Label(janela, text="IMC:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
imclabel.place(x=350, y=300)


# Cálculo do IMC
try:
    imccalculo = float(peso) / (float(altura) ** 2)
    imcuserlabel = Label(janela, text=f"{imccalculo:.2f}", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    imcuserlabel.place(x=350, y=300)

    # Exibir situação de acordo com o IMC
    if imccalculo < 16.9:
        situaçaolabel = Label(janela, text="Muito Abaixo Do Peso", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=420, y=400)
    elif imccalculo >= 17 and imccalculo <= 18.4:
        situaçaolabel = Label(janela, text="Abaixo Do Peso", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=400, y=400)
    elif imccalculo >= 18.5 and imccalculo <= 24.9:
        situaçaolabel = Label(janela, text="Peso normal", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=400, y=400)
    elif imccalculo >= 25 and imccalculo <= 29.9:
        situaçaolabel = Label(janela, text="Acima Do Peso", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=400, y=400)
    elif imccalculo >= 30 and imccalculo <= 34.9:
        situaçaolabel = Label(janela, text="Obesidade Grau I", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=400, y=400)
    elif imccalculo >= 35 and imccalculo <= 40:
        situaçaolabel = Label(janela, text="Obesidade Grau II", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=400, y=400)
    elif imccalculo > 40:
        situaçaolabel = Label(janela, text="Obesidade Grau III", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
        situaçaolabel.place(x=400, y=400)
except:
    imcuserlabel = Label(janela, text="dados invalidos", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
    imcuserlabel.place(x=420, y=300)

# Função de sair
def sair():
    janela.destroy()
    subprocess.Popen(["python", "controladordeusuario.py"])

# Botão Sair
botaosair = Button(janela, text="Sair", width=20, command=sair)
botaosair.place(x=320, y=20)

janela.mainloop()
