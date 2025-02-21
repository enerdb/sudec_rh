import streamlit as st
from datamodels.sudec_rh_classes import Servidor




with st.form("Alterar Cadastro de Servidor"):
    
    col1, col2, col3 = st.columns(3)

    matricula = col1.number_input('Digite a matrícula SSP do servidor', step = 1)
    nome     = st.text_input('Nome completo')
    nome_guerra = st.text_input('Nome de guerra')
    militar = st.checkbox('Militar')
    
    submit = st.form_submit_button('Cadastrar servidor')

if submit:
    novo_servidor = Servidor(
        matricula = matricula,
        nome = nome,
        nome_guerra = nome_guerra,
        militar = militar 
    )

    st.write(novo_servidor)


    

