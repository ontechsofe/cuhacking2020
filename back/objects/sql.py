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
            print (f'Error logging in user', error)
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

    def new_session(self, client_id):
        table_name = 'Session'
        session_id = None
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                sql.SQL("""
                    INSERT INTO Session(clientID)
                    VALUES (%s);
                """),
                [client_id]
            )

            cursor.execute(
                sql.SQL("""
                    SELECT id FROM Session
                    WHERE clientID=%s
                """),
                [client_id]
            )

            session_id = cursor.fetchall()[-1]

            print(f'Added session ID {session_id}')
        except (Exception, Error) as error :
            print (f'Error while starting a new session', error)
            if(self.conn):
                cursor.close()
            return None
        finally:
            self.conn.commit()
            if(self.conn):
                cursor.close()
        return session_id

    def message(self, message):
        table_name0 = 'Interaction'
        table_name1 = 'Session'
        table_name2 = 'InteractionSessionRelationship'
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                sql.SQL("""
                    INSERT INTO Interaction(message, senderID, recipientID, time, sentiment)
                    VALUES (%s, %s, %s, %s, %s)
                """),
                [message['text'], message['sender'], message['recipient'], message['time'], message['sentiment']]
            )

            cursor.execute(
                sql.SQL("""
                    SELECT id
                    FROM Interaction
                    WHERE time=%s AND senderID=%s AND recipientID=%s
                """),
                [message['time'], message['sender'], message['recipient']]
            )
            interaction_id = cursor.fetchone()[0]

            cursor.execute(
                sql.SQL("""
                    INSERT INTO InteractionSessionRelational(interactionID, sessionID)
                    VALUES (%s, %s)
                """),
                [interaction_id, message['session']]
            )
            print(f"Added Interaction from {message['sender']} to {message['recipient']} at {message['time']}")

        except (Exception, Error) as error :
            print (f'Error while inserting into table.', error)
            if(self.conn):
                cursor.close()
            return False
        finally:
            self.conn.commit()
            if(self.conn):
                cursor.close()
        return True
    
    def get_messages(self, session_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                sql.SQL("""
                    SELECT message, senderID, recipientID, time
                    FROM InteractionSessionRelational AS ISR
                    JOIN Interaction AS I ON ISR.interactionID=I.id
                    WHERE sessionID=%s
                """),
                [session_id]
            )

            messages = [ {
                'message': message,
                'senderID': sender_id,
                'recipientID': recipient_id,
                'time': time
                } for (message, sender_id, recipient_id, time) in cursor.fetchall()]
        except (Exception, Error) as error :
            print (f'Error logging in user', error)
            if(self.conn):
                cursor.close()
            return None
        finally:
            if(self.conn):
                cursor.close()
        if len(messages):
            return messages
        else:
            return None

    # EVERYTHING DOWN HERE FOR THERAPISTS
    def get_clients(self):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                sql.SQL("""
                    SELECT id, name
                    FROM Client
                    WHERE name!=%s
                """),
                ['Melanie']
            )

            clients = [ {
                'clientID': client_id,
                'clientName': client_name
                } for (client_id, client_name) in cursor.fetchall()]
        except (Exception, Error) as error :
            print (f'Error logging in user', error)
            if(self.conn):
                cursor.close()
            return None
        finally:
            if(self.conn):
                cursor.close()
        if len(clients):
            return clients
        else:
            return None
    
    def all_messages(self, client_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                sql.SQL("""
                    SELECT sessionId, message, senderID, recipientID, time, sentiment
                    FROM InteractionSessionRelational AS ISR
                    JOIN Interaction AS I ON ISR.interactionID=I.id
                    WHERE senderID=%s OR recipientID=%s
                """),
                [client_id, client_id]
            )

            messages = [ {
                'sessionID': session_id,
                'message': message,
                'senderID': sender_id,
                'recipientID': recipient_id,
                'time': time,
                'sentiment': sentiment
                } for (session_id, message, sender_id, recipient_id, time, sentiment) in cursor.fetchall()]

            cursor.execute(
                sql.SQL("""
                    SELECT id
                    FROM Session
                    WHERE clientID=%s
                """),
                [client_id]
            )
            session_ids = [x[0] for x in cursor.fetchall()]
            
        except (Exception, Error) as error :
            print (f'Error getting all messages', error)
            if(self.conn):
                cursor.close()
            return None
        finally:
            if(self.conn):
                cursor.close()
        if len(messages):
            return messages, session_ids
        else:
            return None