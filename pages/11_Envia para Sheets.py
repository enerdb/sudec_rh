import streamlit as st
import gspread
from google.oauth2.service_account import Credentials

import os
import json
import base64
from dotenv import load_dotenv
import pandas as pd


st.set_page_config(
    page_title="Inserir dados",
    page_icon='✏',
    layout = 'wide'
)

st.markdown("""
            # ESSA PÁGINA AINDA NÃO ESTÁ FUNCIONANDO
            # FAVOR NÃO UTILIZAR AINDA
            """)

######################
# CARREGA DADOS
######################

dados = st.session_state['data']


st.write("Atutenticando")
######################
# AUTENTICAÇÃO NO GOOGLE
######################

st.write("gerando json")
# Decodifica e carrega o arquivo no seu enviroment
if not os.path.exists("credentials.json"):
    load_dotenv()
    credentials_base64 = os.getenv("GOOGLE_CREDENTIALS")
    if credentials_base64:
        credentials_json = base64.b64decode(credentials_base64).decode("utf-8")
        credentials_dict = json.loads(credentials_json)

        with open("credentials.json", "w") as f:
            f.write(json.dumps(credentials_dict))

st.write("usando credenciais")
# Usar credenciais no código
scopes = ["https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

id_pasta = '16qXeetFnH6PuyIkz-D0gviZxG8orHrNQ'
nome_planilha = 'abono'

st.write("abrindo planilha")

planilha = client.open(title=nome_planilha, folder_id=id_pasta).get_worksheet(0)


def mostrar_planilha(planilha):
    dados = planilha.get_all_records()
    df = pd.DataFrame(dados)
# Imprime os dados brutos extraídos diretamente da planilha (lista de dicionários) 
    st.write(df)

mostrar_planilha(planilha=planilha)

st.write("escrevendo na planilha")

planilha.update_acell(label="A2", value="Python para todos")
mostrar_planilha(planilha=planilha)
