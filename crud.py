from connector import SQL_Connector
from cliente import Cliente


mydb = SQL_Connector()
mycursor = mydb.cursor()

async def listar_clientes():
    mycursor.execute("SELECT * FROM clientes")
    myresult = mycursor.fetchall()
    print(myresult)

    return myresult

async def create_cliente(cliente: Cliente):
    sql = "INSERT INTO clientes (nome, documento, telefone, email) VALUES (%s, %s, %s, %s)"
    val = (cliente.nome, cliente.endereco, cliente.telefone, cliente.email)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Cliente Inserido")
    return cliente

async def delete_cliente_by_name(cliente: Cliente):
    sql = f"DELETE FROM clientes WHERE nome = {cliente.nome}"
    mycursor.execute(sql)
    mydb.commit()

    print(mycursor.rowcount, f"Cliente {cliente} Removido")
    return cliente
