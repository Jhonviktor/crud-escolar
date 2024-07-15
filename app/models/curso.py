from pydantic import BaseModel

class Curso(BaseModel):
    id_curso: int = None
    nome: str
    data_criacao: str = None
    id_professor: int = None
