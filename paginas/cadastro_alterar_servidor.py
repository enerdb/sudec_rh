######################################
# Orientações
# Fazer esse cadastro já pensando no modelo de dados novos
# Quando estiver tudo funcionando, migrar dados antigos.
# 
######################################

######################################
# Imports
import streamlit as st
import config
from datamodels.sudec_rh_classes import Servidor

import pandas as pd

##################
#  Helper functions

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

def prepara_lista_select(lista, dado_old):
    
    if (dado_old) and (dado_old in lista):
        lista.remove(dado_old)
        lista.insert(0, dado_old)
    return lista

def empty2none(dado):
    if not dado:
        return None
    elif dado == '':
        return None
    else:
        return dado

def none2empty(dado):
    if not dado:
        return ''
    else:
        return dado

##################
#  Carrega dados
df_pessoas = st.session_state['data']['pessoas']


#  Seleciona servidor para alterar
matricula = seleciona_servidor_input(df_pessoas)

# Flag para alterar dados confidenciais
alterar_confidenciais = st.checkbox("Incluir ou alterar dados confidenciais")
st.write("Para proteção dos usuários, os dados confidenciais cadastrados anteriormente não serão exibidos nesta tela")

# Formulário
if matricula:

    servidor = df_pessoas[df_pessoas["matricula"]==matricula].iloc[0]
    
    if servidor.shape[0]==0:
        st.error('Matrícula não encontrada')
    else:
        regulares = ['nome', 'nome_guerra', 'militar', 'posto', 'quadro', 'cidade', 'sexo', 'siape', 'horario', 'atividade', 'local_trab'] 
        confidenciais = ['cpf', 'endereco', 'cep', 'fone1', 'fone2', 'emaili', 'emailp', 'tipo_sang', 'emergenc_cont', 'alergias', 'outr_cond']
        allvars  = regulares + confidenciais
        
        temp = {}
        for var in allvars:
            temp[var] = servidor[var]
    
        with st.form("Alterar Cadastro de Servidor"):
        
            temp['nome']         = st.text_input('Nome completo', value=temp['nome'])
            temp['nome_guerra']  = st.text_input('Nome de guerra', value=temp['nome_guerra'])
            temp['militar']      = st.checkbox('Militar', value = temp['militar'])
            postof               = st.selectbox('Posto ou graduação', prepara_lista_select(list(config.POSTO_NUM.keys()),config.POSTO_FULL_NAME[temp['posto']]))
            temp['posto']        = config.POSTO_NUM[postof]
            temp['quadro']       = st.selectbox('Quadro', prepara_lista_select(config.LISTA_QUADROS,temp['quadro']))
            temp['cidade']       = st.selectbox('Cidade', prepara_lista_select(config.LISTA_CIDADES,none2empty(temp['cidade'] )))
            temp['sexo']         = st.selectbox('Sexo', prepara_lista_select(config.LISTA_SEXO, none2empty(temp['sexo'])))
            temp['horario']      = st.selectbox('Horário de trabalho', prepara_lista_select(config.LISTA_HORARIOS, none2empty(temp['horario'])))
            temp['siape']        = st.number_input('Siape', value=temp['siape'])           
            temp['atividade']    = st.selectbox('Atividade Predominante', prepara_lista_select(config.LISTA_ATIVIDADES, none2empty(temp['atividade'])))
            temp['local_trab']   = st.selectbox('Local de Trabalho', prepara_lista_select(config.LISTA_LOCAL_TRAB, none2empty(temp['local_trab'])))

            # Pensar em uma forma de manter os dados caso queira alterar alguns.
            if alterar_confidenciais:
                                
                temp['cpf']             = st.number_input('CPF - apenas números',step = 1, value = None)
                temp['endereco']        = st.text_input('Endereço')
                temp['cep']             = st.text_input('CEP')
                temp['fone1']           = st.text_input('Telefone 1')
                temp['fone2']           = st.text_input('Telefone 2')
                temp['emaili']          = st.text_input('e-mail institucional')
                temp['emailp']          = st.text_input('e-mail particular')
                temp['tipo_sang']       = st.selectbox('Tipo sanguíneo', prepara_lista_select(config.LISTA_TIPO_SANGUINEO, none2empty(temp['tipo_sang'])))
                temp['emergenc_cont']   = st.text_input('Contato de emergência')
                temp['alergias']        = st.text_input('Alergias')
                temp['outr_cond']       = st.text_input('Outra condição de saúde a considerar')



            submit = st.form_submit_button('Enviar dados')

        if submit:

            novo_servidor = Servidor(
                matricula = matricula,
                nome = temp['nome'],
                nome_guerra = temp['nome_guerra'],
                militar = temp['militar'],
                posto =  empty2none(temp['posto']),
                quadro =  empty2none(temp['quadro']),
                cidade =  empty2none(temp['cidade']),
                sexo =  empty2none(temp['sexo']),
                siape = temp['siape'],
                horario =  empty2none(temp['horario']),
                atividade =  empty2none(temp['atividade']),
                local_trab =  empty2none(temp['local_trab']),
                cpf = temp['cpf'],
                endereco =  empty2none(temp['endereco']),
                cep =  empty2none(temp['cep']),
                fone1 =  empty2none(temp['fone1']),
                fone2 =  empty2none(temp['fone2']),
                emaili =  empty2none(temp['emaili']),
                emailp =  empty2none(temp['emailp']),
                tipo_sang =  empty2none(temp['tipo_sang']),
                emergenc_cont =  empty2none(temp['emergenc_cont']),
                alergias =  empty2none(temp['alergias']),
                outr_cond =  empty2none(temp['outr_cond'])
            )
            st.write(novo_servidor.model_dump())

            df1 = pd.DataFrame([novo_servidor.model_dump()]) 
            
            st.dataframe(df1)
            
            servidor = pd.DataFrame([servidor.to_dict()])
            st.dataframe(servidor)
            #servidor.index = df1.index
            
            #st.write(type(servidor))

            df1 = df1.fillna(servidor)

            st.dataframe(df1)

            st.success('Novos dados impressos com Sucesso')
            st.error('O Cadastro no sistema não foi realizado')


