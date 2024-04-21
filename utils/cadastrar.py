import sqlite3

class Cadastro:
    def __init__(self):
        self.conn = sqlite3.connect('usuarios.db')
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS usuario (id INTEGER PRIMARY KEY AUTOINCREMENT, usuario TEXT NOT NULL, senha TEXT NOT NULL)")
        self.conn.commit()
     

    def cadastroPessoa(self, usuario, senha):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO usuario (usuario, senha) VALUES (?, ?)", (usuario, senha))
        self.conn.commit()