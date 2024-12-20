import streamlit as st

st.set_page_config(
    page_title="Afastamentos",
    page_icon='🏖',
    layout = 'wide'
)

dados = st.session_state['data']

st.markdown('## Servidores')
st.dataframe(dados['servidores'])
st.markdown('## Afastamentos')
st.dataframe(dados['afastamentos'])
st.markdown('## Férias')
st.dataframe(dados['ferias'])
st.markdown('## Abono Anual')
st.dataframe(dados['abono'])

