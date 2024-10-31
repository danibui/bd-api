from database import get_db_connection
from models.payments import Payment

class PaymentsDbHelper:
    @staticmethod
    def create_payment(payment: Payment):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """
            INSERT INTO payments (appointment_id, amount, payment_date, payment_method)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (payment.appointment_id, payment.amount, 
                             payment.payment_date, payment.payment_method))
        conn.commit()
        cursor.close()
        conn.close()
        
        return True

    @staticmethod
    def get_all_payments():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        
        query = "SELECT * FROM payments"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return result