import sqlite3
import random
import math
import sys


def inicializar_banco():
    try:
        conn = sqlite3.connect('biblioteca.db')
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS aluno (
            ra INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(100) NOT NULL,
            senha VARCHAR(100) NOT NULL,
            saldo_devedor DECIMAL(10,2) NOT NULL DEFAULT 0.00)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo VARCHAR(100) NOT NULL,
            autor VARCHAR(100) NOT NULL,
            area VARCHAR(50) NOT NULL,
            situacao TEXT NOT NULL DEFAULT 'Disponivel')''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS emprestimo (
            id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
            ra_aluno INT NOT NULL,
            id_livro INT NOT NULL,
            FOREIGN KEY (ra_aluno) REFERENCES aluno (ra) ON DELETE CASCADE,
            FOREIGN KEY (id_livro) REFERENCES livros (id) ON DELETE CASCADE)''')

        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Erro ao inicializar banco: {e}")
        sys.exit()


def conectar():
    return sqlite3.connect('biblioteca.db')


def login():
    print("\n--- LOGIN DE USUARIO ---")
    try:
        ra = int(input("RA: "))
        senha = input("Senha: ")
        
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM aluno WHERE ra = ? AND senha = ?", (ra, senha))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return user
        else:
            print("Erro: Credenciais invalidas.")
            return None
    except ValueError:
        print("Erro: O RA deve ser numerico.")
        return None

def consultar_acervo():
    print("\n--- CONSULTA DE ACERVO ---")
    print("Filtros: [1] Titulo | [2] Autor | [3] Area")
    op = input("Opcao: ")
    
    colunas = {"1": "titulo", "2": "autor", "3": "area"}
    campo = colunas.get(op, "titulo")
    termo = input(f"Buscar {campo}: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM livros WHERE {campo} LIKE ?", (f'%{termo}%',))
    resultados = cursor.fetchall()
    conn.close()

    if resultados:
        print(f"\n{'ID':<4} | {'TITULO':<25} | {'SITUACAO':<12}")
        print("-" * 50)
        for livro in resultados:
            print(f"{livro[0]:<4} | {livro[1]:<25} | {livro[4]:<12}")
    else:
        print("Nenhum livro encontrado.")

def realizar_emprestimo(ra_aluno):
    try:
        print("\n--- REALIZAR EMPRESTIMO ---")
        id_livro = int(input("ID do livro: "))
        
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("SELECT titulo, situacao FROM livros WHERE id = ?", (id_livro,))
        livro = cursor.fetchone()

        if livro and livro[1] == 'Disponivel':
            cursor.execute("UPDATE livros SET situacao = 'Emprestado' WHERE id = ?", (id_livro,))
            cursor.execute("INSERT INTO emprestimo (ra_aluno, id_livro) VALUES (?, ?)", (ra_aluno, id_livro))
            protocolo = random.randint(1000, 9999)
            conn.commit()
            print(f"Sucesso! Protocolo: {protocolo}")
        else:
            print("Erro: Livro inexistente ou ja emprestado.")
        conn.close()
    except ValueError:
        print("Erro: ID invalido.")

def devolver_livro(ra_aluno):
    try:
        print("\n--- DEVOLUCAO ---")
        id_livro = int(input("ID do livro: "))
        dias = int(input("Dias de atraso (0 para pontual): "))
        
        conn = conectar()
        cursor = conn.cursor()

        if dias > 0:
            multa = math.ceil(dias * 2.50)
            cursor.execute("UPDATE aluno SET saldo_devedor = saldo_devedor + ? WHERE ra = ?", (multa, ra_aluno))
            print(f"Multa registrada: R$ {multa:.2f}")

        cursor.execute("UPDATE livros SET situacao = 'Disponivel' WHERE id = ?", (id_livro,))
        cursor.execute("DELETE FROM emprestimo WHERE id_livro = ? AND ra_aluno = ?", (id_livro, ra_aluno))
        conn.commit()
        conn.close()
        print("Devolucao concluida.")
    except Exception as e:
        print(f"Erro no processo: {e}")

def pagar_multa(ra_aluno):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT saldo_devedor FROM aluno WHERE ra = ?", (ra_aluno,))
    saldo = cursor.fetchone()[0]
    
    print(f"\nSua divida atual: R$ {saldo:.2f}")
    if saldo > 0:
        if input("Deseja quitar agora? (s/n): ").lower() == 's':
            cursor.execute("UPDATE aluno SET saldo_devedor = 0 WHERE ra = ?", (ra_aluno,))
            conn.commit()
            print("Debito zerado.")
    conn.close()


if __name__ == "__main__":
    inicializar_banco()
    
    while True:
        usuario = login()
        if usuario:
            while True:
                print(f"\nMENU - {usuario[1].upper()}")
                print("1. Consulta | 2. Emprestimo | 3. Devolucao | 4. Multa | 5. Sair")
                op = input("Opcao: ")
                
                if op == "1": consultar_acervo()
                elif op == "2": realizar_emprestimo(usuario[0])
                elif op == "3": devolver_livro(usuario[0])
                elif op == "4": pagar_multa(usuario[0])
                elif op == "5": break
                else: print("Opcao invalida.")
        
        if input("\nEncerrar aplicacao? (s/n): ").lower() == 's':
            break