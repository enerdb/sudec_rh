import streamlit as st
from datamodels.sudec_rh_classes import Servidor
import config
import pandas as pd
from drive import drive_update_servidor

militar = st.checkbox('Militar')


with st.form("Alterar Cadastro de Servidor"):
    
    col1, col2, col3 = st.columns(3)

    matricula = col1.number_input('Digite a matrícula SSP do servidor', step = 1, value = None)
    nome     = col1.text_input('Nome completo')
    nome_guerra = col1.text_input('Nome de guerra')
    
    if militar:
        poston = col2.selectbox('Posto ou graduação', list(config.POSTO_NUM.keys()))
        posto = config.POSTO_NUM[poston]
        quadro = col2.selectbox('Quadro', config.LISTA_QUADROS) 
        siape = col2.number_input('Matrícula Siape',step = 1, value = None)
    else:
        posto = config.POSTO_NUM['Agente Civil']
        quadro = None
        siape = None

    submit = st.form_submit_button('Cadastrar servidor')


if submit:
    novo_servidor = Servidor(
        matricula = matricula,
        nome = nome,
        nome_guerra = nome_guerra,
        militar = militar,
        posto = posto,
        quadro = quadro,
        siape = siape
    )

    df = pd.DataFrame([novo_servidor.model_dump()])

    st.session_state['data']['serv_total'] = pd.concat([st.session_state['data']['serv_total'], df], ignore_index=True)

    drive_update_servidor(st.session_state['data']['serv_total'])
    st.success('Servidor cadastrado com sucesso')







    

