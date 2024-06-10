import psycopg2

conn = psycopg2.connect(database="netology_db",user="postgres",password="",host="192.168.32.215")
with conn.cursor() as cur:
    cur.execute("CREATE TABLE IF NOT EXISTS test(id serial primary key);")
    conn.commit()
conn.close()