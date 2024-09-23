import sqlite3
from pathlib import Path
from tabulate import tabulate


# Caminho do banco de dados
db_dir = Path("data")
db_dir.mkdir(parents=True, exist_ok=True)  # Garante que o diretório "data" exista
db_path = db_dir / "livraria.db"  # Define o caminho completo para o banco de dados

# Conectando ao banco de dados
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Criando tabela de livros se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano_publicacao INTEGER NOT NULL,
        preco REAL NOT NULL
    )
''')
conn.commit()

def adicionar_livro(titulo, autor, ano, preco):
    # Verifica se o livro já existe no banco de dados
    cursor.execute("SELECT * FROM livros WHERE titulo = ? AND autor = ? AND ano_publicacao = ? AND preco = ?",
                   (titulo, autor, ano, preco))
    if cursor.fetchone() is None:
        # Se o livro não existe, insere no banco
        cursor.execute("INSERT INTO livros (titulo, autor, ano_publicacao, preco) VALUES (?, ?, ?, ?)",
                       (titulo, autor, ano, preco))
        conn.commit()
        print(f"Livro '{titulo}' adicionado com sucesso!")
    else:
        print(f"O livro '{titulo}' já existe no banco de dados.")

def exibir_livros(retornar_lista=False):
    try:
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        if livros:
            # Exibe os livros na tela formatados
            print(tabulate(livros, headers=["ID", "Título", "Autor", "Ano de Publicação", "Preço"], tablefmt="fancy_grid"))
        else:
            print("Nenhum livro encontrado.")
        
        # Retorna a lista de livros, seja ela vazia ou com dados
        return livros if retornar_lista else []
    except sqlite3.Error as e:
        print(f"Erro ao exibir livros: {e}")
        return []



def atualizar_preco_livro(livro_id, novo_preco):
    try:
        cursor.execute("UPDATE livros SET preco = ? WHERE id = ?", (novo_preco, livro_id))
        conn.commit()
        if cursor.rowcount == 0:
            print("Nenhum livro encontrado com esse ID.")
        else:
            print("Preço atualizado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar o preço do livro: {e}")

def remover_livro(livro_id):
    try:
        cursor.execute("DELETE FROM livros WHERE id = ?", (livro_id,))
        conn.commit()
        if cursor.rowcount == 0:
            print("Nenhum livro encontrado com esse ID.")
        else:
            print("Livro removido com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao remover o livro: {e}")

def buscar_livros_por_autor(autor):
    try:
        cursor.execute("SELECT * FROM livros WHERE autor = ?", (autor,))
        livros = cursor.fetchall()
        if livros:
            print(tabulate(livros, headers=["ID", "Título", "Autor", "Ano de Publicação", "Preço"], tablefmt="fancy_grid"))
        else:
            print("Nenhum livro encontrado para o autor especificado.")
    except sqlite3.Error as e:
        print(f"Erro ao buscar livros por autor: {e}")

# Fechar a conexão com o banco de dados
def fechar_conexao():
    conn.close()
