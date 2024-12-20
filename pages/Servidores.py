import streamlit as st

st.set_page_config(
    page_title="Servidores",
    page_icon='📄',
    layout = 'wide'
)

df_data = st.session_state['data']['servidores']

setores = df_data['Atividade predominante'].unique()
setor = st.sidebar.selectbox('Setor', setores)

servidores_setor = df_data[df_data['Atividade predominante']==setor].set_index('Matrícula na SSP')


st.dataframe(servidores_setor)