import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np



#####################
# CARREGANDO DADOS
#####################

dados = st.session_state['data']
df_afastamentos = dados['dias_afastamento']
df_servidores = dados['serv_total']


#####################
# FUNCTIONS
#####################

def gera_lista_afastados(df_afastamentos, dia_i, dia_f):
    # Rever a forma de retorno. Separar por dia ou por matrícula?
    # Retornar DataFrame?

    dias = pd.date_range(dia_i, dia_f).tolist() 

    lista_servidores_afastados = []
    for dia in dias:
        afastamentos_dia = df_afastamentos[df_afastamentos['Dia']==dia.date()]

        #st.write(dia)
        #st.write(df_afastamentos['Dia'].iloc[0])
        #st.write(afastamentos_dia)
        lista_servidores_afastados.extend(afastamentos_dia['Matrícula'].to_list())

    return set(lista_servidores_afastados)




######################
# INTERFACE
######################
dia_i = st.sidebar.date_input('Insira a data inicial', format = 'DD/MM/YYYY')

dia_f = st.sidebar.date_input('Insira a data final', format = 'DD/MM/YYYY')

if st.sidebar.button("Exibir dados"):

    if (dia_f < dia_i):
        st.markdown("## A data final deve ser maior ou igual à inicial")
    else:
        lista_servidores_afastados = gera_lista_afastados(df_afastamentos, dia_i, dia_f)

        
       
        df_afast_filtered = df_afastamentos[(df_afastamentos['Dia']>=dia_i) & (df_afastamentos['Dia']<=dia_f)][['Matrícula','Dia']]
        df_primeiro_dia = df_afast_filtered.groupby(['Matrícula']).min().rename(columns={"Dia": "Primeiro Dia"})
        df_ultimo_dia = df_afast_filtered.groupby(['Matrícula']).max().rename(columns={"Dia": "Último Dia"})

        df_servidores_afastados = df_servidores[df_servidores['Matrícula na SSP'].isin(lista_servidores_afastados)]
      
        df_servidores_afastados = df_servidores_afastados.join(df_primeiro_dia, on = 'Matrícula na SSP')
        df_servidores_afastados = df_servidores_afastados.join(df_ultimo_dia, on = 'Matrícula na SSP')

        
        #df_servidores_afastados = df_servidores[df_servidores['Matrícula na SSP'].isin(lista_servidores_afastados)]
        df_servidores_disponiveis = df_servidores[~df_servidores['Matrícula na SSP'].isin(lista_servidores_afastados)]

        columns_afast_display = ['Matrícula na SSP', 'Nome Completo', 'Posto ou Graduação', 'Quadro QOBM/QBMG', 'Nome de Guerra (preferencial se civil)', 'Cidade', 'Primeiro Dia', 'Último Dia', 'Antiguidade']
        columns_disponivel_display = ['Matrícula na SSP', 'Nome Completo', 'Posto ou Graduação', 'Quadro QOBM/QBMG', 'Nome de Guerra (preferencial se civil)', 'Cidade', 'Antiguidade']

  
        st.markdown(f'#### Servidores afastados no período')
        df_toprint = df_servidores_afastados[columns_afast_display].sort_values('Antiguidade').reset_index(drop=True)
        df_toprint.index +=1
        st.dataframe(
            df_toprint,
            column_config = {
            'Matrícula na SSP': st.column_config.NumberColumn(format = '%d'),
            'Primeiro Dia': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            'Último Dia': st.column_config.DateColumn(format = 'DD/MM/YYYY')
            }
        )

        st.markdown(f'#### Servidores disponíves no período')
        df_toprint = df_servidores_disponiveis[columns_disponivel_display].sort_values('Antiguidade').reset_index(drop=True)
        df_toprint.index +=1

        st.dataframe(
            df_toprint,
            column_config = {
            'Matrícula na SSP': st.column_config.NumberColumn(format = '%d')
            }
        )

