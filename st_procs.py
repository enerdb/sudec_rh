import streamlit as st
import config

def seleciona_servidor_input(df):
    st.markdown('##### Selecione um servidor')
    
    df['posto_busca'] = df['posto'].map(config.POSTO_SHORT_NAME)
    df['nome_busca'] = df["posto_busca"] + ' ' + df["nome_guerra"] + ' - ' + df["nome"]
    options = df['nome_busca'].to_list()
    options.insert(0,'')

    nome_busca = st.selectbox('Insira um nome para buscar', options = options)
    if nome_busca == '':
        matricula = None
    else:
        matricula = float(df[df['nome_busca']==nome_busca]['matricula'].iloc[0])

    st.markdown('##### ou digite diretamente a matrícula')

    # Input de matricula
    matricula = st.number_input('Digite a matrícula do servidor', value=matricula, format='%.0f')

    # limpa dados
    df.drop(columns = ['nome_busca', 'posto_busca'])

    return matricula