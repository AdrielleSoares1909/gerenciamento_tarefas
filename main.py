"""
    PROJETO — API de Gerenciamento de Tarefas

    Imagine que uma empresa quer um sistema simples para organizar tarefas internas.
    --------------------------------

    📌 Funcionalidades obrigatórias

    1️⃣ Criar uma tarefa
    --------------------------
    Campos:

    id

    título

    descrição

    status (pendente, em andamento, concluída)

    data de criação
    ---------------------------

    2️⃣ Listar todas as tarefas

    3️⃣ Buscar tarefa por ID

    4️⃣ Atualizar tarefa

    5️⃣ Deletar tarefa
"""

from fastapi import FastAPI,HTTPException
import requests
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI(
    title = "API GERENCIADOR DE TAREFAS",
    description = "Gerenciar tarefas do dia a dia"
)



class Tarefa(BaseModel):
    id: Optional[str]
    titulo: str
    descricao : str
    status : str
    


banco: list[Tarefa] = []

@app.get('/tarefas')
def atualizar_tarefas():
    return banco

@app.get('/tarefas/{tarefa_id}')
def obter_tarefa(tarefa_id: str):
    for tarefa in banco:
        if tarefa.id == tarefa_id:
            return tarefa
    return {'Erro:' 'Tarefa nao encontrada'}


@app.delete('/tarefas/{tarefa_id}')
def deletar_tarefas(tarefa_id: str):
    posicao = -1
    # buscar a posicao da tarefa
    for index, tarefa in enumerate(banco):
        if tarefa.id == tarefa_id:
            posicao = index
            break

    if posicao != -1:
        banco.pop(posicao)
        return {'Mensagem': 'Terefa removida com sucesso'}
    else:
        return {'Mensagem': "Tarefa nao localizada"}


@app.post("/tarefas")
def criar_tarefas(tarefa: Tarefa): 
    tarefa.id = str(uuid4())
    banco.append(tarefa)
    return banco






