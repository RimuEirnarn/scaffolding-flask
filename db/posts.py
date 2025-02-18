"""Posts db"""
from sqlite_database import real, text

POSTS_SCHEMA = [
    text('post_id').primary(),
    text('author_id').foreign('users/uid').on_delete('cascade'),
    text("title"),
    text('content'),
    real('created_at'),
    real('updated_at')
]
