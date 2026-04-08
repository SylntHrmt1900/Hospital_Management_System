# Hospital Management System

A Python-based Hospital Management System designed for small clinics to digitize patient records, manage doctor appointments, and automate billing processes using a lightweight, file-based database.

## 📋 Overview
This project digitizes core clinic workflows to replace manual, error-prone paper registers with structured digital storage. It provides a lightweight solution for outpatient clinics to manage data accurately and efficiently without the need for a complex database installation.

## 👥 Student Team Members (Alliance University)
* **Pranav Adhithya R**
* **Tuhin V**
* **Srujana CM**
* **Sanjitha**
* **Rahul G**
* **Ayyappa**

## ✨ Key Features
* **Patient Record Management:** Register new patients, search records by name or ID, and update or delete entries.
* **Appointment Scheduling:** View available doctors and schedule or cancel appointments.
* **Automated Billing:** Generate itemized invoices including consultation fees and additional diagnostic services with automated 5% GST calculation.
* **Persistent Storage:** Uses pipe-delimited (`|`) text files to ensure data is saved across sessions while remaining portable.

## 🏗️ System Architecture
The application is structured into independent modules that interact with four primary text files:
* `patients.txt`: Stores demographics and medical history.
* `doctors.txt`: Maintains a roster of available doctors and their fees.
* `appointments.txt`: Tracks all scheduled visits and their status.
* `billing.txt`: Records all financial transactions and invoices.

## 🚀 Getting Started
1. **Prerequisites:** Ensure you have Python 3.x installed.
2. **Run the Application:** Execute the main script via terminal:
    ```bash
    python hospital.py
    ```
3. **Navigation:** Use the numerical menu options to access Patient Records, Appointments, or Billing.

## 🛠️ Resources Used
* **Source Code:** [hospital.py](https://github.com/SylntHrmt1900/Hospital_Management_System/blob/main/hospital.py)
* **Project Report:** [Python_Microproject_Report.docx](https://github.com/SylntHrmt1900/Hospital_Management_System/blob/main/Python_Microproject_Report.docx)
* **Project Proposal:** [Python_Proposal.docx](https://github.com/SylntHrmt1900/Hospital_Management_System/blob/main/Python_Proposal.docx)
* **Libraries:** `os`, `uuid`, `datetime` (Standard Python Library)
* **IDE:** Visual Studio Code

## 📈 Future Improvements
* Migration from flat text files to a relational database like MySQL or SQLite for concurrent access.
* Development of a Graphical User Interface (GUI) using Tkinter.
* Integration of automated SMS/Email appointment reminders.
