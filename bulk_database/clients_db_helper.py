from database import get_db_connection
from models.clients import Client

class ClientsDbHelper:
    @staticmethod
    def insert_client(client: Client):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            query = """
                INSERT INTO clients (name, phone, email, start_date, end_date) 
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (client.name, client.phone, client.email, client.start_date, client.end_date))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al insertar cliente: {str(e)}")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    
    @staticmethod
    def get_clients():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        query = "SELECT * FROM clients"
        cursor.execute(query)
        result = cursor.fetchall()  

        cursor.close()
        conn.close()

        return result
