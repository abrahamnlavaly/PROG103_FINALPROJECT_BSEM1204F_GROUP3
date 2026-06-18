# PROG103_FINALPROJECT_BSEM1204F_GROUP3

## Student Records Management System

### Final Group Project – PROG103

This project was developed as part of the requirements for **PROG103 – Principles of Structured Programming**.

The application is a **Student Records Management System** built using Python. It allows users to manage student records, search and filter information, visualize data using charts, and generate PDF reports.

---

## Features

### User Authentication

* Login Page
* Username and Password Validation
* Error Handling for Invalid Credentials
* Forgot Password Functionality

### Records Management

The system stores and displays student records containing:

* Record ID
* Full Name
* Gender
* Status
* Contact Information
* Date Created

The database is preloaded with at least 20 sample records.

### Dashboard

The dashboard provides:

* Record Display
* Search Functionality
* Gender Filtering
* Record Management Interface

### Data Visualization

The system includes graphical reports using Matplotlib:

#### Bar Chart

Displays:

* Number of Records by Status

#### Pie Chart

Displays:

* Gender Distribution

#### Line Graph

Displays:

* Record Registration Trends

### PDF Report Generation

Users can generate PDF reports containing:

* Student Records
* Record Information
* Report Tables

Generated reports are saved as PDF files for easy sharing and printing.

---

## Technologies Used

* Python
* Tkinter
* SQLite3
* Matplotlib
* ReportLab

---

## Project Structure

```text
PROG103_FINALPROJECT_BSEM1204F_GROUP3
│
├── database.py
├── login.py
├── dashboard.py
├── reports.py
├── insert_records.py
├── charts.py
├── records.db
├── README.md
└── .gitignore
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/abrahamnlavaly/PROG103_FINALPROJECT_BSEM1204F_GROUP3.git
```

### Install Required Packages

```bash
pip install matplotlib reportlab
```

---

## Running the Application

### Step 1 – Create the Database

```bash
python database.py
```

### Step 2 – Launch the Application

```bash
python login.py
```

### Default Login Credentials

Username:

```text
admin
```

Password:

```text
1234
```

---

## Deliverables Implemented

✅ Login Page

✅ User Authentication

✅ Display of 20+ Records

✅ Dashboard Interface

✅ Search Functionality

✅ Gender Filter

✅ SQLite Database Integration

✅ Bar Chart Visualization

✅ Pie Chart Visualization

✅ Line Graph Visualization

✅ PDF Report Generation

---

## Future Improvements

* Status Filtering
* Date Filtering
* Weekly Reports
* Monthly Reports
* Yearly Reports
* Enhanced Dashboard Analytics
* Record Editing and Deletion

---

## Course Information

**Course:** PROG103 – Principles of Structured Programming

**Project Type:** Final Group Project

**Group:** BSEM1204F Group 3

**Academic Year:** 2026

---

## Authors

BSEM1204F Group 3
