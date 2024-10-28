from database import get_db_connection
from models.medical_history import MedicalHistory

class MedicalHistoryDbHelper:
    @staticmethod
    def create_medical_history(history: MedicalHistory):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """
            INSERT INTO medical_history (client_id, description, history_date)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (history.client_id, history.description, history.history_date))
        conn.commit()
        cursor.close()
        conn.close()
        
        return True

    @staticmethod
    def get_all_medical_history():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM medical_history"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result