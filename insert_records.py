import sqlite3
from datetime import datetime

conn = sqlite3.connect("records.db")
cursor = conn.cursor()

for i in range(1, 21):
    cursor.execute("""
    INSERT INTO records
    (full_name, gender, status, contact, created_date)
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        f"Student {i}",
        "Male" if i % 2 == 0 else "Female",
        "Active",
        f"07600000{i}",
        datetime.now().strftime("%Y-%m-%d")
    ))

conn.commit()
conn.close()

print("20 Records Added")