import sqlite3 

conn = sqlite3.connect('users.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS USUARIO (
   ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
   Nome TEXT NOT NULL,
   Celular TEXT NOT NULL,
   Login TEXT NOT NULL,
   Senha TEXT NOT NULL                            
);

""")

print("conectado ao Banco de dados")

