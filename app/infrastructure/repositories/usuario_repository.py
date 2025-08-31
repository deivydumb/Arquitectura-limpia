from app.domain.entities.usuario import Usuario
from typing import List

class UsuarioRepository:
    def __init__(self):
        self._usuarios = []

    def agregar_usuario(self, usuario: Usuario):
        self._usuarios.append(usuario)

    def obtener_todos(self) -> List[Usuario]:
        return self._usuarios
