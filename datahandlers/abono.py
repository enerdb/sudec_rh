import pandas as pd

#url_abono = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vS0ViaRdmnFJh5VMrAuA9kYI_gqvCQkuWNNL3HuKwPMpBR2yDgHKOgduCN4Q1I0MQ1XA9QuTT90-94c/pub?gid=144957376&single=true&output=csv'

def trata_abono_2sys(df):
    # ['Timestamp','Matrícula SSP', 'Ano do gozo', '1º dia', '2º dia', '3º dia', '4º dia', '5º dia', 'SEI']

    df['Timestamp'] = pd.to_datetime(df['Timestamp'], dayfirst=True)
    df['Matrícula SSP'] = df['Matrícula SSP']
    df['1º dia'] = pd.to_datetime(df['1º dia'], dayfirst=True)
    df['2º dia'] = pd.to_datetime(df['2º dia'], dayfirst=True)
    df['3º dia'] = pd.to_datetime(df['3º dia'], dayfirst=True)
    df['4º dia'] = pd.to_datetime(df['4º dia'], dayfirst=True)
    df['5º dia'] = pd.to_datetime(df['5º dia'], dayfirst=True)
    return df

def trata_abono_2drive(df):
    
    #df2drive = df
    df2drive = pd.DataFrame()
    df2drive['Timestamp'] = df['Timestamp'].dt.strftime('%d/%m/%Y %H:%M:%S')
    df2drive['Matrícula SSP'] = df['Matrícula SSP']
    df2drive['Ano do gozo'] = df['Ano do gozo']
    daycols = ["1º dia", "2º dia", "3º dia", "4º dia", "5º dia"]
    for col in daycols:
        df2drive[col] = df[col].dt.strftime('%d/%m/%Y')
    df2drive['SEI'] = df['SEI']
    df2drive = df2drive.fillna('')

    return df2drive
     
def filter_abono_by_matricula_ano(df, matricula, ano):
    return df[(df['Matrícula SSP']==matricula) & (df['Ano do gozo']==ano)]



def concat_abonos(df1, df2):
    df = pd.concat([df1, df2], ignore_index=True)

    # Agrupar pelos campos desejados e manter apenas o registro com maior Timestamp
    df_sorted = df.sort_values(by=["Timestamp"], ascending=False)
    df_grouped = df_sorted.groupby(["Matrícula SSP", "Ano do gozo"], as_index=False).first()

    # Concatenar os valores de 'SEI' para os registros agrupados
    df_sei = df.groupby(["Matrícula SSP", "Ano do gozo"])['SEI'].apply(lambda x: ' '.join(x)).reset_index()

    # Mesclar os DataFrames
    result = df_grouped.merge(df_sei, on=["Matrícula SSP", "Ano do gozo"], suffixes=("", "_concat"))
    result["SEI"] = result["SEI_concat"]
    del result["SEI_concat"]

    return result