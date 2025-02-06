import streamlit as st

import pandas as pd
from drive import get_sheet_from_drive, update_worksheet_from_df, add_line2worksheet



st.set_page_config(
    page_title="Inserir dados",
    page_icon='✏',
    layout = 'wide'
)

st.markdown("""
            # ESSA PÁGINA AINDA NÃO ESTÁ FUNCIONANDO
            # FAVOR NÃO UTILIZAR AINDA
            """)

################################################################################################
# CARREGA DADOS
################################################################################################

dados = st.session_state['data']

################################################################################################
# AUTENTICAÇÃO NO GOOGLE
################################################################################################




sheet = get_sheet_from_drive()
worksheet = sheet.get_worksheet(0)

curso = st.text_input('Insira um novo curso')
if st.button("inserir"):
    add_line2worksheet(worksheet, curso)
    st.success('Curso adicionado')

