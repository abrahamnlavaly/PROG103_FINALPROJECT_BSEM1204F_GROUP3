import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("records.db")
cursor = conn.cursor()

cursor.execute("""
SELECT status,
COUNT(*)
FROM records
GROUP BY status
""")

data = cursor.fetchall()

status = [x[0] for x in data]
count = [x[1] for x in data]

plt.bar(status,count)

plt.title("Records By Status")

plt.show()
plt.pie(
    count,
    labels=status,
    autopct="%1.1f%%"
)

plt.show()
cursor.execute("""
SELECT created_date,
COUNT(*)
FROM records
GROUP BY created_date
""")

data = cursor.fetchall()

dates = [x[0] for x in data]
counts = [x[1] for x in data]

plt.plot(dates,counts)

plt.title("Registration Trend")

plt.show()