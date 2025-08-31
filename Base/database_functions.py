import psycopg2


class DataBaseFunctions:
         
    def __init__(self):
        pass
         
        
    def db_connection(self, sql):
        conn = psycopg2.connect(
            dbname="piano",
            user="jazz",
            password="jazz",
            host="localhost",
            port="5432"
        )

        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        return rows

