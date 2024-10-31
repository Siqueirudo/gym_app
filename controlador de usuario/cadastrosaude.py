import sys
from tkinter import *
from tkinter import messagebox
import subprocess
import database

# Pegar o argumento do nome de usuário
username = sys.argv[1] if len(sys.argv) > 1 else "Usuário desconhecido"

# Criar a janela
janela = Tk()
janela.title("Painel de acesso")
janela.geometry("800x600")
janela.configure(background="white")
janela.resizable(width=False, height=False)
janela.attributes("-alpha", 0.9)
janela.iconbitmap(default="icone.ico")

logo = PhotoImage(file="logocsf.png")
leftframe = Frame(janela, width=305, height=600, bg="MIDNIGHTBLUE", relief="raise")
leftframe.pack(side=LEFT)
leftframe = Frame(janela, width=490, height=600, bg="MIDNIGHTBLUE", relief="raise")
leftframe.pack(side=RIGHT)
logolabel = Label(janela, image=logo, bg="MIDNIGHTBLUE")
logolabel.place(x=25, y=200)

# Função para sair
def sair():
    janela.destroy()
    subprocess.Popen(["python", "controladordeusuario.py"])

botaosair = Button(janela, text="Sair", width=20, command=sair)
botaosair.place(x=320, y=20)

# Exibir o nome do usuário logado
nomelabel = Label(janela, text=username, font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white")
nomelabel.place(x=780, y=30, anchor="e")

bemvindolabel = Label(janela, text="Bem Vindo a forjafit",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
bemvindolabel.place(x=420,y=100)

pedidolabel = Label(janela,text="antes de continuar precisamos das seguintes informaçoes",font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white")
pedidolabel.place(x=330,y=150)

pesolabel = Label(janela,text="peso(kg):",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
pesolabel.place(x=400,y=200)
pesoentry = Entry(janela,width=33)
pesoentry.place(x=530,y=214)
alturalabel= Label(janela,text="altura(cm):",font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
alturalabel.place(x=400,y=300)
alturaentry = Entry(janela,width=30)
alturaentry.place(x=550,y=314)

def enviar():
    peso = pesoentry.get()
    altura =alturaentry.get()

    if peso == "" or altura == "":
        messagebox.showerror(title="erro de cadastro", message="por favor nao deixe campos em branco")
    else:
        database.cursor.execute("""
         UPDATE USUARIO SET Peso = ?, Altura = ? WHERE Login = ?
        """, (peso, altura, username))
        database.conn.commit()
        messagebox.showinfo(title="info registro", message="Conta criada!")
        janela.destroy()  # Fechar a janela de login
        subprocess.Popen(["python", "testelogindireto.py",peso,altura,username])

botaotreino = Button(janela, text="enviar", width=20, command=enviar)
botaotreino.place(x=600, y=500)

janela.mainloop()
