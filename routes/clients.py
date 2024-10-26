from fastapi import APIRouter, HTTPException, Depends
from models.clients import Client
from database import get_db_connection

router = APIRouter()

@router.post("/clients/")
def create_client(client: Client):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO clients (name, phone, email, start_date, end_date) 
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (client.name, client.phone, client.email, client.start_date, client.end_date))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Client created successfully!"}

@router.get("/clients/")
def get_clients():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM clients"
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    if not result:
        raise HTTPException(status_code=404, detail="No clients found")
    
    return result
