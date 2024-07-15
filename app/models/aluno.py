from pydantic import BaseModel

class Aluno(BaseModel):
    id_aluno: int = None
    nome: str
    data_nascimento: str
    logradouro: str = None
    numero: int = None
    bairro: str = None
    cidade: str = None
    estado: str = None
    data_criacao: str = None
    cep: str = None
    id_curso: int = None
