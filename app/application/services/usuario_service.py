from app.domain.entities.usuario import Usuario
from app.infrastructure.repositories.usuario_repository import UsuarioRepository
from typing import List

class UsuarioService:
    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    def crear_usuario(self, id: int, nombre: str, email: str) -> Usuario:
        usuario = Usuario(id, nombre, email)
        self.repo.agregar_usuario(usuario)
        return usuario

    def obtener_usuarios(self) -> List[Usuario]:
        return self.repo.obtener_todos()
