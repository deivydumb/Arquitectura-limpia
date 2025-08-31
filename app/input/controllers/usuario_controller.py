from app.application.services.usuario_service import UsuarioService
from app.infrastructure.repositories.usuario_repository import UsuarioRepository
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
repo = UsuarioRepository()
service = UsuarioService(repo)

class UsuarioIn(BaseModel):
    id: int
    nombre: str
    email: str

class UsuarioOut(BaseModel):
    id: int
    nombre: str
    email: str

@app.post("/usuarios", response_model=UsuarioOut)
def crear_usuario(usuario: UsuarioIn):
    nuevo_usuario = service.crear_usuario(usuario.id, usuario.nombre, usuario.email)
    return UsuarioOut(id=nuevo_usuario.id, nombre=nuevo_usuario.nombre, email=nuevo_usuario.email)

@app.get("/usuarios", response_model=List[UsuarioOut])
def obtener_usuarios():
    usuarios = service.obtener_usuarios()
    return [UsuarioOut(id=u.id, nombre=u.nombre, email=u.email) for u in usuarios]
