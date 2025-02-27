import streamlit as st



#####################
# CARREGANDO DADOS
#####################

dados = st.session_state['data']

df_invalidos = dados['servidores_inv']
#["Matrícula na SSP","Nome Completo","Nome de Guerra (preferencial se civil)","Efetividade","Posto ou Graduação","Quadro QOBM/QBMG","Cidade","Sexo", "Horário de trabalho", "Atividade predominante", "Local de Trabalho"]

matr_inv = df_invalidos['Matrícula na SSP']


df_nom_invalid = dados['nom_invalid'] # ['Matrícula SSP','Cargo','GRATIFICAÇÃO', 'SETOR', 'Data de nomeação', 'Data_min_exon']
df_nom_invalid = df_nom_invalid[df_nom_invalid['Matrícula SSP'].isin(matr_inv)]


df_cargos = dados['cargos']

#####################
# TRANSFORMANDO DADOS
#####################

df_pend = df_nom_invalid.merge(df_invalidos, left_on='Matrícula SSP', right_on = 'Matrícula na SSP')
columns_pend = ['Matrícula SSP', 'Nome Completo', 'Cargo', 'SETOR', 'GRATIFICAÇÃO', 'Data de nomeação' ]
columns_cargos = ['Cargo', 'Setor', 'Gratificação']


#####################
# EXIBIÇÃO
#####################

if df_pend.shape[0] == 0:
    st.markdown('### Não há pendências no cadastro dos cargos')

    st.markdown('#### Cargos Previstos')
    st.dataframe(df_cargos[columns_cargos])

else:
    st.markdown('### Os servidores abaixo não estão nomeados em cargos válidos ou alguém foi nomeado em seus cargos')

    col1, col2 = st.columns([3,2])

    col1.markdown('#### Servidores')
    col1.dataframe(df_pend[columns_pend],
        column_config = {
            'Matrícula SSP': st.column_config.NumberColumn(format = '%d')
        }) 

    col2.markdown('#### Cargos Previstos')
    col2.dataframe(df_cargos[columns_cargos])