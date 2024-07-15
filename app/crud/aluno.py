from fastapi import APIRouter, HTTPException, Depends
from typing import List
import sqlite3
from app.banco import get_db
from app.models.aluno import Aluno

router = APIRouter()

@router.post("/", response_model=Aluno)
def create_aluno(aluno: Aluno, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO ALUNO (NOME, DATA_NASCIMENTO, LOGRADOURO, NUMERO, BAIRRO, CIDADE, ESTADO, DATA_CRIACAO, CEP, ID_CURSO)
        VALUES (?,?,?,?,?,?,?,?,?,?)
    """, (aluno.nome, aluno.data_nascimento, aluno.logradouro, aluno.numero, aluno.bairro, aluno.cidade, aluno.estado, aluno.data_criacao, aluno.cep, aluno.id_curso))
    db.commit()
    aluno.id_aluno = cursor.lastrowid
    return aluno

@router.get("/", response_model=List[Aluno])
def read_alunos(skip: int = 0, limit: int = 10, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM ALUNO LIMIT? OFFSET?", (limit, skip))
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    alunos = []
    for row in rows:
        data = dict(zip(columns, row))
        aluno = Aluno(
            id_aluno=data.get('ID_ALUNO'),
            nome=data.get('NOME'),
            data_nascimento=data.get('DATA_NASCIMENTO'),
            logradouro=data.get('LOGRADOURO'),
            numero=data.get('NUMERO'),
            bairro=data.get('BAIRRO'),
            cidade=data.get('CIDADE'),
            estado=data.get('ESTADO'),
            data_criacao=data.get('DATA_CRIACAO'),
            cep=data.get('CEP'),
            id_curso=data.get('ID_CURSO')
        )
        alunos.append(aluno)
    return alunos

@router.get("/{id_aluno}", response_model=Aluno)
def read_aluno(id_aluno: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM ALUNO WHERE ID_ALUNO =?", (id_aluno,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Aluno not found")
    columns = [desc[0] for desc in cursor.description]
    data = dict(zip(columns, row))
    aluno = Aluno(
        id_aluno=data.get('ID_ALUNO'),
        nome=data.get('NOME'),
        data_nascimento=data.get('DATA_NASCIMENTO'),
        logradouro=data.get('LOGRADOURO'),
        numero=data.get('NUMERO'),
        bairro=data.get('BAIRRO'),
        cidade=data.get('CIDADE'),
        estado=data.get('ESTADO'),
        data_criacao=data.get('DATA_CRIACAO'),
        cep=data.get('CEP'),
        id_curso=data.get('ID_CURSO')
    )
    return aluno

@router.put("/{id_aluno}", response_model=Aluno)
def update_aluno(id_aluno: int, aluno: Aluno, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("""
        UPDATE ALUNO SET NOME =?, DATA_NASCIMENTO =?, LOGRADOURO =?, NUMERO =?, BAIRRO =?, CIDADE =?, ESTADO =?, DATA_CRIACAO =?, CEP =?, ID_CURSO =?
        WHERE ID_ALUNO =?
    """, (aluno.nome, aluno.data_nascimento, aluno.logradouro, aluno.numero, aluno.bairro, aluno.cidade, aluno.estado, aluno.data_criacao, aluno.cep, aluno.id_curso, id_aluno))
    db.commit()
    return aluno

@router.delete("/{id_aluno}", response_model=Aluno)
def delete_aluno(id_aluno: int, db: sqlite3.Connection = Depends(get_db)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM ALUNO WHERE ID_ALUNO =?", (id_aluno,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Aluno not found")
    columns = [desc[0] for desc in cursor.description]
    data = dict(zip(columns, row))
    aluno = Aluno(
        id_aluno=data.get('ID_ALUNO'),
        nome=data.get('NOME'),
        data_nascimento=data.get('DATA_NASCIMENTO'),
        logradouro=data.get('LOGRADOURO'),
        numero=data.get('NUMERO'),
        bairro=data.get('BAIRRO'),
        cidade=data.get('CIDADE'),
        estado=data.get('ESTADO'),
        data_criacao=data.get('DATA_CRIACAO'),
        cep=data.get('CEP'),
        id_curso=data.get('ID_CURSO')
    )
    cursor.execute("DELETE FROM ALUNO WHERE ID_ALUNO =?", (id_aluno,))
    db.commit()
    return aluno