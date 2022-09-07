from fastapi import FastAPI
from cliente import Cliente
from crud import listar_clientes, create_cliente, delete_cliente_by_name

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/clientes/listar")
async def listar_clientes_db():
    return await listar_clientes()

@app.post("/clientes/cadastrar")
async def create_cliente_db(cliente: Cliente):
    return await create_cliente(cliente=cliente)

@app.delete("/clientes/deletar_cliente")
async def delete_cliente_db(cliente: Cliente):
    return await delete_cliente_by_name(cliente=cliente)



