import sqlite3
from contextlib import closing

DATABASE_URL = "school.db"

def get_db():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn

def create_tables():
    with closing(get_db()) as db:
        with db:
            db.execute("""
            CREATE TABLE IF NOT EXISTS ALUNO (
                ID_ALUNO INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME TEXT NOT NULL,
                DATA_NASCIMENTO TEXT NOT NULL,
                LOGRADOURO TEXT,
                NUMERO INTEGER,
                BAIRRO TEXT,
                CIDADE TEXT,
                ESTADO TEXT,
                DATA_CRIACAO TEXT,
                CEP TEXT,
                ID_CURSO INTEGER
            )
            """)
            db.execute("""
            CREATE TABLE IF NOT EXISTS CURSO (
                ID_CURSO INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME TEXT NOT NULL,
                DATA_CRIACAO TEXT,
                ID_PROFESSOR INTEGER
            )
            """)
            db.execute("""
            CREATE TABLE IF NOT EXISTS PROFESSOR (
                ID_PROFESSOR INTEGER PRIMARY KEY AUTOINCREMENT,
                NOME TEXT NOT NULL,
                DATA_NASCIMENTO TEXT NOT NULL,
                DATA_CRIACAO TEXT
            )
            """)

create_tables()
