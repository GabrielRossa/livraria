from database import *
from file_manager import *
import os

def menu():
    while True:
        print("""
        1. Adicionar novo livro
        2. Exibir todos os livros
        3. Atualizar preço de um livro
        4. Remover um livro
        5. Buscar livros por autor
        6. Exportar dados para CSV
        7. Importar dados de CSV
        8. Fazer backup do banco de dados
        9. Sair
        """)
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Título do livro: ")
            autor = input("Autor: ")

            while True:
                try:
                    ano = int(input("Ano de publicação: "))
                    if ano > 0:
                        break
                    else:
                        print("O ano deve ser um valor positivo.")
                except ValueError:
                    print("Por favor, insira um ano válido.")

            while True:
                try:
                    preco = float(input("Preço: "))
                    if preco > 0:
                        break
                    else:
                        print("O preço deve ser um valor positivo.")
                except ValueError:
                    print("Por favor, insira um preço válido.")

            adicionar_livro(titulo, autor, ano, preco)
            fazer_backup()
        
        elif opcao == '2':
            exibir_livros()
        
        elif opcao == '3':
            try:
                livro_id = int(input("ID do livro a ser atualizado: "))
                novo_preco = float(input("Novo preço: "))
                atualizar_preco_livro(livro_id, novo_preco)
                fazer_backup()
            except ValueError:
                print("Por favor, insira valores válidos.")
        
        elif opcao == '4':
            try:
                livro_id = int(input("ID do livro a ser removido: "))
                remover_livro(livro_id)
                fazer_backup()
            except ValueError:
                print("Por favor, insira um ID válido.")
        
        elif opcao == '5':
            autor = input("Autor: ")
            buscar_livros_por_autor(autor)
        
        elif opcao == '6':
            exportar_para_csv()
        
        elif opcao == '7':
            csv_path = input("Caminho do arquivo CSV: ")
            importar_de_csv(csv_path)
        
        elif opcao == '8':
            fazer_backup()
            limpar_backups_antigos()
        
        elif opcao == '9':
            print("Saindo...")
            fechar_conexao()
            break

if __name__ == "__main__":
    menu()
