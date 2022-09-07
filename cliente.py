from pydantic import BaseModel


class ClienteBase(BaseModel):
    nome: str
    endereco: str
    email: str
    telefone: str

class CreateCliente(ClienteBase):
    pass

class Cliente(ClienteBase):
    id: int

    class Config:
        orm_mode = True