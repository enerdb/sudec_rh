#streamlit run home.py


# Criar um projeto no google cloud
# ativar apis e serviços
# google drive api.
# ativar
# IAM e administrador
# Contas de serviço
# Criar conta de serviço
# Chave
# chave json
# baixar arquivo
# compartilhar planilha con a conta de serviço no sheets
# pip install gspread e oauth2client


'''
import gspread
import pandas as pd

from oauth2client.service_account import ServiceAccountCredentials

# Nome do arquivo de credenciais
filename = 'xxx.json'

# Escopos das APIs do Google Sheets e Drive
scopes = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

# Autenticar com a conta de serviço
creds = ServiceAccountCredentials.from_json_keyfile_name(filename=filename, scopes=scopes)
client = gspread.authorize(creds)

# Acessar a planilha pelo nome e ID da pasta
nome_planilha = "Cursos Gratuitos da Asimov"
id_pasta = 'xxxxx'
planilha = client.open(title=nome_planilha, folder_id=id_pasta).get_worksheet(0)

def mostrar_planilha(planilha):
    dados = planilha.get_all_records()
    df = pd.DataFrame(dados)
# Imprime os dados brutos extraídos diretamente da planilha (lista de dicionários) 
   print(dados)
    print('---') 
# Imprime os dados formatados como um DataFrame (tabela organizada)
    print(df)
    print('---')

if __name__ == '__main__':
    # Ler e exibir os dados
    print('READ')
    mostrar_planilha(planilha=planilha)

    # Criar um novo curso
    print('CREATE')
    planilha.update_cell(row=5, col=1, value="Novo Curso")
    planilha.update_acell(label="B7", value=0)
    mostrar_planilha(planilha=planilha)

    # Atualizar informações existentes
    print('UPDATE')
    planilha.update_acell(label="A2", value="Python para todos")
    mostrar_planilha(planilha=planilha)

    # Deletar uma linha
    print('DELETE')
    planilha.delete_rows(4)
    mostrar_planilha(planilha=planilha)


    acesso-sheets-sudec-bi@dotted-banner-445121-u4.iam.gserviceaccount.com

'''