# Hospital Management System

A Python-based Hospital Management System designed for small clinics to digitize patient records, manage doctor appointments, and automate billing processes using a lightweight, file-based database.

## 📋 Overview
[cite_start]This project digitizes core clinic workflows to replace manual, error-prone paper registers with structured digital storage[cite: 1, 3]. [cite_start]It provides a lightweight solution for outpatient clinics to manage data accurately and efficiently without the need for a complex database installation[cite: 1, 3].

## 👥 Student Team Members (Alliance University)
* [cite_start]**Pranav Adhithya R** [cite: 1, 3]
* [cite_start]**Tuhin V** [cite: 1, 3]
* [cite_start]**Srujana CM** [cite: 1, 3]
* [cite_start]**Sanjitha** [cite: 1, 3]
* [cite_start]**Rahul G** [cite: 1, 3]
* [cite_start]**Ayyappa** [cite: 1, 3]

## ✨ Key Features
* [cite_start]**Patient Record Management:** Register new patients, search records by name or ID, and update or delete entries[cite: 1].
* [cite_start]**Appointment Scheduling:** View available doctors and schedule or cancel appointments[cite: 1].
* [cite_start]**Automated Billing:** Generate itemized invoices including consultation fees and additional diagnostic services with automated 5% GST calculation[cite: 1].
* [cite_start]**Persistent Storage:** Uses pipe-delimited (`|`) text files to ensure data is saved across sessions while remaining portable[cite: 1, 3].

## 🏗️ System Architecture
[cite_start]The application is structured into independent modules that interact with four primary text files[cite: 1]:
* [cite_start]`patients.txt`: Stores demographics and medical history[cite: 1].
* [cite_start]`doctors.txt`: Maintains a roster of available doctors and their fees[cite: 1].
* [cite_start]`appointments.txt`: Tracks all scheduled visits and their status[cite: 1].
* [cite_start]`billing.txt`: Records all financial transactions and invoices[cite: 1].

## 🚀 Getting Started
1. [cite_start]**Prerequisites:** Ensure you have Python 3.x installed[cite: 1].
2. **Run the Application:** Execute the main script via terminal:
    ```bash
    python hospital.py
    ```
3. [cite_start]**Navigation:** Use the numerical menu options to access Patient Records, Appointments, or Billing[cite: 1].

## 🛠️ Resources Used
* [cite_start]**Source Code:** [hospital.py](https://github.com/SylntHrmt1900/Hospital_Management_System/blob/main/hospital.py) [cite: 2]
* [cite_start]**Project Report:** [Python_Microproject_Report.docx](https://github.com/SylntHrmt1900/Hospital_Management_System/blob/main/Python_Microproject_Report.docx) [cite: 1]
* [cite_start]**Project Proposal:** [Python_Proposal.docx](https://github.com/SylntHrmt1900/Hospital_Management_System/blob/main/Python_Proposal.docx) [cite: 3]
* [cite_start]**Libraries:** `os`, `uuid`, `datetime` (Standard Python Library)[cite: 1, 2].
* [cite_start]**IDE:** Visual Studio Code[cite: 1, 3].

## 📈 Future Improvements
* [cite_start]Migration from flat text files to a relational database like MySQL or SQLite for concurrent access[cite: 1, 3].
* [cite_start]Development of a Graphical User Interface (GUI) using Tkinter[cite: 1, 3].
* [cite_start]Integration of automated SMS/Email appointment reminders[cite: 1].
