from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel



app = FastAPI()

origins = ['http://localhost:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animal(BaseModel):
    id: Optional[int]
    nome: str
    cor:str
    sexo: str
    idade: int


banco:List[Animal] = []



@app.get('/animal')
def listar_animal():
    return banco

@app.post('/animal')
def criar_animal(animal:Animal):
    banco.append(animal)
    return None

@app.get('/animal/{id_animal}')
def obter_animal(id_animal: int):
    for animal in banco:
        if animal.id == id_animal:
            return  banco[animal.id]
        
@app.delete('/animal/{id_animal}')
def remover_animal(id_animal: int):
    possicao = -1
    for index, animal in enumerate(banco):
        if animal.id == id_animal:
            possicao = index
            break
    if possicao!= -1:
        banco.pop(possicao)
    
    return  None
    