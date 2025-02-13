import streamlit as st
import pandas as pd    
from datahandlers.servidor import filter_servidor_by_matricula
import config

dados = st.session_state['data']
#df_servidores = dados['serv_total'] 
df_servidores = dados['servidores'] 

col1, col2, col3 = st.columns(3)
matricula = col1.number_input('Digite a matrícula SSP do servidor', value=None, step = 1)

if matricula:

    # colunas = ["Matrícula na SSP","Nome Completo","Nome de Guerra (preferencial se civil)","Efetividade","Posto ou Graduação","Quadro QOBM/QBMG","Cidade","Sexo", "Horário de trabalho", "Atividade predominante", "Local de Trabalho"]
   
    colunas = ["Nome Completo","Nome de Guerra (preferencial se civil)","Efetividade","Posto ou Graduação","Quadro QOBM/QBMG","Cidade","Sexo"]

    df_servidor = filter_servidor_by_matricula(df_servidores,matricula,)[colunas]

    st.dataframe(df_servidor)
    
    nome = df_servidor['Nome Completo'].iloc[0]
    nome_war = df_servidor["Nome de Guerra (preferencial se civil)"].iloc[0]
    efetividade = df_servidor["Efetividade"].iloc[0]
    posto = df_servidor["Posto ou Graduação"].iloc[0]
    quadro = df_servidor["Quadro QOBM/QBMG"].iloc[0]
    cidade = df_servidor["Cidade"].iloc[0]
    sexo = df_servidor['Sexo'].iloc[0]


    def prepara_lista_select(lista, dado_old):
        
        if (dado_old) and (dado_old in lista):
            lista.remove(dado_old)
            lista.insert(0, dado_old)
        return lista
        

    with st.form("Alterar Cadastro de Servidor"):

        # col1, col2, col3, col4, col5 = st.columns(5)
        #columns = [col1, col2, col3, col4, col5]
       
        nome     = st.text_input('Nome completo', value=df_servidor['Nome Completo'].iloc[0])
        nome_war = st.text_input('Nome de guerra', value=df_servidor["Nome de Guerra (preferencial se civil)"].iloc[0])
        efetividade = st.selectbox('Efetividade', prepara_lista_select(config.LISTA_EFETIVIDADE, efetividade))    
        posto = st.selectbox('Posto ou graduação', prepara_lista_select(config.LISTA_POSTOS,posto))
        quadro = st.selectbox('Quadro', prepara_lista_select(config.LISTA_QUADROS,quadro))     
        cidade = st.selectbox('Cidade', prepara_lista_select(config.LISTA_CIDADES,cidade))   
        sexo = st.selectbox('Sexo', prepara_lista_select(['Masculino', 'Feminino'], sexo))

        submit = st.form_submit_button('Enviar dados')

    if submit:
        st.write(f'Matricula: {matricula}')
        st.write(f'Nome: {nome}')
        st.write(f'Nome de guerra: {nome_war}')
        st.write(f'Efetividade: {efetividade}')
        st.write(f'Posto: {posto}')
        st.write(f'Quadro: {quadro}')
        st.write(f'Cidade: {cidade}')
        st.write(f'Sexo: {sexo}')
        
        st.success('Novos dados impressos com Sucesso')
        st.error('O Cadastro no sistema não foi realizado')