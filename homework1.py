import psycopg2

def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS clients (
                client_id serial primary key,
                first_name varchar(255) not null,
                last_name varchar(255) not null,
                email varchar(100) null
                    );
                """)
        cur.execute("""CREATE TABLE IF NOT EXISTS phones (
	            phone_id serial primary key,
	            client_id int not null,
	            phone varchar(22) null,
	            CONSTRAINT fk_client_id FOREIGN KEY(client_id) REFERENCES clients(client_id) ON DELETE CASCADE
                    );
                """)
        conn.commit()


def add_client(conn, first_name, last_name, email, phones=None):
    with conn.cursor() as cur:
        sql = """INSERT INTO clients (first_name,last_name,email) VALUES (%s,%s,%s) RETURNING client_id;"""
        params = (first_name, last_name, email)
        cur.execute(sql,params)
        client_id = cur.fetchone()[0]
        print(phones)
        if phones:
            for phone in phones:
                phone_sql = """INSERT INTO phones (client_id,phone) VALUES (%s,%s);"""
                cur.execute(phone_sql,(client_id,phone))
                print(phone_sql)
        conn.commit()


def add_phone(conn, client_id, phone):
    with conn.cursor() as cur:
        check_sql = """SELECT client_id FROM clients WHERE client_id=%s;"""
        cur.execute(check_sql,(client_id,))
        found_id = cur.fetchone()[0]
        print(found_id)
        if isinstance(found_id,int) == True:
            print(f'Adding phone {phone} to client id {client_id} ',end='')
            sql = """INSERT INTO phones (client_id,phone) VALUES (%s,%s);"""
            params = (client_id, phone)
            cur.execute(sql,params)
            print('Ok!')
        else:
            print('Client not found!')
        conn.commit()


def change_client(conn, client_id, first_name=None, last_name=None, email=None, phones=None):
    olddata = {}
    newdata = {}
    with conn.cursor() as cur:
        select_data = """SELECT first_name,last_name,email FROM clients WHERE client_id=%s"""
        cur.execute(select_data,(client_id,))
        datalist = list(cur.fetchall()[0])
        olddata["first_name"] = datalist[0]
        olddata["last_name"] = datalist[1]
        olddata["email"] = datalist[2]
        
        if first_name:
            olddata["first_name"] = first_name
        elif last_name:
            olddata["last_name"] = last_name
        elif email:
            olddata["email"] = last_name
        newdata = olddata.copy()
        print(newdata)
        
        for table_name,value in newdata.items():
            update_sql = f'UPDATE clients SET {table_name}=%s WHERE client_id=%s;'
            params = (value,client_id)
            cur.execute(update_sql,params)
        
        if phones:
            print('Updating phones!')
            delete_sql = """DELETE FROM phones WHERE client_id=%s"""
            cur.execute(delete_sql,(client_id,))
            for phone in phones:
                insert_sql = """INSERT INTO phones (client_id,phone) VALUES (%s,%s);"""
                cur.execute(insert_sql,(client_id,phone))       
        conn.commit()
    

def delete_phone(conn, client_id, phone):
    phone = str(phone)
    with conn.cursor() as cur:
        delete_sql = """DELETE FROM phones WHERE phone=%s and client_id=%s;"""
        cur.execute(delete_sql,(phone,client_id))
    conn.commit()

def find_client(conn, first_name=None, last_name=None, email=None, phone=None):
    with conn.cursor() as cur:
        select_sql = """SELECT c.client_id FROM clients c INNER JOIN phones p ON c.client_id=p.client_id WHERE c.first_name=%s OR c.last_name=%s OR c.email=%s OR p.phone=%s"""
        cur.execute(select_sql,(first_name,last_name,email,phone))        
        found_id = cur.fetchone()[0]
        print(found_id)
    conn.commit()

with psycopg2.connect(database="netology_db",user="postgres",password="",host="192.168.32.215") as conn:
    create_db(conn)
    add_client(conn,'Bob','Marley','info@bobmarleymuseum.com')
    add_client(conn,'Frank','Sinatra','contact@thefranksinatra.com',['954-295-4464','310-288-9970'])
    add_phone(conn,'5','89251111112')
    add_phone(conn,'27','89251111112')
    change_client(conn,'27','SuperBob_','Marley','info@bobmarleymuseum.com',['89031111111','89261151115'])
    change_client(conn,'27','Bob','Marley')
    delete_phone(conn,'27','89031111111')
    find_client(conn,'Bob','')
    find_client(conn,'','Marley')
conn.close()