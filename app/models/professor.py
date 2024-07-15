from pydantic import BaseModel

class Professor(BaseModel):
    id_professor: int = None
    nome: str
    data_nascimento: str
    data_criacao: str = None
