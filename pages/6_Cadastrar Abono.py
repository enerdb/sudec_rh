import streamlit as st
import pandas as pd
from datetime import datetime, date
from time import sleep
from drive import drive_update_abono

from datamodels.abono import trata_abono_2drive, trata_abono_2sys, filter_abono_by_matricula_ano, concat_abonos

st.set_page_config(
    page_title="Inserir dados",
    page_icon='✏',
    layout = 'wide'
)

st.markdown("## Insira os dados do servidor e o ano de referência do abono")

#####################
# Funções
#####################




#####################
# CARREGANDO DADOS
#####################

dados = st.session_state['data']

df_servidores = dados['serv_total'] 
df_abono = dados['abono']

#####################
# INTERFACE
#####################


col1, col2, col3 = st.columns(3)

# Identifica Servidor e ano
# matricula = col1.number_input('Digite a matrícula SSP do servidor', value=None, format='%.0f')
matricula = col1.number_input('Digite a matrícula SSP do servidor', value=None, step = 1)
ano_ref = col1.selectbox('Ano de referência', [2024 + i for i in range(10)])


if matricula:
    servidor = df_servidores[df_servidores['Matrícula na SSP']==matricula]
    col1.markdown(f'**Nome Completo:** {servidor['Nome Completo'].iloc[0]}')

if matricula and ano_ref:
    colunas = ['Ano do gozo', '1º dia', '2º dia', '3º dia', '4º dia', '5º dia', 'SEI']

    df_abono_corrente = filter_abono_by_matricula_ano(df_abono,matricula, ano_ref)[colunas].set_index('Ano do gozo')

    st.dataframe(
        df_abono_corrente,
        column_config = {
            'Ano do gozo': st.column_config.NumberColumn(format = '%d'),
            '1º dia': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            '2º dia': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            '3º dia': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            '4º dia': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            '5º dia': st.column_config.DateColumn(format = 'DD/MM/YYYY')
            }
        )

    # Formulário de alteração de abono
        # Inicializa variáveis com os valores atuais.
    if df_abono_corrente.shape[0] == 0 :
        df_abono_corrente.loc[ano_ref] = [None, None, None, None, None, None]

    # def safe_convert_date(value):
    #     if pd.isna(value) or value is None:
    #         return None
    #     if isinstance(value, str):
    #         return datetime.strptime(value, "%d/%m/%Y").date()
    #     if isinstance(value, pd.Timestamp):
    #         return value.date()
    #     if isinstance(value, date):
    #         return value
    #     return None  # Fallback se vier algo inesperado

    # dia1 = safe_convert_date(df_abono_corrente['1º dia'].iloc[0])
    # dia2 = safe_convert_date(df_abono_corrente['2º dia'].iloc[0])
    # dia3 = safe_convert_date(df_abono_corrente['3º dia'].iloc[0])
    # dia4 = safe_convert_date(df_abono_corrente['4º dia'].iloc[0])
    # dia5 = safe_convert_date(df_abono_corrente['5º dia'].iloc[0])
    # sei = df_abono_corrente['SEI'].iloc[0]
    
    dia1 = df_abono_corrente['1º dia'].iloc[0]
    dia2 = df_abono_corrente['2º dia'].iloc[0]
    dia3 = df_abono_corrente['3º dia'].iloc[0]
    dia4 = df_abono_corrente['4º dia'].iloc[0]
    dia5 = df_abono_corrente['5º dia'].iloc[0]
    sei = df_abono_corrente['SEI'].iloc[0]

    st.markdown("### Cadastro ou alteração de abono")

    # Preenche formulário
    with st.form("Alterar Abono"):

        col1, col2, col3, col4, col5 = st.columns(5)
        
        dia1 = col1.date_input('1º dia', format = 'DD/MM/YYYY', value = dia1)
        dia2 = col2.date_input('2º dia', format = 'DD/MM/YYYY', value = dia2)
        dia3 = col3.date_input('3º dia', format = 'DD/MM/YYYY', value = dia3)
        dia4 = col4.date_input('4º dia', format = 'DD/MM/YYYY', value = dia4)
        dia5 = col5.date_input('5º dia', format = 'DD/MM/YYYY', value = dia5)

        # dia1 = col1.date_input('1º dia', format = 'DD/MM/YYYY', value = dia1).strftime('%d/%m/%Y')
        # dia2 = col2.date_input('2º dia', format = 'DD/MM/YYYY', value = dia2).strftime('%d/%m/%Y')
        # dia3 = col3.date_input('3º dia', format = 'DD/MM/YYYY', value = dia3).strftime('%d/%m/%Y')
        # dia4 = col4.date_input('4º dia', format = 'DD/MM/YYYY', value = dia4).strftime('%d/%m/%Y')
        # dia5 = col5.date_input('5º dia', format = 'DD/MM/YYYY', value = dia5).strftime('%d/%m/%Y')
        sei = st.text_input('Processo SEI', value=sei)
        novo_abono = pd.DataFrame([         
            {   "Timestamp": datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                "Matrícula SSP": matricula,
                "Ano do gozo": ano_ref,
                "1º dia": pd.to_datetime(dia1).date() if dia1 else None, 
                "2º dia": pd.to_datetime(dia2).date() if dia2 else None,
                "3º dia": pd.to_datetime(dia3).date() if dia3 else None,
                "4º dia": pd.to_datetime(dia4).date() if dia4 else None,
                "5º dia": pd.to_datetime(dia5).date() if dia5 else None,
                "SEI": sei}
                ]
        )

        novo_abono = trata_abono_2sys(novo_abono)
        
       
        submit = st.form_submit_button('Enviar dados')
        
    if submit:
        st.session_state['data']['abono'] = concat_abonos(df_abono, novo_abono)
        df = st.session_state['data']['abono']

        df = trata_abono_2drive(df)

        drive_update_abono(df)
        st.success('Novo abono cadastrado')






