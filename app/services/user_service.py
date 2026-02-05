from app.utils.util import generate_uuid_v7
from app.core.security import hash_password
from app.db.connection import get_db_connection

def create_user(email: str, username: str, plain_password: str):
    user_id = generate_uuid_v7()
    password_hash = hash_password(plain_password)

    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO users (id, email_address, username, password_hash)
                VALUES (%s, %s, %s, %s)
                """,
                (user_id, email, username, password_hash)
            )
        return user_id
    finally:
        if conn:
            conn.close()