import psycopg2

def obtener_conexion():
    return psycopg2.connect(
        host="localhost",
        database="curso_flask",
        user="postgres",
        password="12345",
        port="5432"
    )