import sqlite3

class Login:
    def __init__(self):
        self.conn = sqlite3.connect('usuarios.db')
        self.cursor = self.conn.cursor()

    def validar_login(self, usuario, senha):
        consulta = "SELECT * FROM usuario WHERE usuario = ? AND senha = ?"
        self.cursor.execute(consulta, (usuario, senha))
        resultado = self.cursor.fetchone()

        if resultado:
            print("Login válido")
            return True
        else:
            print("Usuário ou senha incorretos")
            return False


