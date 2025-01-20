import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Servidores",
    page_icon='👨‍👦‍👦',
    layout = 'wide'
)

#df_data = st.session_state['data']['servidores']
df_data = st.session_state['data']['serv_total']





# Lista Setores
setores = df_data['Atividade predominante'].unique()


# Multiselect
setores_selected = st.sidebar.multiselect('Filtrar por Setor de Trabalho', setores, placeholder = 'Selecione os Setores')

# Inclui todos os servidores se não houver seleção
if not setores_selected:
    setores_selected = setores

#Segmenta DF com base na seleção
servidores_setor = df_data[df_data['Atividade predominante'].isin(setores_selected)].set_index('Matrícula na SSP')


# Exibe seleção filtrada
st.dataframe(
    servidores_setor,
    column_config = {
        'Matrícula na SSP': st.column_config.NumberColumn(format = '%d')
    }
)

###################################
# Download data
###################################


# @st.cache_data
# def convert_df(df):
#     # IMPORTANT: Cache the conversion to prevent computation on every rerun
#     return df.to_csv().encode("utf-8")

# csv = convert_df(servidores_setor)

# st.download_button(
#     label="Download data as CSV",
#     data=csv,
#     file_name="large_df.csv",
#     mime="text/csv",
# )