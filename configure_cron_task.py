"""
Скрипт для периодического вызова хранимой процедуры `insert_random_data` в базе данных PostgreSQL.

Описание:
- Устанавливает соединение с базой данных PostgreSQL.
- Вызывает хранимую процедуру `insert_random_data`.
- Если процедура выполнилась успешно, сохраняет изменения в базе данных.
- В случае ошибки при выполнении процедуры, выводит сообщение об ошибке.

"""


import psycopg2
import schedule
import time

def execute_procedure():
    try:
        conn = psycopg2.connect(
            dbname='postgres',
            user='postgres',
            password='mysecretpassword',
            host='postgres',  
            port='5432',
            client_encoding='UTF8'
        )
        cur = conn.cursor()
        cur.execute("CALL insert_random_data();")
        conn.commit()
        cur.close()
        conn.close()
        print("Процедура успешно выполнена")
    except Exception as e:
        print(f"Ошибка при выполнении процедуры: {e}")


schedule.every(5).seconds.do(execute_procedure)

while True:
    schedule.run_pending()
    print("Ожидание следующего запуска...")
    time.sleep(1)