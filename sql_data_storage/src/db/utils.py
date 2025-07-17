def execute_query(connection, query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        connection.commit()

def fetch_all(connection, query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        return cursor.fetchall()

def fetch_one(connection, query, params=None):
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        return cursor.fetchone()

def insert_record(connection, table, data):
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'
    execute_query(connection, query, tuple(data.values()))

def update_record(connection, table, data, condition):
    set_clause = ', '.join([f"{key} = %s" for key in data.keys()])
    query = f'UPDATE {table} SET {set_clause} WHERE {condition}'
    execute_query(connection, query, tuple(data.values()))

def delete_record(connection, table, condition):
    query = f'DELETE FROM {table} WHERE {condition}'
    execute_query(connection, query)