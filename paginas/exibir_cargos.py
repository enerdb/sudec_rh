import streamlit as st
import config


#####################
# CARREGANDO DADOS
#####################

dados = st.session_state['data']

cargos_columns = ['Cargo', 'Setor', 'SIGRH - FUNÇÃO (DEC 46.117)', 'Gratificação', 'Salário', 'Ocupante']
df_cargos = dados['cargos']
df_gratificacao = dados['gratificacao']
df_cargos = df_cargos.merge(df_gratificacao, on = 'Gratificação')[cargos_columns]




#servidores_columns = ['Matrícula na SSP', 'Posto ou Graduação', 'Quadro QOBM/QBMG', 'Nome de Guerra (preferencial se civil)', 'Nome Completo', 'Antiguidade']
servidores_columns = ['Matrícula na SSP', 'Posto ou Graduação', 'Quadro QOBM/QBMG', 'Nome de Guerra (preferencial se civil)', 'Nome Completo', 'Antiguidade']
df_servidores = dados['serv_total'][['matricula'] + config.SERV_COLUNAS_DISPLAY].set_index('matricula')

#####################
# FILTROS
#####################


# Lista Setores
setores = df_cargos['Setor'].unique()

# Multiselect
setores_selected = st.sidebar.multiselect('Filtrar por Setor de Nomeação', setores, placeholder = 'Selecione os Setores')

# Inclui todos os servidores se não houver seleção
if not setores_selected:
    setores_selected = setores

#Segmenta DF com base na seleção
df_cargos_setor = df_cargos[df_cargos['Setor'].isin(setores_selected)]

#### FILTO CARGO ####

# Lista Cargos
cargos = df_cargos['Cargo'].unique()

# Multiselect
cargos_selected = st.sidebar.multiselect('Filtrar por Cargo', cargos, placeholder = 'Selecione os Cargos')

# Inclui todos os servidores se não houver seleção
if not cargos_selected:
    cargos_selected = cargos

#Segmenta DF com base na seleção
df_cargos_cargos = df_cargos_setor[df_cargos_setor['Cargo'].isin(cargos_selected)]


df_cargos_filtrado = df_cargos_cargos

#####################
# MERGE
#####################
df_cargos_ocupados = df_cargos_filtrado.merge(df_servidores, left_on = 'Ocupante', right_on = 'matricula')
df_cargo_vagos = df_cargos_filtrado[df_cargos_filtrado['Ocupante'].isna()].drop(columns = ['Ocupante'])

#####################
# EXIBIÇÃO DE CARGOS
#####################

df_cargos_ocupados = df_cargos_ocupados.reset_index(drop=True)
df_cargos_ocupados.index +=1

df_cargo_vagos = df_cargo_vagos.reset_index(drop=True)
df_cargo_vagos.index +=1

df_display = df_cargos_ocupados

df_display['posto'] = df_display['posto'].map(config.POSTO_SHORT_NAME).fillna('')

st.markdown('### Cargos Ocupados')
st.dataframe(df_cargos_ocupados,
             column_config = {
                 'SIGRH - FUNÇÃO (DEC 46.117)': st.column_config.NumberColumn(format = '%d'),
                 'Ocupante': st.column_config.NumberColumn(format = '%d'),
                 'militar' :st.column_config.CheckboxColumn()
             }
)
             
st.markdown('### Cargos Vagos')
st.dataframe(df_cargo_vagos,
             column_config = {
                 'SIGRH - FUNÇÃO (DEC 46.117)': st.column_config.NumberColumn(format = '%d'),
                 'Ocupante': st.column_config.NumberColumn(format = '%d')
             }
)



#st.markdown('### Cargos')
#st.dataframe(df_cargos_filtrado)

#st.markdown('### Todos os Servidores')
#st.dataframe(df_servidores)
