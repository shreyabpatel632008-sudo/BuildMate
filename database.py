import sqlite3
import os
from datetime import datetime

DB_NAME = "data/buildmate.db"


def connect():
    os.makedirs("data", exist_ok=True)
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT,
            topic TEXT,
            content TEXT,
            status TEXT DEFAULT 'Pending',
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS replies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            platform TEXT,
            original_comment TEXT NOT NULL,
            reply TEXT NOT NULL,
            status TEXT DEFAULT 'Pending',
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS discovered_topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT UNIQUE NOT NULL,
            category TEXT,
            source TEXT,
            link TEXT,
            summary TEXT,
            score INTEGER,
            published TEXT,
            discovered_at TEXT NOT NULL
        )
    """)

    # Add image_path to existing posts without deleting old records.
    cursor.execute("PRAGMA table_info(posts)")
    columns = [column[1] for column in cursor.fetchall()]

    if "image_path" not in columns:
        cursor.execute(
            "ALTER TABLE posts ADD COLUMN image_path TEXT"
        )

    conn.commit()
    conn.close()


def save_post(platform, topic, content, image_path=None):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO posts
        (platform, topic, content, created_at, image_path)
        VALUES (?, ?, ?, ?, ?)
    """, (
        platform,
        topic,
        content,
        datetime.now().isoformat(),
        image_path
    ))

    conn.commit()
    conn.close()


def get_posts():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts ORDER BY id DESC")
    posts = cursor.fetchall()

    conn.close()
    return posts


def update_post_status(post_id, status):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE posts SET status = ? WHERE id = ?",
        (status, post_id)
    )

    conn.commit()
    conn.close()


def save_reply(platform, comment, reply):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO replies
        (platform, original_comment, reply, created_at)
        VALUES (?, ?, ?, ?)
    """, (
        platform,
        comment,
        reply,
        datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()


def get_replies():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM replies ORDER BY id DESC")
    replies = cursor.fetchall()

    conn.close()
    return replies


def save_topic(topic):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO discovered_topics
        (title, category, source, link, summary, score,
         published, discovered_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        topic["title"],
        topic["category"],
        topic["source"],
        topic["link"],
        topic["summary"],
        topic["score"],
        topic["published"],
        datetime.now().isoformat()
    ))

    saved = cursor.rowcount == 1

    conn.commit()
    conn.close()

    return saved


def get_topics():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM discovered_topics
        ORDER BY score DESC, id DESC
    """)

    topics = cursor.fetchall()

    conn.close()
    return topics