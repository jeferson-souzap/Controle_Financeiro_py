import streamlit as st
import datetime

#configuração
from utils.config import obter_categorias, remover_categoria, adicionar_categoria, obter_categorias_tipo


st.title("Adicionar Despesas")


col1, col2 = st.columns(2)

with col1:
    descricao = st.text_input("Descrição:", placeholder="Ex.: dividendos da bolsa, herança...")

with col2:
    valor = st.text_input("Valor:", placeholder="R$0.00")

col3, col4 = st.columns(2)

with col3:
    data = st.date_input("Data:", value=datetime.date.today())

with col4:
    st.markdown("**Opções Extras**")
    foi_recebida = st.toggle("Foi recebida", value=False)
    recorrente = st.toggle("Despesa Recorrente", value=False)

#---------------------------------------------------------------------------------
#Dropdown de categoria
categoria_db =  obter_categorias_tipo()
categoria = st.selectbox("Categoria da despesa", categoria_db)


#---------------------------------------------------------------------------------
# Botão de envio final
if st.button("Adicionar despesa"):
    # Aqui você pode adicionar a lógica para adicionar a despesa ao banco de dados
    st.success("Despesa adicionada com sucesso!")
