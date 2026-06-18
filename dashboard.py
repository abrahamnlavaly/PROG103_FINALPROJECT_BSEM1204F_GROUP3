from tkinter import *
from tkinter import ttk
import sqlite3
import matplotlib.pyplot as plt
import reports


root = Tk()
root.title("Dashboard")
root.geometry("1000x600")


def load_records():

    for row in tree.get_children():
        tree.delete(row)

    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records")

    data = cursor.fetchall()

    for row in data:
        tree.insert("", END, values=row)

    conn.close()


def search_record():

    keyword = search_entry.get()

    for row in tree.get_children():
        tree.delete(row)

    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM records
        WHERE full_name LIKE ?
        """,
        ('%' + keyword + '%',)
    )

    data = cursor.fetchall()

    for row in data:
        tree.insert("", END, values=row)

    conn.close()


def filter_gender():

    gender = gender_var.get()

    for row in tree.get_children():
        tree.delete(row)

    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT * FROM records
        WHERE gender=?
        """,
        (gender,)
    )

    data = cursor.fetchall()

    for row in data:
        tree.insert("", END, values=row)

    conn.close()


def show_bar_chart():

    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT status, COUNT(*)
    FROM records
    GROUP BY status
    """)

    data = cursor.fetchall()

    conn.close()

    status = [x[0] for x in data]
    count = [x[1] for x in data]

    plt.bar(status, count)
    plt.title("Records By Status")
    plt.show()


def show_pie_chart():

    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT gender, COUNT(*)
    FROM records
    GROUP BY gender
    """)

    data = cursor.fetchall()

    conn.close()

    gender = [x[0] for x in data]
    count = [x[1] for x in data]

    plt.pie(
        count,
        labels=gender,
        autopct="%1.1f%%"
    )

    plt.title("Gender Distribution")
    plt.show()


def show_line_chart():

    conn = sqlite3.connect("records.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT created_date, COUNT(*)
    FROM records
    GROUP BY created_date
    """)

    data = cursor.fetchall()

    conn.close()

    dates = [x[0] for x in data]
    count = [x[1] for x in data]

    plt.plot(dates, count)

    plt.title("Registration Trend")
    plt.show()


def generate_report():

    reports.generate_pdf()


Label(
    root,
    text="Student Records Dashboard",
    font=("Arial", 18)
).pack()

search_entry = Entry(root)
search_entry.pack()

Button(
    root,
    text="Search",
    command=search_record
).pack()

gender_var = StringVar()
gender_var.set("Male")

OptionMenu(
    root,
    gender_var,
    "Male",
    "Female"
).pack()

Button(
    root,
    text="Filter Gender",
    command=filter_gender
).pack()

tree = ttk.Treeview(root)

tree["columns"] = (
    "ID",
    "Name",
    "Gender",
    "Status",
    "Contact",
    "Date"
)

tree.column("#0", width=0)

for col in tree["columns"]:
    tree.heading(col, text=col)

tree.pack(fill=BOTH, expand=True)

Button(
    root,
    text="Bar Chart",
    command=show_bar_chart
).pack(side=LEFT, padx=10)

Button(
    root,
    text="Pie Chart",
    command=show_pie_chart
).pack(side=LEFT, padx=10)

Button(
    root,
    text="Line Graph",
    command=show_line_chart
).pack(side=LEFT, padx=10)

Button(
    root,
    text="Generate PDF",
    command=generate_report
).pack(side=LEFT, padx=10)

load_records()

root.mainloop()