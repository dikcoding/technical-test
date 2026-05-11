import sqlite3

DB_NAME = "detik.db"

def create_table():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news_articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        url TEXT,
        publish_date TEXT
    )
    """)

    conn.commit()
    conn.close()


def load(cleaned_data):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for data in cleaned_data:
        cursor.execute("""
        INSERT INTO news_articles (
            title,
            url,
            publish_date
        )
        VALUES (?, ?, ?)
        """, (

            data["title"],
            data["url"],
            data["publish_date"]
        ))

    conn.commit()
    conn.close()