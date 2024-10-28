from database import get_db_connection
from models.appointments import Appointment

class AppointmentsDbHelper:
    @staticmethod
    def insert_appointment(appointment: Appointment):
        conn = get_db_connection()
        cursor = conn.cursor()

        try:
            query = """
                INSERT INTO appointments (client_id, appointment_date, treatment, doctor_id) 
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (appointment.client_id, appointment.appointment_date, appointment.treatment, appointment.doctor_id))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error al insertar cita: {str(e)}")
            conn.rollback()
            return False
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def get_appointments():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        try:
            query = "SELECT * FROM appointments"
            cursor.execute(query)
            result = cursor.fetchall()
            return result, True
        except Exception as e:
            print(f"Error al obtener citas: {str(e)}")
            return [], False
        finally:
            cursor.close()
            conn.close()