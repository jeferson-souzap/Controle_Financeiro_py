# No arquivo main.py
import streamlit as st



st.set_page_config(page_title="Controle Financeiro", layout="wide", initial_sidebar_state='collapsed')


col_met01, col_met02, col_met03 = st.columns(3, border=True)

with col_met01:
    st.metric(label='', value=10)

with col_met02:
    st.metric(label='', value=20)

with col_met03:
    st.metric(label='', value=30)


