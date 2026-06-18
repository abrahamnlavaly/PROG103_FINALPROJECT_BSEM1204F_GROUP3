import sqlite3
from reportlab.platypus import SimpleDocTemplate, Table


def generate_pdf():

    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records")

    records = cursor.fetchall()

    conn.close()

    pdf = SimpleDocTemplate("Records_Report.pdf")

    data = [
        [
            "ID",
            "Name",
            "Gender",
            "Status",
            "Contact",
            "Date"
        ]
    ]

    for row in records:
        data.append(list(row))

    table = Table(data)

    pdf.build([table])

    print("PDF Generated")