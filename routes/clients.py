from fastapi import APIRouter, HTTPException, Depends
from models.clients import Client
from bulk_database.clients_db_helper import ClientsDbHelper


router = APIRouter()

@router.post("/clients/")
def create_client(client: Client):
    if ClientsDbHelper.insert_client(client):
        return {"message": "Client created successfully!"}
    else:
        return {"message": "Error creating client"}, 500


@router.get("/clients/")
def get_clients():
    result = ClientsDbHelper.get_clients()
    if result != None:
        return {"clients": result}, 200
    else:
        raise HTTPException(status_code=500, detail="Error al obtener los clientes")