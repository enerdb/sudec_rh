import streamlit as st

########################################
# LAYOUT CONFIG
########################################

#st.set_page_config(layout = 'wide')


########################################
# PAGES CONFIG
########################################

pages = {
    "Geral": [
        st.Page("paginas/inicio.py",                title="Início", icon = '🏠'),
    ],
    "Visualizar": [
        st.Page("paginas/exibir_servidores.py",     title="Servidores", icon = '👨‍👦‍👦'),
        st.Page("paginas/exibir_cargos.py",         title="Cargos", icon = '👮‍♂️'),
        st.Page("paginas/exibir_servidor.py",       title="Exibir Servidor", icon = '👨'),
        st.Page("paginas/exibir_afastamentos.py",   title="Exibir Afastamentos", icon = '🏖'),
        st.Page("paginas/exibir_pendencias.py",     title="Pendências", icon = '⚠'),
    ],
    "Cadastrar ou Alterar": [
        st.Page("paginas/cadastro_novo_servidor.py",title="Novo Servidor"),
        st.Page("paginas/cadastro_alterar_servidor.py",     title="Alterar dados servidor"),
        st.Page("paginas/cadastro_abono.py",        title="Abono anual"),
        st.Page("paginas/cadastros_google.py",      title="Outros cadastros"),
    ],
    "Adm:" :[
        st.Page("paginas/adm_tabelas.py", title = "Debug Tabelas"),
        st.Page("paginas/adm_import_servidores.py", title="Import Servidores")
    ]
}

pg = st.navigation(pages)
pg.run()



########################################
# COMMANDS
########################################
# Set-ExecutionPolicy Unrestricted -Scope Process
# venv\Scripts\Activate.ps1
# streamlit run home.py



