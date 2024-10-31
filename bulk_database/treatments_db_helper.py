from database import get_db_connection
from models.treatments import Treatment

class TreatmentsDbHelper:
    @staticmethod
    def create_treatment(treatment: Treatment):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """
            INSERT INTO treatments (appointment_id, treatment_type, cost, treatment_date)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (treatment.appointment_id, treatment.treatment_type,
                             treatment.cost, treatment.treatment_date))
        conn.commit()
        cursor.close()
        conn.close()
        
        return True

    @staticmethod
    def get_all_treatments():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM treatments"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result