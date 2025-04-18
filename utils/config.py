import streamlit as st
import sqlite3

local_banco = r'D:\#Mega\Jeferson - Dev\02 - Linguagens\Python\Controle_Financeiro_py\dados\controle.db'


# Função para obter categorias do banco de dados
def obter_categorias():
    conn = sqlite3.connect(local_banco)
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM categoria")
    categorias = cursor.fetchall()
    conn.close()
    return [categoria[0] for categoria in categorias]  # Retorna uma lista de nomes

def obter_categorias_tipo():
    conn = sqlite3.connect(local_banco)
    cursor = conn.cursor()
    cursor.execute("SELECT nome, tipo FROM categoria")
    categorias = cursor.fetchall()
    conn.close()
    return [categoria[0:2] for categoria in categorias]  # Retorna uma lista de nomes



def adicionar_categoria(nome, tipo):
    conn = sqlite3.connect(local_banco)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO categoria (nome, tipo) VALUES (?, ?)", (nome, tipo))
    conn.commit()
    conn.close()

def remover_categoria(nome):
    conn = sqlite3.connect(local_banco)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM categoria WHERE nome = ?", (nome))
    conn.commit()
    conn.close()