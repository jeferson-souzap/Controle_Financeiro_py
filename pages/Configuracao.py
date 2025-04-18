import streamlit as st
import datetime

#---------------------
from utils.config import adicionar_categoria, remover_categoria, obter_categorias, obter_categorias_tipo

st.header('Área de Cadastro')

col01, col02 = st.columns(2, border=True)

with col01:
    st.markdown("### Adicionar categoria")

    categoria_db =  obter_categorias_tipo()
    #categoria = st.selectbox("Categoria da despesa", categoria_db)

    nova_categoria = st.text_input("Nova categoria...", key="nova_cat")

    # Corrigido para usar valores válidos
    tipo = st.radio('Selecione o tipo de Categoria:', ["entrada", "saida"], index=0)

    col_but01, _ = st.columns([1, 2])    
    with col_but01:
        if st.button("Adicionar", key="btn_add_cat"):
            if nova_categoria and nova_categoria not in categoria_db:
                adicionar_categoria(nova_categoria, tipo)  # Adiciona ao banco de dados
                st.success(f"Categoria '{nova_categoria}' do tipo '{tipo}' adicionada.")
            else:
                st.warning("Categoria inválida ou já existente.")
                st.rerun()
    
    #---------------------------------------------------------------

with col02:
    st.markdown("### Excluir categorias")
    categorias_selecionadas = st.multiselect(
        label="Selecione para excluir",
        options=categoria_db,
        key="excluir_cat"
    )

    
    if st.button("Remover", key="btn_remover"):
        for cat in categorias_selecionadas:
            remover_categoria(cat)  # Remove do banco de dados
        st.success("Categorias removidas.")


st.dataframe(categoria_db)
    