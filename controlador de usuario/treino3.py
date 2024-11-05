from tkinter import *
from tkinter import messagebox
import subprocess
import sys

username = sys.argv[1] if len(sys.argv) > 1 else "Usuário desconhecido"

# Lista de exercícios com séries e repetições
treino_triceps_peito = [
    {"exercicio": "HACK", "series": "3x12", "carga": 20},
    {"exercicio": "Leg Press", "series": "3x10", "carga": 15},
    {"exercicio": "Cadeira Extensora", "series": "4x12", "carga": 12},
    {"exercicio": "Mesa Flexora", "series": "3x12", "carga": 10}
]

# Função para salvar as cargas editadas
def salvar_cargas():
    for i, entry in enumerate(carga_entries):
        try:
            carga = int(entry.get())  # Verifica se é um número
            treino_triceps_peito[i]["carga"] = carga
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um valor numérico para a carga.")
            return
    messagebox.showinfo("Sucesso", "Cargas salvas com sucesso!")

# Função para sair
def sair():
    janela.destroy()
    subprocess.Popen(["python", "treino.py",username])

# Criar a janela principal
janela = Tk()
janela.title("Painel de Acesso")
janela.geometry("800x600")
janela.configure(background="white")
janela.resizable(width=False, height=False)
janela.attributes("-alpha", 0.9)
janela.iconbitmap(default="icone.ico")

# Frames laterais
leftframe = Frame(janela, width=305, height=600, bg="MIDNIGHTBLUE", relief="raise")
leftframe.pack(side=LEFT)
rightframe = Frame(janela, width=490, height=600, bg="MIDNIGHTBLUE", relief="raise")
rightframe.pack(side=RIGHT)

# Logo
logo = PhotoImage(file="logocsf.png")
logolabel = Label(janela, image=logo, bg="MIDNIGHTBLUE")
logolabel.place(x=25, y=200)

# Nome do usuário
nomelabel = Label(janela, text=username, font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white")
nomelabel.place(x=780, y=30, anchor="e")

# Botão Sair
botaosair = Button(janela, text="Sair", width=10, command=sair)
botaosair.place(x=320, y=20)

# Título dos Exercícios
titulo = Label(rightframe, text="Perna", font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white")
titulo.place(x=200, y=20)

# Cabeçalhos da tabela
Label(rightframe, text="Exercício", font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white").place(x=20, y=80)
Label(rightframe, text="Séries x Repetições", font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white").place(x=150, y=80)
Label(rightframe, text="Carga (kg)", font=("Century Gothic", 12), bg="MIDNIGHTBLUE", fg="white").place(x=350, y=80)

# Campos para os exercícios
carga_entries = []
y_position = 120

for treino in treino_triceps_peito:
    # Nome do exercício e séries
    Label(rightframe, text=treino["exercicio"], font=("Century Gothic", 10), bg="MIDNIGHTBLUE", fg="white").place(x=20, y=y_position)
    Label(rightframe, text=treino["series"], font=("Century Gothic", 10), bg="MIDNIGHTBLUE", fg="white").place(x=180, y=y_position)
    
    # Entrada de carga
    carga_entry = Entry(rightframe, font=("Century Gothic", 10), width=5)
    carga_entry.insert(0, treino["carga"])
    carga_entry.place(x=370, y=y_position)
    carga_entries.append(carga_entry)
    
    y_position += 40

# Botão para salvar as cargas
botao_salvar = Button(rightframe, text="Salvar Cargas", font=("Century Gothic", 10), command=salvar_cargas)
botao_salvar.place(x=350, y=y_position + 20)

janela.mainloop()
