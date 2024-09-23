
# Sistema de Gerenciamento de Livraria
Alunos: Gabriel Rossa e Milena Schrickte

## Descrição
Este sistema foi desenvolvido para gerenciar uma livraria, incluindo o controle de livros, autores, e preços. Ele utiliza um banco de dados SQLite para armazenar as informações dos livros e permite exportar e importar dados em formato CSV. Além disso, o sistema oferece uma função de backup automática e manipulação de arquivos.

## Funcionalidades
- **Adicionar** novos livros.
- **Exibir** todos os livros cadastrados em formato de tabela.
- **Atualizar** o preço de um livro.
- **Remover** livros do sistema.
- **Buscar** livros por autor.
- **Exportar** dados para um arquivo CSV.
- **Importar** dados a partir de um arquivo CSV.
- **Backup automático** sempre que novos livros forem adicionados, atualizados ou removidos.
- **Limpeza de backups** antigos, mantendo apenas os 5 últimos backups.

## Estrutura do Projeto
```
/livraria/
    /backups/             # Diretório para armazenar os backups do banco de dados
    /data/                # Diretório para armazenar o banco de dados SQLite
    /exports/             # Diretório para exportar arquivos CSV
    database.py           # Arquivo para operações de banco de dados
    file_manager.py       # Arquivo para manipulação de arquivos (backups e CSV)
    main.py               # Arquivo principal que contém a lógica do sistema
    README.md             # Documentação do projeto
```

## Como Usar

### 1. Configuração do Ambiente

1. Certifique-se de ter o Python instalado. Use o comando:
   ```bash
   python --version
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install tabulate
   ```

### 2. Executar o Sistema
No terminal, navegue até o diretório raiz do projeto e execute o arquivo `main.py`:
```bash
python main.py
```

### 3. Funcionalidades

Ao rodar o programa, será exibido um menu de opções. Selecione a opção desejada digitando o número correspondente.

## Backup e Exportação
- Sempre que um novo livro for adicionado ou modificado, um backup automático será criado no diretório `/backups/`.
- O sistema exporta dados em formato CSV para o diretório `/exports/`.