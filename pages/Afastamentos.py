import streamlit as st

st.set_page_config(
    page_title="Afastamentos",
    page_icon='🏖',
    layout = 'wide'
)

#####################
# CARREGANDO DADOS
#####################

dados = st.session_state['data']
df_afastamentos = dados['dias_afastamento']
df_servidores = dados['servidores']

dia = st.date_input('Insira a data a ser verificada')


if st.button("Exibir dados"):
    
    st.write(f"Servidores afastados no dia {dia}")
       
    afastamentos_dia = df_afastamentos[df_afastamentos['Dia']==dia]
    lista_servidores_afastados = afastamentos_dia['Matrícula'].to_list()

    st.write(f"Matrículas afastadas: {lista_servidores_afastados}")

    df_servidores_afastados = df_servidores[df_servidores['Matrícula na SSP'].isin(lista_servidores_afastados)]
    df_servidores_disponiveis = df_servidores[~df_servidores['Matrícula na SSP'].isin(lista_servidores_afastados)]


    
    st.markdown(f'#### Servidores afastados em {dia}')
    st.dataframe(df_servidores_afastados)

    st.markdown(f'#### Servidores disponíves em {dia}')
    st.dataframe(df_servidores_disponiveis)






#st.dataframe(df_afastamentos)

#st.write(df_afastamentos['Dia'].dtypes)

#for evento in eventos:
#      
#    inicio = new Date(datasIniciais[i][0])
#    fim = new Date(datasFinais[i][0])
# 
#    for (var data = new Date(inicio); data <= fim; data.setDate(data.getDate() + 1)):
#        resultado.push([evento, new Date(data)])
          


# Formato da saída:


#Matricula, # Dia afastado, Motivo

#df = pd.concat([pd.DataFrame([[1,2]], columns=df.columns), df], ignore_index=True)