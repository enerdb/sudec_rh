######################################
# Orientações
# Fazer esse cadastro já pensando no modelo de dados novos
# Quando estiver tudo funcionando, migrar dados antigos.
# 
######################################

######################################
# Imports
import streamlit as st
import config
from datamodels.sudec_rh_classes import Servidor

##################
#  Helper functions

def seleciona_servidor_input(df):
    st.markdown('##### Selecione um servidor')
    
    df['posto_busca'] = df['posto'].map(config.POSTO_SHORT_NAME)
    df['nome_busca'] = df["posto_busca"] + ' ' + df["nome_guerra"] + ' - ' + df["nome"]
    options = df['nome_busca'].to_list()
    options.insert(0,'')

    nome_busca = st.selectbox('Insira um nome para buscar', options = options)
    if nome_busca == '':
        matricula = None
    else:
        matricula = float(df[df['nome_busca']==nome_busca]['matricula'].iloc[0])

    st.markdown('##### ou digite diretamente a matrícula')

    # Input de matricula
    matricula = st.number_input('Digite a matrícula do servidor', value=matricula, format='%.0f')

    # limpa dados
    df.drop(columns = ['nome_busca', 'posto_busca'])

    return matricula

def prepara_lista_select(lista, dado_old):
    
    if (dado_old) and (dado_old in lista):
        lista.remove(dado_old)
        lista.insert(0, dado_old)
    return lista

##################
#  Carrega dados
df_pessoas = st.session_state['data']['pessoas']


#  Seleciona servidor para alterar
matricula = seleciona_servidor_input(df_pessoas)

# Flag para alterar dados confidenciais
alterar_confidenciais = st.checkbox("Incluir ou alterar dados confidenciais")
st.write("Para proteção dos usuários, os dados confidenciais cadastrados anteriormente não serão exibidos nesta tela")

# Formulário
if matricula:

    servidor = df_pessoas[df_pessoas["matricula"]==matricula].iloc[0]
    
    if servidor.shape[0]==0:
        st.error('Matrícula não encontrada')
    else:
        nome = servidor['nome']
        nome_guerra = servidor["nome_guerra"]
        efetividade = servidor["militar"]
        posto = servidor["posto"]
        quadro = servidor["quadro"]
        cidade = servidor["cidade"]
        sexo_fem = servidor['sexo_fem']
        siape = servidor['siape']
        horario_manha = servidor['horario_manha']
        atividade = servidor['atividade']
        local_trab = servidor['local_trab']
    
        with st.form("Alterar Cadastro de Servidor"):
        
            nome     = st.text_input('Nome completo', value=nome)
            nome_guerra = st.text_input('Nome de guerra', value=nome_guerra)
            militar = st.checkbox('Militar', value = servidor['militar'])
            posto = st.selectbox('Posto ou graduação', prepara_lista_select(config.LISTA_POSTOS,posto))
            quadro = st.selectbox('Quadro', prepara_lista_select(config.LISTA_QUADROS,quadro))     
            cidade = st.selectbox('Cidade', prepara_lista_select(config.LISTA_CIDADES,cidade))   
            sexo = st.selectbox('Sexo', prepara_lista_select(['Masculino', 'Feminino'], sexo_fem)) # ajustar listas.
            
            siape = st.number_input('Siape', value=siape)
            horario_manha = st.selectbox('Horário de trabalho', prepara_lista_select(['Manhã', 'Tarde']), horario_manha )
            atividade = st.selectbox('Atividade Predominante', prepara_lista_select([''], atividade))
            local_trab = st.selectbox('Local de Trabalho', prepara_lista_select([''], local_trab))

            # Pensar em uma forma de manter os dados caso queira alterar alguns.
            if alterar_confidenciais:
                cpf = st.number_input('CPF - apenas números',step = 1, value = None)
                endereco = st.text_input('Endereço')
                cep = st.text_input('CEP')
                fone1 = st.text_input('Telefone 1')
                fone2 = st.text_input('Telefone 2')
                emaili = st.text_input('e-mail institucional')
                emailp = st.text_input('e-mail particular')
                tipo_sang = st.text_input('Tipo sanguíneo')
                fator_rh = st.text_input('Fator RH')
                emergenc_cont = st.text_input('Contato de emergência')
                alergias = st.text_input('Alergias')
                outr_cond = st.text_input('Outra condição de saúde a considerar')

            submit = st.form_submit_button('Enviar dados')

        if submit:
            novo_servidor = Servidor(
                matricula = matricula,
                nome = nome,
                nome_guerra = nome_guerra,
                militar = militar,
                posto = posto,
                quadro = quadro,
                siape = siape
            )

            st.write(novo_servidor.model_dump())

            st.success('Novos dados impressos com Sucesso')
            st.error('O Cadastro no sistema não foi realizado')


