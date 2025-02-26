import streamlit as st
from datamodels.sudec_rh_classes import Servidor
import config
import pandas as pd

from drive import drive_update_servidor


dados = st.session_state['data']

st.write(dados['servidores'])

secret = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vQn6fev7p2BoTmzOcP7AAvGwYgNEIHOJ6w4pMNLias9WH06a3bS5n4oR1Df8WcjURaP6rx9yVD09JW7/pub?gid=0&single=true&output=csv')  

st.write(secret)


servidores = []

for _, row in dados['servidores'].iterrows():

    secret_row = secret[secret['Matrícula na SSP'] == row['Matrícula na SSP']].replace({float('nan'): None})

    if not row['Efetividade']:
        row['Efetividade'] = 'Servidor Sem Vínculo'
    
    if row['Efetividade'] == 'Servidor Sem Vínculo':
        militar = False
    else:
        militar = True

    if secret_row['Tipo Sanguíneo'].values[0]:
        tipo_sang = secret_row['Tipo Sanguíneo'].values[0]+ secret_row['Fator RH'].values[0][-2]
    else:
        tipo_sang = None
    
        
    
    novo_servidor = Servidor(
        matricula = row['Matrícula na SSP'],
        nome = row['Nome Completo'],
        nome_guerra = row['Nome de Guerra (preferencial se civil)'],     
        militar = militar,
        posto = config.POSTO_NUM[row['Posto ou Graduação']],
        quadro = row['Quadro QOBM/QBMG'],
        siape = secret_row['Matrícula SIAPE'].values[0],
        cidade = row['Cidade'],
        horario = row['Horário de trabalho'],
        atividade = row['Atividade predominante'],
        local_trab = row['Local de Trabalho'],
        cpf = secret_row['CPF'].values[0],
        endereco = secret_row['Endereço Residencial'].values[0],
        cep = secret_row['CEP'].values[0],
        fone1 = secret_row['Telefone 1'].values[0],
        fone2 = secret_row['Telefone 2'].values[0],
        emaili = secret_row['E-mail Institucional (SSP e/ou CBMDF)'].values[0],
        emailp = secret_row['E-mail particular'].values[0],
        sexo = row['Sexo'],
        tipo_sang = tipo_sang,
        emergenc_cont = secret_row['Contato de emergência (NOME E TELEFONE)'].values[0],
        alergias = secret_row['Alergias'].values[0],
        outr_cond = secret_row['Outra condição de saúde relevante'].values[0],
    )
    servidores.append(novo_servidor.model_dump())
    


df = pd.DataFrame(servidores)


drive_update_servidor(df)
st.success('Servidores importados para drive com sucesso!')

#############################################################################
# O que o banco do sheets faz?
#############################################################################
# 1 Cadastro de servidores pelo forms
# 2 Cadastro de dados funcionais pelo forms
# 3 Registra funcionais com base no datetime mais recente
# 4 Valida servidores pelo datetime mais recente + Junta dados funcionais com tabela de servidores
# 4.1 Export private total - sem filtro
# 4.2 Export private nomeados - filtra nomeados usando import range de planilha de cargos

#############################################################################
# O que meu sistema já faz?
#############################################################################
# 1 Cadastro local de servidores e dados funcionais
# 2 ok - ver 1 acima
# 3 ok - alteração dinâmica com update do banco
# 4 ok - atteração dinâmica com update do banco	
# 4.1 - update no banco

# Falta - setar flag de nomeação - não vou setar aqui.
# como:
#   Ler tabela de cargos e fazer uma lista com ocupantes.
#   Filtra servidores com isin na lista de ocupantes





