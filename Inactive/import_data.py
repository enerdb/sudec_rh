# Substituida em 20/02/2025
def import_data():

    dados = {}

    # Extrai os dados

    sheet = get_sheet_from_drive('dados_rh')

    ## Carrega abono
    df = get_data_from_drive(sheet, 'abono')
    dados['abono'] = trata_abono_2sys(df)

    ## carrega servidores
    df = pd.read_csv(config.URL_SERVIDORES_NOMEADOS)
    dados['servidores'] = trata_servidor_2sys(df)

    ## carrega histórico de servidores
    df = pd.read_csv(config.URL_SERVIDORES_HISTORICO)
    dados['historico'] = trata_servidor_2sys(df)

    ## carrega outros afastamentos
    dados['afastamentos'] = pd.read_csv(config.URL_AFASTAMENTOS_NOVO) # ["Carimbo de data/hora", "Matrícula SSP", "Primeiro dia de afastamento", 'Último dia de afastamento", "Tipo de afastamento", "Processo SEI"]
    dados['afastamentos']['Primeiro dia de afastamento'] = pd.to_datetime(dados['afastamentos']['Primeiro dia de afastamento'], dayfirst=True).dt.date
    dados['afastamentos']['Último dia de afastamento'] = pd.to_datetime(dados['afastamentos']['Último dia de afastamento'], dayfirst=True).dt.date   
    
    ## carrega férias   
    dados['ferias'] = pd.read_csv(config.URL_FERIAS) # ["Chave", "Carimbo de data/hora", "Matrícula SSP", "Exercício", "1º Período - início", "1º Período - último dia", "2º Período - início", "2º Período - último dia", '3º Período - início", "3º Período - último dia", "SEI"]
    dados['ferias']['1º Período - início']      = pd.to_datetime(dados['ferias']['1º Período - início'], dayfirst=True).dt.date
    dados['ferias']['1º Período - último dia']  = pd.to_datetime(dados['ferias']['1º Período - último dia'], dayfirst=True).dt.date
    dados['ferias']['2º Período - início']      = pd.to_datetime(dados['ferias']['2º Período - início'], dayfirst=True).dt.date
    dados['ferias']['2º Período - último dia']  = pd.to_datetime(dados['ferias']['2º Período - último dia'], dayfirst=True).dt.date
    dados['ferias']['3º Período - início']      = pd.to_datetime(dados['ferias']['3º Período - início'], dayfirst=True).dt.date
    dados['ferias']['3º Período - último dia']  = pd.to_datetime(dados['ferias']['3º Período - último dia'], dayfirst=True).dt.date
    dados['ferias']['Chave']                    = dados['ferias']['Chave'].astype('int32')
    
    ## carrega cargos  
    dados['cargos'] = pd.read_csv(config.URL_CARGOS) # ["ID", "CARGO EM COMISSÃO", "Cargo", "Setor", "SIGRH - FUNÇÃO (DEC 46.117)", "Gratificação", "NC_padronizado", "Seq", "Ocupante"]
    
    ## carrega gratificações
    dados['gratificacao'] = pd.read_csv(config.URL_GRATIFICACAO) # ["Gratificação", "Salário"]
    
    ## carrega nomeações invalidas
    dados['nom_invalid'] = pd.read_csv(config.URL_NOM_INVALID) # ['Matrícula SSP','Cargo','GRATIFICAÇÃO', 'SETOR', 'Data de nomeação', 'Data_min_exon']
    dados['servidores_inv'] = dados['historico'][dados['historico']["Matrícula na SSP"].isin(dados['nom_invalid']['Matrícula SSP'])]

    ## integra servidores nomeados + historico
    dados['serv_total'] = pd.concat([dados['servidores'], dados['servidores_inv']], ignore_index = True)
    dados['serv_total'] = dados['serv_total'][~dados['serv_total']['Matrícula na SSP'].duplicated(keep='first')]
    
    ## gera df de servidores inválidos
    matriculas_to_drop = dados['servidores']['Matrícula na SSP']
    dados['servidores_inv'] = dados['serv_total'][~dados['serv_total']['Matrícula na SSP'].isin(matriculas_to_drop)]


    # Gera DF de dias com afastamento
    ## Formato: Matricula, Dia afastado, Motivo

    ## Afastamentos gerais
    lista_afast = []
    for _, row in dados['afastamentos'].iterrows():
        append_dias_afast(lista_afast, row['Primeiro dia de afastamento'], row['Último dia de afastamento'], row['Tipo de afastamento'], row['Matrícula SSP'])

    ## Férias
    for _, row in dados['ferias'].iterrows():
        append_dias_afast(lista_afast, row['1º Período - início'], row['1º Período - último dia'], 'Férias', row['Matrícula SSP'])
        append_dias_afast(lista_afast, row['2º Período - início'], row['2º Período - último dia'], 'Férias', row['Matrícula SSP'])
        append_dias_afast(lista_afast, row['3º Período - início'], row['3º Período - último dia'], 'Férias', row['Matrícula SSP'])
        
    ## Abono anual
    cols = ['1º dia', '2º dia', '3º dia', '4º dia', '5º dia']
    for _, row in dados['abono'].iterrows():
        for dia in cols:
            if not pd.isna(row[dia]):
                lista_afast.append({'Matrícula': row['Matrícula SSP'], 'Dia': row[dia].strftime("%Y-%m-%d"), 'Motivo': 'Abono anual'})
        
    ## Totalização
    dados['dias_afastamento'] = pd.DataFrame(lista_afast)
    dados['dias_afastamento']['Dia'] = pd.to_datetime(dados['dias_afastamento']['Dia'], format="%Y-%m-%d").dt.date

    return dados