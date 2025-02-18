"""Base Database"""

from os import environ
from uuid import UUID

from werkzeug.security import generate_password_hash
from sqlite_database import Database
from sqlite_database.errors import DatabaseExistsError
from dotenv import load_dotenv

from .users import USER_SCHEMA, VAL_VISIBILITY as USER_DATA_VISIBILITY
from .posts import POSTS_SCHEMA


load_dotenv()
DB_PATH = environ.get("DB_PATH", "transient/db.sqlite3")

db = Database(DB_PATH)

try:
    db.check_table("users")
    users_tbl = db.create_table("users", USER_SCHEMA)
    posts_tbl = db.create_table("posts", POSTS_SCHEMA)
    users_tbl.insert(
        {
            "uid": str(UUID(int=0)),
            "username": "admin",
            "display_name": "System Administrator",
            "password": generate_password_hash("admin123"),
            'role': 'admin'
        }
    )
except DatabaseExistsError:
    users_tbl = db.table("users")
    posts_tbl = db.table("posts")
