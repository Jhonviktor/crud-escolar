from fastapi import APIRouter, HTTPException, Depends
from typing import List
import sqlite3
from app.banco import get_db
from app.models.curso import Curso

router = APIRouter()

@router.post("/", response_model=Curso)
def create_curso(curso: Curso, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO CURSO (NOME, DATA_CRIACAO, ID_PROFESSOR)
        VALUES (?, ?, ?)
    """, (curso.nome, curso.data_criacao, curso.id_professor))
    db.commit()
    curso.id_curso = cursor.lastrowid
    return curso

@router.get("/", response_model=List[Curso])
def read_cursos(skip: int = 0, limit: int = 10, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM CURSO LIMIT ? OFFSET ?", (limit, skip))
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    cursos = []
    for row in rows:
        data = dict(zip(columns, row))
        curso = Curso(
            id_curso=data.get('ID_CURSO'),
            nome=data.get('NOME'),
            data_criacao=data.get('DATA_CRIACAO'),
            id_professor=data.get('ID_PROFESSOR')
        )
        cursos.append(curso)
    return cursos

@router.get("/{id_curso}", response_model=Curso)
def read_curso(id_curso: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM CURSO WHERE ID_CURSO = ?", (id_curso,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Curso not found")
    columns = [desc[0] for desc in cursor.description]
    data = dict(zip(columns, row))
    curso = Curso(
        id_curso=data.get('ID_CURSO'),
        nome=data.get('NOME'),
        data_criacao=data.get('DATA_CRIACAO'),
        id_professor=data.get('ID_PROFESSOR')
    )
    return curso

@router.put("/{id_curso}", response_model=Curso)
def update_curso(id_curso: int, curso: Curso, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("""
        UPDATE CURSO SET NOME = ?, DATA_CRIACAO = ?, ID_PROFESSOR = ?
        WHERE ID_CURSO = ?
    """, (curso.nome, curso.data_criacao, curso.id_professor, id_curso))
    db.commit()
    return curso

@router.delete("/{id_curso}", response_model=Curso)
def delete_curso(id_curso: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM CURSO WHERE ID_CURSO = ?", (id_curso,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Curso not found")
    columns = [desc[0] for desc in cursor.description]
    data = dict(zip(columns, row))
    curso = Curso(
        id_curso=data.get('ID_CURSO'),
        nome=data.get('NOME'),
        data_criacao=data.get('DATA_CRIACAO'),
        id_professor=data.get('ID_PROFESSOR')
    )
    cursor.execute("DELETE FROM CURSO WHERE ID_CURSO = ?", (id_curso,))
    db.commit()
    return curso