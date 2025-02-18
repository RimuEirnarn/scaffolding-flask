"""Users db model"""
from sqlite_database import text

USER_SCHEMA = [
    text("uid").primary(),
    text("display_name"),
    text('username').unique(),
    text('password'),
    text('role').default("user")
]

VAL_VISIBILITY = (
    'username',
    'display_name',
    'uid',
    'role'
)