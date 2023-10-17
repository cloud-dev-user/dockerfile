import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        host="postgres",
        database="my-app-database",
        user="my-app-user",
        password="my-app-password"
    )
    return conn

def write_to_db(data):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("INSERT INTO my-app-table (data) VALUES (%s)", (data,))

    conn.commit()
    cur.close()
    conn.close()

# Example usage:

write_to_db("Hello, world!")
