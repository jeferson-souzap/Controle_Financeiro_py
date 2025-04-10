import streamlit as st
import pandas as pd

# Simulação de dados extraídos do banco
dados = pd.DataFrame([
    {"categoria": "Água", "valor": 105, "mes": "Fevereiro", "status": "Pago"},
    {"categoria": "Luz", "valor": 276, "mes": "Março", "status": "Pendente"},
    {"categoria": "Internet", "valor": 139.98, "mes": "Abril", "status": "Pago"},
    # ...
])

# Pivot estilo planilha
tabela = dados.pivot_table(
    index="categoria",
    columns="mes",
    values="valor",
    aggfunc="sum"
)

# Criação de uma função para colorir valores pagos/pendentes
def destaque_valores(val):
    if pd.isnull(val):
        return ''
    return 'background-color: #b6fcd5' if val > 0 else ''

# Exibição
st.write("### Planejamento Mensal (Estilo Planilha)")
st.dataframe(tabela.style.applymap(destaque_valores))

