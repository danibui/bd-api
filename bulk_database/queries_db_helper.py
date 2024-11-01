from database import get_db_connection

class QueriesDbHelper:
    
   
    @staticmethod
    def get_payments_by_method(payment_method: str):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM payments WHERE payments.payment_method = %s"
        cursor.execute(query, (payment_method,))  # Los parámetros deben pasarse como tupla
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result
    
    @staticmethod
    def get_payments_with_treatments():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT payment_id, amount, payment_date, payment_method, appointments.treatment 
            FROM payments 
            INNER JOIN appointments ON appointments.appointment_id = payments.payment_id
        """
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result
    
    @staticmethod
    def get_payments_with_treatments_and_clients():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT payment_id, amount, payments.payment_date, payments.payment_method,
                   appointments.treatment, clients.name 
            FROM payments
            INNER JOIN appointments ON appointments.appointment_id = payments.payment_id
            INNER JOIN clients ON clients.client_id = appointments.appointment_id
        """
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result
    
    @staticmethod
    def get_clients_with_medical_history():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT * FROM clients
            INNER JOIN medical_history ON medical_history.client_id = clients.client_id
        """
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result

    @staticmethod
    def get_appointments_with_doctors():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT * FROM appointments 
            INNER JOIN doctors ON doctors.doctor_id = appointments.doctor_id
        """
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result
    
    @staticmethod
    def get_appointments_by_treatment(treatment: str):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT * FROM appointments 
            WHERE appointments.treatment = %s
        """
        cursor.execute(query, (treatment,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result
    
    @staticmethod
    def get_treatments_by_type(treatment_type: str):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT * FROM treatments 
            WHERE treatments.treatment_type = %s
        """
        cursor.execute(query, (treatment_type,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result
    
    @staticmethod
    def get_treatments_by_min_cost(min_cost: float):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT * FROM treatments 
            WHERE treatments.cost >= %s
        """
        cursor.execute(query, (min_cost,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result
    
    @staticmethod
    def get_total_treatments_cost():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT SUM(treatments.cost) as total_cost 
            FROM treatments
        """
        cursor.execute(query)
        result = cursor.fetchone()  # Usamos fetchone() porque solo retorna un valor
        cursor.close()
        conn.close()
        
        return result
    
    @staticmethod
    def get_medical_history_from_date(from_date: str):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT * FROM medical_history 
            WHERE medical_history.history_date >= %s
        """
        cursor.execute(query, (from_date,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result
    

    @staticmethod
    def get_doctors_by_specialty(specialty: str):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT * FROM doctors 
            WHERE doctors.specialty = %s
        """
        cursor.execute(query, (specialty,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result
    
    @staticmethod
    def get_client_by_email(email: str):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT * FROM clients 
            WHERE clients.email = %s
        """
        cursor.execute(query, (email,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result
    
    @staticmethod
    def get_clients_appointments_by_doctor(doctor_id: int):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT * FROM clients 
            INNER JOIN appointments ON appointments.client_id = clients.client_id 
            INNER JOIN doctors ON doctors.doctor_id = appointments.doctor_id 
            WHERE doctors.doctor_id = %s
        """
        cursor.execute(query, (doctor_id,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result
    
    @staticmethod
    def get_payments_by_client_id(client_id: int):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = """
            SELECT * FROM payments
            INNER JOIN appointments ON appointments.appointment_id = payments.appointment_id
            INNER JOIN clients ON clients.client_id = appointments.appointment_id
            WHERE clients.client_id = %s
        """
        cursor.execute(query, (client_id,))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result