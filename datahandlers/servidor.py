import pandas as pd

#["Matrícula na SSP","Nome Completo","Nome de Guerra (preferencial se civil)","Efetividade","Posto ou Graduação","Quadro QOBM/QBMG","Cidade","Sexo", "Horário de trabalho", "Atividade predominante", "Local de Trabalho"]


def trata_servidor_2sys(df):
    postos_dict = {
    'Coronel': 1,
    'Tenente Coronel':2,
    'Major' : 3,
    'Capitão' : 4,
    '1º Tenente' : 5, 
    '2º Tenente' : 6,
    'Subtenente' : 7,
    '1º Sargento': 8,
    '2º Sargento' : 9,
    '3º Sargento' : 10,
    'Cabo': 11,
    'Soldado': 12,
    'Agente Civil': 13
    }
    
    df['Nome Completo']            = df['Nome Completo'].str.upper()
    df["Nome de Guerra (preferencial se civil)"]            = df["Nome de Guerra (preferencial se civil)"].str.upper()
    df['Posto ou Graduação']       = df['Posto ou Graduação'].fillna('')
    df['Quadro QOBM/QBMG']         = df['Quadro QOBM/QBMG'].fillna('')
    df['Efetividade']              = df['Efetividade'].fillna('')
    df['Cidade']                   = df['Cidade'].fillna('')
    df['Sexo']                     = df['Sexo'].fillna('')
    df['Horário de trabalho']      = df['Horário de trabalho'].fillna('')
    df['Atividade predominante']   = df['Atividade predominante'].fillna('')
    df['Local de Trabalho']        = df['Local de Trabalho'].fillna('')
    df['Matrícula na SSP']         = df['Matrícula na SSP'].astype('int32')
    df['Antiguidade']              = df['Posto ou Graduação'].map(postos_dict).fillna(14)

    return df

def trata_servidor_2drive(df):
    pass

def filter_servidor_by_matricula(df, matricula):
    return df[df["Matrícula na SSP"]==matricula]

def concat_servidor(df1, df2):
    pass
