import mysql.connector


db_conn = mysql.connector.connect(
    host="kafka-lab.westus2.cloudapp.azure.com", user="root", password="root", database="events")


db_cursor = db_conn.cursor()

db_cursor.execute(''' 
                DROP TABLE add_orders, payments 
                ''')


db_conn.commit()
db_conn.close()
