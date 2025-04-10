import streamlit as st
import datetime

st.title("Adicionar Despesas")

# Simula categorias existentes
if "categorias_despesa" not in st.session_state:
    st.session_state["categorias_despesa"] = ["Gasolina", "Saúde", "Aluguel", "Transporte", "Mercado"]


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

#Dropdown de categoria
categoria = st.selectbox("Categoria da despesa", options=st.session_state["categorias_despesa"])

# Expander para categorias
with st.expander("Adicionar/Remover Categorias"):
    st.markdown("### Adicionar categoria")
    nova_categoria = st.text_input("Nova categoria...", key="nova_cat")
    col_add, _ = st.columns([1, 4])
    with col_add:
        if st.button("Adicionar", key="btn_add_cat"):
            if nova_categoria and nova_categoria not in st.session_state["categorias_despesa"]:
                #Substituir pelo banco de dados
                st.session_state["categorias_despesa"].append(nova_categoria)
                
                st.success(f"Categoria '{nova_categoria}' adicionada.")
            else:
                st.warning("Categoria inválida ou já existente.")

    st.markdown("---")
    st.markdown("### Excluir categorias")
    categorias_selecionadas = st.multiselect(
        label="Selecione para excluir",
        options=st.session_state["categorias_despesa"],
        key="excluir_cat"
    )
    col_rem, _ = st.columns([1, 4])
    with col_rem:
        if st.button("Remover", key="btn_remover"):
            for cat in categorias_selecionadas:
                st.session_state["categorias_despesa"].remove(cat)
            st.success("Categorias removidas.")

st.markdown("---")
# Botão de envio final
if st.button("Adicionar despesa"):
    st.success("Despesa adicionada com sucesso!")

