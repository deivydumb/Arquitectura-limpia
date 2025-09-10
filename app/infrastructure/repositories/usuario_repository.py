
from abc import ABC, abstractmethod
from app.domain.entities.usuario import Usuario
from typing import List


class UsuarioRepositoryBase(ABC):
    @abstractmethod
    def agregar_usuario(self, usuario: Usuario):
        pass

    @abstractmethod
    def obtener_todos(self) -> List[Usuario]:
        pass

class UsuarioRepository(UsuarioRepositoryBase):
    def __init__(self):
        self._usuarios = []

    def agregar_usuario(self, usuario: Usuario):
        self._usuarios.append(usuario)

    def obtener_todos(self) -> List[Usuario]:
        return self._usuarios
