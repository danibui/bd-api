from database import get_db_connection
from models.doctors import Doctor

class DoctorsDbHelper:
    @staticmethod
    def insert_doctor(doctor: Doctor):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            query = """
                INSERT INTO doctors (name, specialty, phone, email)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (doctor.name, doctor.specialty, doctor.phone, doctor.email))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al insertar doctor: {str(e)}")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_doctors():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            query = "SELECT * FROM doctors"
            cursor.execute(query)
            result = cursor.fetchall()
            return result, True
        except Exception as e:
            print(f"Error al obtener doctores: {str(e)}")
            return [], False
        finally:
            cursor.close()
            conn.close()        