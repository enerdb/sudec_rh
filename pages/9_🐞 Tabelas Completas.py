import streamlit as st

st.set_page_config(
    page_title="Afastamentos",
    page_icon='🐞',
    layout = 'wide'
)

dados = st.session_state['data']

tabelas = [
    'servidores',
    'afastamentos',
    'ferias',
    'abono',
    'cargos',
    'gratificacao',
    'nom_invalid',
    'historico',
    'servidores_inv',
    'serv_total',
    'novo_abono'
]

for tabela in tabelas:
    st.markdown(f'## {tabela}')
    st.write(dados[tabela].columns.tolist())
    st.dataframe(dados[tabela].reset_index(drop=True))




# st.markdown('## Servidores')
# st.write(dados['servidores'].columns.tolist())
# st.dataframe(dados['servidores'])

# st.markdown('## Afastamentos')
# st.write(dados['afastamentos'].columns.tolist())
# st.dataframe(dados['afastamentos'])

# st.markdown('## Férias')
# st.write(dados['ferias'].columns.tolist())
# st.dataframe(dados['ferias'])

# st.markdown('## Abono Anual')
# st.write(dados['abono'].columns.tolist())
# st.dataframe(dados['abono'])

# st.markdown('## Cargos')
# st.write(dados['cargos'].columns.tolist())
# st.dataframe(dados['cargos'])

# st.markdown('## Gratificação')
# st.write(dados['gratificacao'].columns.tolist())
# st.dataframe(dados['gratificacao'])

# st.markdown('## Nomeações Inválidas')
# st.write(dados['nom_invalid'].columns.tolist())
# st.dataframe(dados['nom_invalid'])

# st.markdown('## Histórico de Servidores')
# st.write(dados['historico'].columns.tolist())
# st.dataframe(dados['historico'])

# st.markdown('## Histórico de Inválidos')
# st.write(dados['servidores_inv'].columns.tolist())
# st.dataframe(dados['servidores_inv'])

