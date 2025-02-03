import streamlit as st
import pandas as pd
from datetime import datetime
from time import sleep


st.set_page_config(
    page_title="Inserir dados",
    page_icon='✏',
    layout = 'wide'
)

st.markdown("""
            # ESSA PÁGINA AINDA NÃO ESTÁ FUNCIONANDO
            # FAVOR NÃO UTILIZAR AINDA
            """)

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
matricula = col1.number_input('Digite a matrícula SSP do servidor', value=None, format='%.0f')
ano_ref = col1.selectbox('Ano de referência', [2024 + i for i in range(10)])


if matricula:
    servidor = df_servidores[df_servidores['Matrícula na SSP']==matricula]
    col1.markdown(f'**Nome Completo:** {servidor['Nome Completo'].iloc[0]}')

if matricula and ano_ref:
    colunas = ['Ano do gozo', '1º dia', '2º dia', '3º dia', '4º dia', '5º dia', 'SEI']

    df_abono_corrente = df_abono[df_abono['Matrícula SSP']==matricula][df_abono['Ano do gozo']==ano_ref][colunas].set_index('Ano do gozo')

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

    # Fomrmulário de alteração de abono
    st.markdown("### Cadastro ou alteração de abono")
    
    # Inicializa variáveis com os valores atuais.
    if df_abono_corrente.shape[0] == 0 :
        df_abono_corrente.loc[ano_ref] = [None, None, None, None, None, None]
    dia1 = df_abono_corrente['1º dia'].iloc[0]
    dia2 = df_abono_corrente['2º dia'].iloc[0]
    dia3 = df_abono_corrente['3º dia'].iloc[0]
    dia4 = df_abono_corrente['4º dia'].iloc[0]
    dia5 = df_abono_corrente['5º dia'].iloc[0]
    sei = df_abono_corrente['SEI'].iloc[0]
        
    # Preenche formulário
    with st.form("Alterar Abono"):

        col1, col2, col3, col4, col5 = st.columns(5)
        
        dia1 = col1.date_input('1º dia', format = 'DD/MM/YYYY', value = dia1)
        dia2 = col2.date_input('2º dia', format = 'DD/MM/YYYY', value = dia2)
        dia3 = col3.date_input('3º dia', format = 'DD/MM/YYYY', value = dia3)
        dia4 = col4.date_input('4º dia', format = 'DD/MM/YYYY', value = dia4)
        dia5 = col5.date_input('5º dia', format = 'DD/MM/YYYY', value = dia5)
        sei = st.text_input('Processo SEI', value=sei)
        novo_abono = pd.Series({"Chave": f'{matricula}{ano_ref}',
                "Carimbo de data/hora": datetime.now(),
                "Matrícula SSP": matricula,
                "Ano do gozo": ano_ref,
                "1º dia": dia1,
                "2º dia": dia2,
                "3º dia": dia3,
                "4º dia": dia4,
                "5º dia": dia5,
                "SEI": sei}).to_frame().T
        submit = st.form_submit_button('Enviar dados')
        
    if submit:
        st.session_state['data']['abono'] = pd.concat([df_abono, novo_abono], ignore_index=True)
        st.success("Dados enviados com sucesso")






