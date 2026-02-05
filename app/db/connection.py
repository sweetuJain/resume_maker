from typing import Any
import psycopg
from psycopg import Connection 
import logging
from app.core.config import get_settings
settings = get_settings()
logger = logging.getLogger(__name__)

def get_db_connection() -> Connection[Any]:
    try : 
        conn = psycopg.connect(
            host=settings.DB_HOST,
            port=settings.DB_PORT,
            dbname=settings.DB_NAME,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            sslmode="prefer",   # prod safe
        )
        conn.autocommit = True # har query ke baad commit kar dega - transactions ke liye nahi hai - simple queries ke liye hai - read/write operations ke liye hai - performance improve karega - data integrity ke liye theek hai - multiple connections handle kar sakta hai - suitable for web apps
        logger.debug("psycopg3 DB connection successfully")
        return conn
    except Exception as e: 
        logger.exception(f"Failed to connect to DB : {e}")
        raise
