import streamlit as st

st.set_page_config(
    page_title="Servidores",
    page_icon='📄',
    layout = 'wide'
)

dados = st.session_state['data']
df_servidores = dados['servidores']
df_ferias = dados['ferias']
df_abono = dados['abono']
df_afastamentos = dados['afastamentos']


exercicios = df_ferias['Exercício'].unique()

matricula = st.number_input('Digite a matrícula do servidor', value=None, format='%i')

if st.button("Exibir dados"):
    
    # Backend
    servidor = df_servidores[df_servidores['Matrícula na SSP']==matricula]
    #ferias_exercicio = 



    st.markdown(f'### {servidor['Posto ou Graduação'].iloc[0]} {servidor['Quadro QOBMG/QBMG'].iloc[0]} {servidor['Nome de Guerra (preferencial se civil)'].iloc[0]} ')
    st.write(f'Matrícula: {matricula}')
    st.write(f'Nome Completo: {servidor['Nome Completo'].iloc[0]}')
    st.write(f'Cidade de Residência: {servidor['Cidade'].iloc[0]}')
    st.write(f'Atividade Predominante: {servidor['Atividade predominante'].iloc[0]}')
    st.write(f'Local de Trabalho: {servidor['Local de Trabalho'].iloc[0]}')

    # Férias
    
    st.markdown('#### Férias')

    colunas = ['Exercício', '1º Período - início', '1º Período - último dia', '2º Período - início', '2º Período - último dia', '3º Período - início', '3º Período - último dia', 'SEI']
    st.dataframe(df_ferias[df_ferias['Matrícula SSP']==matricula][colunas].set_index('Exercício'))

    # Abono Anual

    st.markdown('#### Abono anual')

    colunas = ['Ano do gozo', '1º dia', '2º dia', '3º dia', '4º dia', '5º dia', 'SEI']
    st.dataframe(df_abono[df_abono['Matrícula SSP']==matricula][colunas].set_index('Ano do gozo'))

    # Outros afastamentos registrados
    st.markdown('#### Outros afastamentos registrados')

    colunas = ['Tipo de afastamento', 'Primeiro dia de afastamento', 'Último dia de afastamento', 'Processo SEI']
    st.dataframe(df_afastamentos[df_afastamentos['Matrícula SSP']==matricula][colunas])



    



#st.dataframe(df_data)