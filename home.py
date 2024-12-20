import pandas as pd
import streamlit as st
from datetime import datetime

########################################
# LAYOUT CONFIG
########################################

st.set_page_config(
    page_title="Servidores",
    page_icon='👨‍👦‍👦',
    layout = 'wide'
)

st.sidebar.markdown("Dúvidas? Tratar com TC Beckmann")

########################################
# FUNÇÕES
########################################

## Função para criar ranges de dias de afastamento
def append_dias_afast(lista, dia1, diau, motivo, matricula):
    if not (pd.isnull(dia1) or pd.isnull(diau)):
        date_range = pd.period_range(start=dia1, end=diau)
        for single_date in date_range:
            lista.append({'Matrícula': matricula, 'Dia': single_date, 'Motivo': motivo})

# Importação e tratamento de dados do google sheets
def import_data():
    url_servidores_historico = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5KNQ_JF9dR3R-utwPgBMlMLjr30nkKZh2eyryt-1yvr25afKWbfT_WMR2Ks7hk5agdLMlhrAUTqb9/pub?gid=724592700&single=true&output=csv'
    url_servidores_nomeados = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5KNQ_JF9dR3R-utwPgBMlMLjr30nkKZh2eyryt-1yvr25afKWbfT_WMR2Ks7hk5agdLMlhrAUTqb9/pub?gid=1024672305&single=true&output=csv'
    url_salarios = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQz_rr0axyr_VQ0HgYseWkqwKBHTumQz7AFjLolLqLRVyobeYlqn6eJzKFvuKa_k5BJO3FLikXxuVT9/pub?gid=1631165264&single=true&output=csv'
    url_cargos = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQz_rr0axyr_VQ0HgYseWkqwKBHTumQz7AFjLolLqLRVyobeYlqn6eJzKFvuKa_k5BJO3FLikXxuVT9/pub?gid=0&single=true&output=csv'
    url_afastamentos = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS0ViaRdmnFJh5VMrAuA9kYI_gqvCQkuWNNL3HuKwPMpBR2yDgHKOgduCN4Q1I0MQ1XA9QuTT90-94c/pub?gid=823536189&single=true&output=csv'
    url_dias_afastamento = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS0ViaRdmnFJh5VMrAuA9kYI_gqvCQkuWNNL3HuKwPMpBR2yDgHKOgduCN4Q1I0MQ1XA9QuTT90-94c/pub?gid=433320192&single=true&output=csv'

    url_afastamentos_novo = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS0ViaRdmnFJh5VMrAuA9kYI_gqvCQkuWNNL3HuKwPMpBR2yDgHKOgduCN4Q1I0MQ1XA9QuTT90-94c/pub?gid=1934526132&single=true&output=csv'
    url_abono = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS0ViaRdmnFJh5VMrAuA9kYI_gqvCQkuWNNL3HuKwPMpBR2yDgHKOgduCN4Q1I0MQ1XA9QuTT90-94c/pub?gid=144957376&single=true&output=csv'
    url_ferias = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS0ViaRdmnFJh5VMrAuA9kYI_gqvCQkuWNNL3HuKwPMpBR2yDgHKOgduCN4Q1I0MQ1XA9QuTT90-94c/pub?gid=215396885&single=true&output=csv'

    dados = {}

    # Extrai os dados
    dados['servidores'] = pd.read_csv(url_servidores_nomeados)
    dados['afastamentos'] = pd.read_csv(url_afastamentos_novo)
    dados['ferias'] = pd.read_csv(url_ferias)
    dados['abono'] = pd.read_csv(url_abono)
    
    st.write('Dados extraídos da internet. Tratando dados')
    # Conversão de tipos

    dados['afastamentos']['Primeiro dia de afastamento'] = pd.to_datetime(dados['afastamentos']['Primeiro dia de afastamento'], dayfirst=True).dt.date
    dados['afastamentos']['Último dia de afastamento'] = pd.to_datetime(dados['afastamentos']['Último dia de afastamento'], dayfirst=True).dt.date
    dados['abono']['1º dia'] = pd.to_datetime(dados['abono']['1º dia'], dayfirst=True).dt.date
    dados['abono']['2º dia'] = pd.to_datetime(dados['abono']['2º dia'], dayfirst=True).dt.date
    dados['abono']['3º dia'] = pd.to_datetime(dados['abono']['3º dia'], dayfirst=True).dt.date
    dados['abono']['4º dia'] = pd.to_datetime(dados['abono']['4º dia'], dayfirst=True).dt.date
    dados['abono']['5º dia'] = pd.to_datetime(dados['abono']['5º dia'], dayfirst=True).dt.date
    dados['ferias']['1º Período - início'] = pd.to_datetime(dados['ferias']['1º Período - início'], dayfirst=True).dt.date
    dados['ferias']['1º Período - último dia'] = pd.to_datetime(dados['ferias']['1º Período - último dia'], dayfirst=True).dt.date
    dados['ferias']['2º Período - início'] = pd.to_datetime(dados['ferias']['2º Período - início'], dayfirst=True).dt.date
    dados['ferias']['2º Período - último dia'] = pd.to_datetime(dados['ferias']['2º Período - último dia'], dayfirst=True).dt.date
    dados['ferias']['3º Período - início'] = pd.to_datetime(dados['ferias']['3º Período - início'], dayfirst=True).dt.date
    dados['ferias']['3º Período - último dia'] = pd.to_datetime(dados['ferias']['3º Período - último dia'], dayfirst=True).dt.date

    # Gera DF de dias com afastamento
    ## Formato
    ### Matricula, Dia afastado, Motivo

    ## Afastamentos gerais
    lista_afast = []
    for _, row in dados['afastamentos'].iterrows():
        append_dias_afast(lista_afast, row['Primeiro dia de afastamento'], row['Último dia de afastamento'], row['Tipo de afastamento'], row['Matrícula SSP'])

    ## Férias
    for _, row in dados['ferias'].iterrows():
        append_dias_afast(lista_afast, row['1º Período - início'], row['1º Período - último dia'], 'Férias', row['Matrícula SSP'])
        append_dias_afast(lista_afast, row['2º Período - início'], row['2º Período - último dia'], 'Férias', row['Matrícula SSP'])
        append_dias_afast(lista_afast, row['3º Período - início'], row['3º Período - último dia'], 'Férias', row['Matrícula SSP'])
    

    ## Afastamentos gerais
#       if not (pd.isnull(row['Primeiro dia de afastamento']) and pd.isnull(row['Último dia de afastamento'])):
#            date_range = pd.date_range(start=row['Primeiro dia de afastamento'], end=row['Último dia de afastamento'])
#            for single_date in date_range:
#                expanded_rows.append({'Matrícula': row['Matrícula SSP'], 'Dia': single_date, 'Motivo': row['Tipo de afastamento']})
    
    ## Férias


#    for _, row in dados['ferias'].iterrows():
#        date_range = pd.date_range(start=row['1º Período - início'], end=row['1º Período - último dia'])
#        for single_date in date_range:
#            expanded_rows.append({'Matrícula': row['Matrícula SSP'], 'Dia': single_date, 'Motivo': 'Férias'})
#
#        date_range = pd.date_range(start=row['2º Período - início'], end=row['2º Período - último dia'])
#        for single_date in date_range:
#            expanded_rows.append({'Matrícula': row['Matrícula SSP'], 'Dia': single_date, 'Motivo': 'Férias'})
#
#        date_range = pd.date_range(start=row['3º Período - início'], end=row['3º Período - último dia'])
#        for single_date in date_range:
#            expanded_rows.append({'Matrícula': row['Matrícula SSP'], 'Dia': single_date, 'Motivo': 'Férias'})
    
    ## Abono anual
    for _, row in dados['abono'].iterrows():
        #append_dias_afast(lista_afast, dados['abono']['1º dia'], dados['abono']['1º dia'], 'Abono anual', row['Matrícula SSP'])
        #append_dias_afast(lista_afast, dados['abono']['1º dia'], dados['abono']['2º dia'], 'Abono anual', row['Matrícula SSP'])
        #append_dias_afast(lista_afast, dados['abono']['1º dia'], dados['abono']['3º dia'], 'Abono anual', row['Matrícula SSP'])
        #append_dias_afast(lista_afast, dados['abono']['1º dia'], dados['abono']['4º dia'], 'Abono anual', row['Matrícula SSP'])
        #append_dias_afast(lista_afast, dados['abono']['1º dia'], dados['abono']['5º dia'], 'Abono anual', row['Matrícula SSP'])



        lista_afast.append({'Matrícula': row['Matrícula SSP'], 'Dia': dados['abono']['1º dia'].iloc[0].strftime("%Y-%m-%d"), 'Motivo': 'Abono anual'})
        lista_afast.append({'Matrícula': row['Matrícula SSP'], 'Dia': dados['abono']['2º dia'].iloc[0].strftime("%Y-%m-%d"), 'Motivo': 'Abono anual'})
        lista_afast.append({'Matrícula': row['Matrícula SSP'], 'Dia': dados['abono']['3º dia'].iloc[0].strftime("%Y-%m-%d"), 'Motivo': 'Abono anual'})
        lista_afast.append({'Matrícula': row['Matrícula SSP'], 'Dia': dados['abono']['4º dia'].iloc[0].strftime("%Y-%m-%d"), 'Motivo': 'Abono anual'})
        lista_afast.append({'Matrícula': row['Matrícula SSP'], 'Dia': dados['abono']['5º dia'].iloc[0].strftime("%Y-%m-%d"), 'Motivo': 'Abono anual'})

    ## Totalização
    st.write('Convertendo datas')
    dados['dias_afastamento'] = pd.DataFrame(lista_afast)
    dados['dias_afastamento']['Dia'] = pd.to_datetime(dados['dias_afastamento']['Dia'], format="%Y-%m-%d").dt.date

    st.sidebar.markdown("Dados atualizados em")
    st.sidebar.markdown(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}")
    return dados


########################################
# 
########################################

if "data" not in st.session_state:
    dados = import_data()
    st.session_state['data'] = dados


st.markdown("# CONTROLE DE SERVIDORES DA SUDEC 👨‍👦‍👦")

st.link_button("Caso tenha acesso, acesse a planilha completa no Google", "https://docs.google.com/spreadsheets/d/1eQ5PXgKFeKUFibGWYWA3QzKGFB9HUNHguO2Cixtypt4/edit?gid=0#gid=0")

if st.button("Atualizar dados"):
    st.write('Solicitação de atualização feita')
    dados = import_data()
    st.session_state['data'] = dados
    st.write('Dados Atualizados')





#streamlit run home.py



