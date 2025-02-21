import pandas as pd
from config import POSTO_NUM

#["Matrícula na SSP","Nome Completo","Nome de Guerra (preferencial se civil)","Efetividade","Posto ou Graduação","Quadro QOBM/QBMG","Cidade","Sexo", "Horário de trabalho", "Atividade predominante", "Local de Trabalho"]

def trata_servidor_2sys(df):

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
    df['Antiguidade']              = df['Posto ou Graduação'].map(POSTO_NUM).fillna(14)

    return df

def trata_servidor_2drive(df):
    pass

def filter_servidor_by_matricula(df, matricula):
    return df[df["Matrícula na SSP"]==matricula]

def concat_servidor(df1, df2):
    pass

#def add_servidor(df1, )



# 0:"Matrícula na SSP"
# 1:"Nome Completo"
# 2:"Nome de Guerra (preferencial se civil)"
# 3:"Efetividade"
# 4:"Posto ou Graduação"
# 5:"Quadro QOBM/QBMG"
# 6:"Cidade"
# 7:"Sexo"
# 8:"Horário de trabalho"
# 9:"Atividade predominante"
# 10:"Local de Trabalho"
# 11:"Antiguidade"

# class Servidor(BaseModel):
#     # Dados básicos                               
#     matricula: PositiveInt # Chave Primaria               Matrícula na SSP
#     nome: str                                             Nome Completo
#     nome_guerra: str                                      Nome de Guerra (preferencial se civil)
#     militar: StrictBool                                   Efetividade

#     # Dados militar
#     posto: Optional[PositiveInt] = None                   Posto ou Graduação
#     quadro: Optional[str] = None                          Quadro QOBM/QBMG
#     siape: Optional[PositiveInt] = None

#     # Dados sensiveis
#     cpf: Optional[PositiveInt] = None
#     endereco: Optional[str] = None
#     cep: Optional[str] = None
#     fone1: Optional[str] = None
#     fone2: Optional[str] = None
#     emaili: Optional[EmailStr] = None
#     emailp: Optional[EmailStr] = None
#     sexo_fem: Optional[bool] = None                       Sexo
#     tipo_sang: Optional[str] = None
#     fator_rh: Optional[bool] = None
#     emergenc_cont: Optional[str] = None
#     alergias: Optional[str] = None
#     outr_cond: Optional[str] = None

#     # Dados funcionais
#     cidade: Optional[str] = None                          Cidade
#     horario_manha: Optional[bool] = None                  Horário de trabalho
#     atividade: Optional[str] = None                       Atividade predominante
#     local_trab: Optional[str] = None                      Local de Trabalho