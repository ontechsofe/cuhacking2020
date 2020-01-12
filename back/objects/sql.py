from psycopg2 import connect, sql, Error

class SQL(object):
    def __init__(self, DB_CONFIG):
        self.conn = self.connect_to_db(DB_CONFIG)

    def connect_to_db(self, DB_CONFIG):
        try:
            conn = connect(
                    user=DB_CONFIG['username'],
                    password=DB_CONFIG['password'],
                    host=DB_CONFIG['host'],
                    port=DB_CONFIG['port'],
                    database=DB_CONFIG['database']
                )
            return conn
        except (Exception, Error) as error :
            print ('Error while connecting to PostgreSQL', error)
    
    def disconnect_from_db(self):
        self.conn.close()

    def new_client(self, name, username, password) -> bool:
        table_name = 'Client'
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                sql.SQL("""
                    INSERT INTO Client(name, username, password)
                    VALUES (%s, %s, %s);
                """),
                [name, username, password]
            )
            
            print(f'Added user {name}')
        except (Exception, Error) as error :
            print (f'Error while inserting into table {table_name}', error)
            if(self.conn):
                cursor.close()
            return False
        finally:
            self.conn.commit()
            if(self.conn):
                cursor.close()
        return True

    def login(self, username, password):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                sql.SQL("""
                    SELECT id, username
                    FROM Client
                    WHERE username=%s AND password=%s;
                """),
                [username, password]
            )

            client = cursor.fetchall()
        except (Exception, Error) as error :
            print (f'Error while inserting into table {table_name}', error)
            if(self.conn):
                cursor.close()
            return None
        finally:
            if(self.conn):
                cursor.close()
        if len(client):
            return client[0]
        else:
            return None
