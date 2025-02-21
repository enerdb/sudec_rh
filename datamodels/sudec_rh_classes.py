from pydantic import BaseModel, PositiveInt, StrictBool, EmailStr
from datetime import datetime
from typing import List, Optional

# pip install email-validator
# Separar classes de banco e classes de cadastro
# Só as classes de cadastro terão timestamp

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
    # Dados básicos
    matricula: PositiveInt # Chave Primaria
    nome: str
    nome_guerra: str
    militar: StrictBool

    # Dados militar
    posto: Optional[PositiveInt] = None
    quadro: Optional[str] = None
    siape: Optional[PositiveInt] = None

    # Dados sensiveis
    cpf: Optional[PositiveInt] = None
    endereco: Optional[str] = None
    cidade: Optional[str] = None
    cep: Optional[str] = None
    fone1: Optional[str] = None
    fone2: Optional[str] = None
    emaili: Optional[EmailStr] = None
    emailp: Optional[EmailStr] = None
    sexo_fem: Optional[bool] = None
    tipo_sang: Optional[str] = None
    fator_rh: Optional[bool] = None
    emergenc_cont: Optional[str] = None
    alergias: Optional[str] = None
    outr_cond: Optional[str] = None

    # Dados funcionais
    horario_manha: Optional[bool] = None
    atividade: Optional[str] = None
    local_trab: Optional[str] = None

    #?
    #nomeado: bool # Precisa?

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



