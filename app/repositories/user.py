from psycopg.types.json import Json
from psycopg.rows import dict_row
from app.db.connection import get_db_connection

class UserRepository:
    @staticmethod
    def create_user(data: dict) -> dict:
        conn = get_db_connection()
        try:
            with conn.cursor(row_factory=dict_row) as cur:
                cur.execute(
                    """ INSERT INTO users (email_address, username, profile_payload, phone_number, password) 
                    VALUES (%(email_address)s, %(username)s, %(profile_payload)s, %(phone_number)s ,%(password)s) 
                    RETURNING   
                        id,
                        email_address,
                        username,
                        profile_payload,
                        phone_number,
                        created_at """
                    ,{**data, "profile_payload": Json(data.get("profile_payload", {}))}
                )
                
                # conn.commit()  - bcz conn.autocommit = True h 
                # return dict(zip(
                #     ["id","email_address","username","profile_payload","phone_number","created_at"],
                #     cur.fetchone()
                # ))
                return cur.fetchone()
        finally:
            conn.close()