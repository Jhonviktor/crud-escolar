from fastapi import APIRouter, HTTPException, Depends
from typing import List
import sqlite3
from app.banco import get_db
from app.models.professor import Professor

router = APIRouter()

@router.post("/", response_model=Professor)
def create_professor(professor: Professor, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO PROFESSOR (NOME, DATA_NASCIMENTO, DATA_CRIACAO)
        VALUES (?,?,?)
    """, (professor.nome, professor.data_nascimento, professor.data_criacao))
    db.commit()
    professor.id_professor = cursor.lastrowid
    return professor

@router.get("/", response_model=List[Professor])
def read_professores(skip: int = 0, limit: int = 10, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM PROFESSOR LIMIT? OFFSET?", (limit, skip))
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    professores = []
    for row in rows:
        data = dict(zip(columns, row))
        professor = Professor(
            id_professor=data.get('ID_PROFESSOR'),
            nome=data.get('NOME'),
            data_nascimento=data.get('DATA_NASCIMENTO'),
            data_criacao=data.get('DATA_CRIACAO')
        )
        professores.append(professor)
    return professores

@router.get("/{id_professor}", response_model=Professor)
def read_professor(id_professor: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM PROFESSOR WHERE ID_PROFESSOR =?", (id_professor,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Professor not found")
    columns = [desc[0] for desc in cursor.description]
    data = dict(zip(columns, row))
    professor = Professor(
        id_professor=data.get('ID_PROFESSOR'),
        nome=data.get('NOME'),
        data_nascimento=data.get('DATA_NASCIMENTO'),
        data_criacao=data.get('DATA_CRIACAO')
    )
    return professor

@router.put("/{id_professor}", response_model=Professor)
def update_professor(id_professor: int, professor: Professor, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("""
        UPDATE PROFESSOR SET NOME =?, DATA_NASCIMENTO =?, DATA_CRIACAO =?
        WHERE ID_PROFESSOR =?
    """, (professor.nome, professor.data_nascimento, professor.data_criacao, id_professor))
    db.commit()
    return professor

@router.delete("/{id_professor}", response_model=Professor)
def delete_professor(id_professor: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM PROFESSOR WHERE ID_PROFESSOR =?", (id_professor,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Professor not found")
    columns = [desc[0] for desc in cursor.description]
    data = dict(zip(columns, row))
    professor = Professor(
        id_professor=data.get('ID_PROFESSOR'),
        nome=data.get('NOME'),
        data_nascimento=data.get('DATA_NASCIMENTO'),
        data_criacao=data.get('DATA_CRIACAO')
    )
    cursor.execute("DELETE FROM PROFESSOR WHERE ID_PROFESSOR =?", (id_professor,))
    db.commit()
    return professor