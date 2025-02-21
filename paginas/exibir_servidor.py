import streamlit as st


# Carrega dados
dados = st.session_state['data']
df_servidores = dados['serv_total'] 
#df_servidores = dados['servidores'] 
df_ferias = dados['ferias']
df_abono = dados['abono']
df_afastamentos = dados['afastamentos']
df_cargos = dados['cargos']
exercicios = df_ferias['Exercício'].unique()

# Busca por nome

st.markdown('##### Selecione um servidor')

df_servidores['nome_busca'] = df_servidores["Posto ou Graduação"] + ' ' + df_servidores["Nome de Guerra (preferencial se civil)"] + ' - ' + df_servidores["Nome Completo"]
options = df_servidores['nome_busca'].to_list()
options.insert(0,'')

nome_busca = st.selectbox('Insira um nome para buscar', options = options)
if nome_busca == '':
    matricula = None
else:
    matricula = float(df_servidores[df_servidores['nome_busca']==nome_busca]['Matrícula na SSP'].iloc[0])

st.markdown('##### ou digite diretamente a matrícula')


# Input de matricula
matricula = st.number_input('Digite a matrícula do servidor', value=matricula, format='%.0f')

if st.button("Exibir dados") and matricula:
    
    # Backend
    servidor = df_servidores[df_servidores['Matrícula na SSP']==matricula]
    cargo = df_cargos[df_cargos['Ocupante']==matricula]
    
    #ferias_exercicio
    st.markdown(f'### {servidor['Posto ou Graduação'].iloc[0]} {servidor['Quadro QOBM/QBMG'].iloc[0]} {servidor['Nome de Guerra (preferencial se civil)'].iloc[0]}')
    st.markdown(f'**Matrícula:** {matricula:.0f}')
    st.markdown(f'**Nome Completo:** {servidor['Nome Completo'].iloc[0]}')
    
    col1, col2 = st.columns(2)
    col1.markdown('#### Dados funcionais')
    col1.markdown(f'**Cidade de Residência:** {servidor['Cidade'].iloc[0]}')
    col1.markdown(f'**Atividade Predominante:** {servidor['Atividade predominante'].iloc[0]}')
    col1.markdown(f'**Local de Trabalho:** {servidor['Local de Trabalho'].iloc[0]}')

    col2.markdown('#### Informações do cargo em comissão')
    


    if(cargo.shape[0]>0):
        col2.markdown(f'**Cargo:** {cargo["Cargo"].iloc[0]}')
        col2.markdown(f'**Setor:** {cargo["Setor"].iloc[0]}')
        col2.markdown(f'**SIGRH:** {cargo["SIGRH - FUNÇÃO (DEC 46.117)"].iloc[0]}')
        col2.markdown(f'**Gratificação:** {cargo["Gratificação"].iloc[0]}')
    else:
        col2.markdown('**O servidor não está nomeado em um cargo válido**')

    

    # Férias
    
    st.markdown('#### Férias')

    colunas = ['Exercício', '1º Período - início', '1º Período - último dia', '2º Período - início', '2º Período - último dia', '3º Período - início', '3º Período - último dia', 'SEI']
    st.dataframe(
        df_ferias[df_ferias['Matrícula SSP']==matricula][colunas].set_index('Exercício'),
        column_config = {
            'Exercício': st.column_config.NumberColumn(format = '%d'),
            '1º Período - início': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            '1º Período - último dia': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            '2º Período - início': st.column_config.DateColumn(format = 'DD/MM/YYY'),
            '2º Período - último dia': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            '3º Período - início': st.column_config.DateColumn(format = 'DD/MM/YYY'),
            '3º Período - último dia': st.column_config.DateColumn(format = 'DD/MM/YYYY')
        }
    )

    # Abono Anual

    st.markdown('#### Abono anual')

    colunas = ['Ano do gozo', '1º dia', '2º dia', '3º dia', '4º dia', '5º dia', 'SEI']
    st.dataframe(
        df_abono[df_abono['Matrícula SSP']==matricula][colunas].set_index('Ano do gozo'),
        column_config = {
            'Ano do gozo': st.column_config.NumberColumn(format = '%d'),
            '1º dia': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            '2º dia': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            '3º dia': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            '4º dia': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            '5º dia': st.column_config.DateColumn(format = 'DD/MM/YYYY')
            }
        )

    # Outros afastamentos registrados
    st.markdown('#### Outros afastamentos registrados')

    colunas = ['Tipo de afastamento', 'Primeiro dia de afastamento', 'Último dia de afastamento', 'Processo SEI']
    st.dataframe(
        df_afastamentos[df_afastamentos['Matrícula SSP']==matricula][colunas],
        column_config = {
            'Primeiro dia de afastamento': st.column_config.DateColumn(format = 'DD/MM/YYYY'),
            'Último dia de afastamento': st.column_config.DateColumn(format = 'DD/MM/YYYY')
        }
    )
