import os
import shutil
from pathlib import Path
import csv
from datetime import datetime
from database import exibir_livros

# Caminho do banco de dados
db_dir = Path("data")
db_dir.mkdir(parents=True, exist_ok=True)  # Garante que o diretório "data" exista
db_path = db_dir / "livraria.db"  # Define o caminho completo para o banco de dados

def exportar_para_csv():
    try:
        livros = exibir_livros(retornar_lista=True)
        if not livros:
            print("Nenhum livro disponível para exportar.")
            return
        
        # Diretório de exportação atualizado para "exports"
        export_dir = Path("exports")  
        export_dir.mkdir(parents=True, exist_ok=True)  # Garante que o diretório 'exports' exista

        export_path = export_dir / "livros_exportados.csv"  # Caminho completo do arquivo
        
        with open(export_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Título', 'Autor', 'Ano de Publicação', 'Preço'])
            writer.writerows(livros)
        
        print(f"Dados exportados com sucesso para {export_path}")
    except Exception as e:
        print(f"Erro ao exportar dados para CSV: {e}")

def importar_de_csv(csv_path):
    from database import adicionar_livro  # Importa aqui para evitar dependência circular
    try:
        with open(csv_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Verifica se os campos estão corretos e acessa com o mesmo nome que os cabeçalhos do CSV
                titulo = row.get('Título')
                autor = row.get('Autor')
                ano_publicacao = row.get('Ano de Publicação')
                preco = row.get('Preço')

                if titulo and autor and ano_publicacao and preco:
                    # Convertendo os valores corretamente
                    adicionar_livro(titulo, autor, int(ano_publicacao), float(preco))
            print("Dados importados com sucesso!")
    except Exception as e:
        print(f"Erro ao importar dados de CSV: {e}")

def fazer_backup():
    try:
        # Diretório de backups atualizado para "backups/"
        backup_dir = Path("backups/")
        backup_dir.mkdir(parents=True, exist_ok=True)
        backup_filename = f"backup_livraria_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.db"
        backup_path = backup_dir / backup_filename
        
        shutil.copy(db_path, backup_path)
        print(f"Backup criado: {backup_path}")
    except Exception as e:
        print(f"Erro ao fazer backup: {e}")

def limpar_backups_antigos(max_backups=5):
    try:
        # Diretório de backups atualizado para "backups/"
        backup_dir = Path("backups/")
        backups = sorted(backup_dir.glob("*.db"), key=os.path.getmtime, reverse=True)
        
        for old_backup in backups[max_backups:]:
            os.remove(old_backup)
            print(f"Backup removido: {old_backup}")
    except Exception as e:
        print(f"Erro ao limpar backups antigos: {e}")
