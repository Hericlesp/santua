import sqlite3 as sql
import os

DB_PATH = r"C:\Users\Justino\Documents\Hexa\git&github\santua\data"
DB_DIR = os.path.join(DB_PATH, "database.db")


class CriarBanco:
    def __init__(self):
        """Inicializa a conexão com o banco de dados e cria as tabelas se não existirem."""
        if not os.path.exists(DB_PATH):
            os.makedirs(DB_PATH)

        self.create_tables()


    def create_tables(self):
        """Cria as tabelas no banco de dados."""
        with sql.connect(DB_DIR) as conn:
            cursor = conn.cursor()

            # Criação da tabela funcionarios
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS funcionarios (
                    ID_FUNCIONARIO INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOME TEXT NOT NULL,
                    DATA_ADM date NOT NULL,
                    CARGO TEXT NOT NULL,
                    PERMISSAO TEXT NOT NULL CHECK (permissao IN ('USER', 'ROOT'))
                )
            ''')

            # Criação da tabela dadosmes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS dadosmes (
                    id_mes INTEGER PRIMARY KEY AUTOINCREMENT,
                    mes TEXT NOT NULL,
                    ano INTEGER NOT NULL,
                    id_funcionario_dados INTEGER,
                    nome_funci TEXT NOT NULL,
                    total_horas_trabalhadas REAL NOT NULL,
                    data_trabalho DATE NOT NULL,
                    hora_entrada TIME NOT NULL,
                    hora_saida TIME NOT NULL,
                    intervalo_entrada TIME,
                    intervalo_saida TIME,
                    horas_trabalhadas REAL NOT NULL,
                    horas_extras REAL,
                    horas_faltantes REAL,
                    observacoes TEXT,
                    FOREIGN KEY (id_funcionario_dados) REFERENCES funcionarios(id_funcionario)
                )
            ''')

            conn.commit()
            conn.close()


if __name__ == "__main__":
    CriarBanco()

#permissao TEXT("USER", "ROOT") NOT NULL'

# class Database:
    
    
    
#     def __init__(self, db_name='usuarios.db'):
#         self.db_name = db_name
#         self.conn = None
#         self.cursor = None
#         self.connect()
#         self.setup_database()

#     def connect(self):
#         self.conn = sql.connect(self.db_name)
#         self.cursor = self.conn.cursor()
        
#     def caminho_do_banco(self):
#         return DB_DIR

#     def setup_database(self):
#         self.cursor.execute('''
#             CREATE TABLE IF NOT EXISTS usuarios (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 nome TEXT NOT NULL,
#                 email TEXT NOT NULL,
#                 senha TEXT NOT NULL,
#                 horario_preferido TEXT,
#                 data_nascimento TEXT
#             )
#         ''')
#         self.conn.commit()

#     def add_user(self, nome, email, senha, horario_preferido=None, data_nascimento=None):
#         self.cursor.execute('''
#             INSERT INTO usuarios (nome, email, senha, horario_preferido, data_nascimento)
#             VALUES (?, ?, ?, ?, ?)
#         ''', (nome, email, senha, horario_preferido, data_nascimento))
#         self.conn.commit()

#     def get_all_users(self):
#         self.cursor.execute('SELECT * FROM usuarios')
#         return self.cursor.fetchall()

#     def close(self):
#         if self.conn:
#             self.conn.close()