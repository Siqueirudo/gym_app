#importar bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import database
import subprocess


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
#posiçao
userlabel.place(x=400, y=200)
#entry de login
userentry = Entry(janela, width=37)
#posiçao
userentry.place(x=480, y=214)

#label de senha
senhalabel = Label(janela, text="Senha:", font=("Century Gothic",20),bg="MIDNIGHTBLUE", fg="white" )
#posiçao
senhalabel.place(x=397, y=350)
#entry da senha
senhaentry = Entry(janela, width=35, show="*")
#posiçao
senhaentry.place(x=490, y=364)

#def para contruir a funçao de login 
def login():
    #pegar informaçao escrita na entry de login
    login1 = userentry.get()
    #pegar informaçao escrita na entry de senha
    senha1 = senhaentry.get()
    
    #executar comandos em sql
    database.cursor.execute("""
    SELECT * FROM USUARIO 
     WHERE Login = ? AND Senha = ? 
    """, (login1,senha1)) 
    verificarlogin = database.cursor.fetchone() #verificar se a entry de login e senha esta no bd
    try: # tentar executar o codigo
        # se verificar login estiver igual login 1 e senha 1 
        if (login1 in verificarlogin and senha1 in verificarlogin): 
            #mostrar na tela acesso confirmado
            messagebox.showinfo(title="login info",message="acesso confirmado. Bem Vindo!") 
            janela.destroy()  # Fechar a janela de login
            subprocess.Popen(["python","testelogindireto.py",login1])

    # se der erro
    except:  
        #mostrar na tela acesso negado 
        messagebox.showerror(title="login info", message="Acesso Negado.")

#botao de login
botaolabel = Button(janela,text='Login',width=20, command=login)
#posiçao
botaolabel.place(x=580,y=500)

#funçao criada para quando apertar no no batao register da tela inicial
def register():
    #removendo botao
    botaolabel.place(x=1000000)
    registrarlabel.place(x=100000)
    
    
    #adicionando label
    nomelabel = Label(janela, text="Nome:", font=("Century Gothic",20),bg="MIDNIGHTBLUE", fg="white")
    nomelabel.place(x=400,y=80)
    nomeentry = Entry(janela, width=35)
    nomeentry.place(x=500, y=95)

    celularlabel = Label(janela, text="Celular:", font=("Century Gothic",20),bg="MIDNIGHTBLUE", fg="white")
    celularlabel.place(x=400,y=170)
    celularentry = Entry(janela,width=33)
    celularentry.place(x=505, y=184)

    
    userlabel.place(x=400, y=260)
    userentry.place(x=485, y=274)

    #funçao criada para salvar do bd as informaçoes
    def registertodb():
        #pegar informaçao escrita na entry de nome
        nome = nomeentry.get()
        #pegar informaçao escrita na entry de celular
        celular = celularentry.get()
        #pegar informaçao escrita na entry de login
        login = userentry.get()
        #pegar informaçao escrita na entry de senha
        senha = senhaentry.get() 
        
        #se nome.celular,login ou senha estiver vazio 
        if (nome == "" or celular == "" or login == "" or senha == ""):
            #exibir mensagem de erro
            messagebox.showerror(title="register erro", message="Não deixe campos em branco")
        else:  # se nao
            #inserir informaçoes no bd na ordem
            database.cursor.execute("""
            INSERT INTO USUARIO(Nome,Celular,Login,Senha) VALUES(?, ?, ?, ?)
            """, (nome, celular, login, senha))
            database.conn.commit() #atualizar as informaçoes no bd
            #mostrar a mensagem que a conta foi criada
            messagebox.showinfo(title="info registro", message="Conta criada!")
            janela.destroy()  # Fechar a janela de login
            subprocess.Popen(["python", "teste.py",login]) 
            
    #botao para registrar as informaçoes no bd
    registrarlabel1 = Button(janela,text='Registrar',width=20, command= registertodb)
    #posiçao
    registrarlabel1.place(x=600,y=500)

    
    #funçao para o botao voltar caso clique sem querer em register ter a opçao de voltar
    def voltar():
        nomelabel.place(x=50000)
        nomeentry.place(x=50000)
        celularlabel.place(x=500000)
        celularentry.place(x=500000)
        registrarlabel1.place(x=500000)
        backlabel.place(x=500000)
        userlabel.place(x=400, y=200)
        userentry.place(x=480, y=214)
        botaolabel.place(x=580,y=500)
        registrarlabel.place(x=400,y=500)
        

    #botao voltar para posibilidade acima
    backlabel = Button(janela,text='voltar',width=20,command=voltar)
    backlabel.place(x=400,y=500)
    #senhaentry.place(x=100000)

    

    

    
    


registrarlabel = Button(janela,text='Registrar',width=20,command=register)
registrarlabel.place(x=400,y=500)


janela.mainloop()
