from pydantic import BaseModel, PositiveInt, StrictBool, EmailStr
from datetime import datetime
from typing import List

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
    timestamp: datetime # pensar em como usar isso. acho que não faz sentido se eu manter 2 listas, uma ativa e uma histórica
    matricula: PositiveInt # Chave Primaria
    nome: str
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
    sexo_fem: bool
    tipo_sang: str
    rh: bool
    emergenc_cont: str
    alergias: str
    outr_cond: str
    horario_manha: bool
    atividade: str
    local_trab: str
    nomeado: bool

#ID	Nome_full	nome_Cargo	Setor	SIGRH - FUNÇÃO (DEC 46.117)	Gratificação	NC_padronizado	Seq	Ocupante
class Cargo(BaseModel):
    cargo_id: PositiveInt # Chave Primaria
    full_name: str
    sigrh: str
    gratificacao: str
    salario: float
    setor: str
    ocupante: PositiveInt # Chave externa para Servidor

class Nomeacao(BaseModel):
    timestamp: datetime
    matricula: PositiveInt
    cargo_id: PositiveInt
    data_nomeacao: datetime
    data_min_exoneracao: datetime

class Exoneracao(BaseModel):
    timestamp: datetime
    matricula: PositiveInt
    cargo_id: PositiveInt
    data_exoneracao: datetime


# registrar uma lista de dias de afastamento e tentar usar herança para os outros tipos de afastamento.
# Ainda não vi ganho em implementar o modelo acima
class AfastamentoGenerico(BaseModel):
    timestamp: datetime
    matricula: PositiveInt
    dia1: datetime
    diau: datetime
    tipo: str
    sei: str

#	ano: de gozo 1º Período - início	1º Período - último dia	2º Período - início	2º Período - último dia	3º Período - início	3º Período - último dia	SEI
class Ferias(BaseModel):
    timestamp: datetime
    ano: PositiveInt
    p1_dia1: datetime
    p1_diau: datetime
    p2_dia1: datetime
    p2_diau: datetime
    p3_dia1: datetime
    p4_diau: datetime
    sei: str

class Abono(BaseModel):
    timestamp: datetime
    matricula: PositiveInt
    ano: PositiveInt
    dia1: datetime
    dia2: datetime
    dia3: datetime
    dia4: datetime
    dia5: datetime
    sei: str



