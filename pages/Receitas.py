import streamlit as st
from datetime import datetime

st.title("Adicionar Receita")

# Layout em colunas
col1, col2 = st.columns(2)
with col1:
    descricao = st.text_input("Descrição:", placeholder="Ex: Salário, Dividendos")
with col2:
    valor = st.number_input("Valor:", min_value=0.0, format="%.2f")

# Data
data = st.date_input("Data:", value=datetime.today())

# Extras (switches)
st.markdown("**Extras**")
col_ex1, col_ex2 = st.columns(2)
with col_ex1:
    foi_recebida = st.toggle("Foi recebida")
with col_ex2:
    recorrente = st.toggle("Receita Recorrente")

# Categoria da receita
st.markdown("**Categoria da receita**")
categorias = ["Salário", "Comissão", "Dividendos", "Investimentos", "Outros"]
categoria = st.selectbox("Escolha a categoria:", categorias)

st.divider()

# Gerenciar categorias
with st.expander("➕ Adicionar / Remover Categorias"):
    nova_categoria = st.text_input("Nova categoria...")
    if st.button("Adicionar"):
        st.success(f"Categoria '{nova_categoria}' adicionada!")  # Aqui você adicionaria ao banco
    
    st.markdown("**Excluir categorias**")
    excluir = st.multiselect("Selecione categorias para remover:", categorias)
    if st.button("Remover selecionadas"):
        st.warning(f"Categorias removidas: {', '.join(excluir)}")  # Aqui também, update no banco

st.divider()

# Botão final
if st.button("✅ Adicionar Receita"):
    st.success(f"Receita de R$ {valor:.2f} adicionada com sucesso!")

