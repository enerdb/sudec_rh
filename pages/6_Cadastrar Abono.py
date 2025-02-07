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

n_abonos = 0
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


    dias = ['1º dia', '2º dia', '3º dia', '4º dia', '5º dia']
    dias_dict = {}
    for dia in dias:
        dias_dict[dia] = df_abono_corrente[dia].iloc[0]

    sei = df_abono_corrente['SEI'].iloc[0]

    st.markdown("### Cadastro ou alteração de abono")

    n_abonos = col1.slider('Selecione quantos abonos quer preencher, incluindo os já cadastrados',
                         min_value = 0,
                         max_value =5,
                         step =1,
                         value = 0)

if n_abonos > 0:

    # Preenche formulário
    with st.form("Alterar Abono"):

        col1, col2, col3, col4, col5 = st.columns(5)
        columns = [col1, col2, col3, col4, col5]
       
        for i in range(n_abonos):
            dia = dias_dict[dias[i]]
            if not pd.isna(dia):
                nova_data = columns[i].date_input(dias[i], format='DD/MM/YYYY', value=dia)
            else:
                nova_data = columns[i].date_input(dias[i], format='DD/MM/YYYY')

            dias_dict[dias[i]] = nova_data


            # if dias_dict[dias[i]]:
            #     dias_dict[dias[i]] = col1.date_input(dias[i], format = 'DD/MM/YYYY', value = dias_dict[dias[i]])
            # else:
            #     dias_dict[dias[i]] = col1.date_input(dias[i], format = 'DD/MM/YYYY', value = hoje)

        sei = st.text_input('Processo SEI', value=sei)

        novo_abono = pd.DataFrame([         
            {   "Timestamp": datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
                "Matrícula SSP": matricula,
                "Ano do gozo": ano_ref,
                "1º dia": pd.to_datetime(dias_dict["1º dia"]).date() if dias_dict["1º dia"] else None, 
                "2º dia": pd.to_datetime(dias_dict["2º dia"]).date() if dias_dict["3º dia"] else None,
                "3º dia": pd.to_datetime(dias_dict["3º dia"]).date() if dias_dict["4º dia"] else None,
                "4º dia": pd.to_datetime(dias_dict["4º dia"]).date() if dias_dict["5º dia"] else None,
                "5º dia": pd.to_datetime(dias_dict["5º dia"]).date() if dias_dict["5º dia"] else None,
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






