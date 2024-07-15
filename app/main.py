from fastapi import FastAPI
from app.crud import aluno, curso, professor

app = FastAPI()

app.include_router(aluno.router, prefix="/alunos", tags=["alunos"])
app.include_router(curso.router, prefix="/cursos", tags=["cursos"])
app.include_router(professor.router, prefix="/professores", tags=["professores"])
