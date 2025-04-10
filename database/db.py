import sqlite3

conn = sqlite3.connect(r"D:\#Mega\Jeferson - Dev\02 - Linguagens\Python\Controle_Financeiro_py\dados\controle.db")
cursor = conn.cursor()

# Tabela de usuários
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")

# Tabela de categorias
cursor.execute("""
CREATE TABLE IF NOT EXISTS categoria (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    grupo TEXT NOT NULL,               
    tipo TEXT CHECK (tipo IN ('entrada', 'saida')) NOT NULL
)
""")


# Tabela de categorias
cursor.execute("""
CREATE TABLE IF NOT EXISTS grupos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
)
""")



# Tabela de lançamentos
cursor.execute("""
CREATE TABLE IF NOT EXISTS lancamento (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data DATE NOT NULL,
    valor REAL NOT NULL,
    status TEXT CHECK (status IN ('pago', 'pendente')) NOT NULL DEFAULT 'pendente',
    fixo BOOLEAN NOT NULL DEFAULT 0,
    usuario_id INTEGER,
    categoria_id INTEGER,
    observacao TEXT,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id),
    FOREIGN KEY (categoria_id) REFERENCES categoria(id)
)
""")

conn.commit()
conn.close()
