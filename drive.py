import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
import base64
from dotenv import load_dotenv
import pandas as pd


def generate_credentials():
    if not os.path.exists("credentials.json"):
        load_dotenv()
        credentials_base64 = os.getenv("GOOGLE_CREDENTIALS")
        if credentials_base64:
            credentials_json = base64.b64decode(credentials_base64).decode("utf-8")
            credentials_dict = json.loads(credentials_json)

            with open("credentials.json", "w") as f:
                f.write(json.dumps(credentials_dict))

def get_sheet_from_drive(planilha):
    generate_credentials()
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",  # Acesso a planilhas
        "https://www.googleapis.com/auth/drive",   # Acesso ao Google Drive
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(filename='credentials.json', scopes=scopes)
    client = gspread.authorize(creds)
    id_pasta = '16qXeetFnH6PuyIkz-D0gviZxG8orHrNQ'
    nome_planilha = planilha
    #nome_planilha = 'dados_rh'

    return client.open(title=nome_planilha, folder_id=id_pasta)

def update_worksheet_from_df(worksheet, df):
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())


def get_data_from_drive(sheet, tab):
    # tab = nome da aba
    return pd.DataFrame(sheet.worksheet(tab).get_all_records())

def get_df_from_drive(sheet, tab):
    # tab = nome da aba
    return pd.DataFrame(sheet.worksheet(tab).get_all_records())


def drive_update_abono(df):
    sheet = get_sheet_from_drive('dados_rh')
    update_worksheet_from_df(sheet.worksheet('abono'), df)

def drive_update_servidor():
    

























# def show_worksheet(planilha):
#     dados = planilha.get_all_records()
#     df = pd.DataFrame(dados)
#     st.write(df)

def update_worksheet(worksheet):
    worksheet.update_acell(
        row=5,
        col=1,
        value="Novo Curso"
    )

def add_line2worksheet(worksheet, value):

    # tips
    # https://docs.gspread.org/en/latest/user-guide.html
    # worksheet.update([[1, 2], [3, 4]], 'A1:B2')
    # ou
    # worksheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())

    dados = worksheet.get_all_records()
    n_rows = len(dados)
    worksheet.update_cell(
        row=n_rows+2,
        col=1,
        value=value
    )
