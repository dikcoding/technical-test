import sqlite3

DB_NAME = "detik.db"

def query_last_7_days():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM news_articles
    WHERE publish_date >= DATE('now', '-7 days')
    """)

    rows = cursor.fetchall()

    print("\nNEWS FROM LAST 7 DAYS:\n")

    for row in rows:
        print(row)

    conn.close()