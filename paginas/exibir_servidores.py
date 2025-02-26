import streamlit as st
import pandas as pd
import config


#df_data = st.session_state['data']['servidores']
df_data = st.session_state['data']['serv_total']

# Lista Setores
setores = df_data['atividade'].unique()


# Multiselect
setores_selected = st.sidebar.multiselect('Filtrar por Setor de Trabalho', setores, placeholder = 'Selecione os Setores')

# Inclui todos os servidores se não houver seleção
if not setores_selected:
    setores_selected = setores

#Segmenta DF com base na seleção
servidores_display = df_data[df_data['atividade'].isin(setores_selected)].set_index('matricula').sort_values('posto')

servidores_display['posto'] = servidores_display['posto'].map(config.POSTO_SHORT_NAME).fillna('')

# Exibe seleção filtrada


st.dataframe(
    servidores_display[config.SERV_COLUNAS_DISPLAY],
    column_config = {
        'matricula': st.column_config.NumberColumn(format = '%d'),
        'militar' :st.column_config.CheckboxColumn()
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