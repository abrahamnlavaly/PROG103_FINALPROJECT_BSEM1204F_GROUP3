import sqlite3
from datetime import datetime

conn = sqlite3.connect("records.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS records(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    gender TEXT,
    status TEXT,
    contact TEXT,
    created_date TEXT
)
""")

cursor.execute("SELECT COUNT(*) FROM records")
count = cursor.fetchone()[0]

if count == 0:

    for i in range(1, 21):

        gender = "Male" if i % 2 == 0 else "Female"

        if i % 3 == 0:
            status = "Inactive"
        elif i % 5 == 0:
            status = "Pending"
        else:
            status = "Active"

        cursor.execute("""
        INSERT INTO records
        (full_name, gender, status, contact, created_date)
        VALUES (?,?,?,?,?)
        """,
        (
            f"Student {i}",
            gender,
            status,
            f"07600000{i}",
            datetime.now().strftime("%Y-%m-%d")
        ))

conn.commit()
conn.close()

print("Database Ready")