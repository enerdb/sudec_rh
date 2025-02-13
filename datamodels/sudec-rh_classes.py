from pydantic import BaseModel, PositiveInt, StrictBool, EmailStr
# pip install email-validator

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

class Servidor(BaseModel):
    matricula: PositiveInt
    nome:   str
    nome_guerra: str
    cpf: PositiveInt
    militar: StrictBool 
    posto: PositiveInt
    quadro: str
    siape: PositiveInt
    endereco: str
    cidade: str
    cep: str
    fone1: str
    fone2: str
    emaili: EmailStr
    emailp: EmailStr
    sexo: bool
    tipo_sang: str
    rh: bool
    emergenc_cont: str
    outr_cond: str
