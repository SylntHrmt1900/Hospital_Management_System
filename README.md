# Hospital_Management_System
A Python-based Hospital Management System designed for small clinics to digitize patient records, manage doctor appointments, and automate billing processes using a lightweight, file-based database.

## 📋 Overview
[cite_start]This project digitizes core clinic workflows to replace manual, error-prone paper registers with structured digital storage[cite: 20, 165]. [cite_start]It provides a lightweight solution for outpatient clinics to manage data accurately and efficiently without the need for a complex database installation[cite: 23, 39].

## 👥 Student Team Members (Alliance University)
* [cite_start]**Pranav Adhithya R** [cite: 10, 623]
* [cite_start]**Tuhin V** [cite: 11, 624]
* [cite_start]**Srujana CM** [cite: 12, 626]
* [cite_start]**Sanjitha** [cite: 13, 625]
* [cite_start]**Rahul G** [cite: 14, 628]
* [cite_start]**Ayyappa** [cite: 15, 627]

## ✨ Key Features
* [cite_start]**Patient Record Management:** Register new patients, search records by name or ID, and update or delete entries[cite: 46, 632].
* [cite_start]**Appointment Scheduling:** View available doctors and schedule or cancel appointments[cite: 49, 50, 632].
* [cite_start]**Automated Billing:** Generate itemized invoices including consultation fees and additional diagnostic services with automated 5% GST calculation[cite: 51, 652].
* [cite_start]**Persistent Storage:** Uses pipe-delimited (`|`) text files to ensure data is saved across sessions while remaining portable[cite: 43, 44].

## 🏗️ System Architecture
[cite_start]The application is structured into independent modules that interact with four primary text files[cite: 44, 45]:
* [cite_start]`patients.txt`: Stores demographics and medical history[cite: 44].
* [cite_start]`doctors.txt`: Maintains a roster of available doctors and their fees[cite: 44].
* [cite_start]`appointments.txt`: Tracks all scheduled visits and their status[cite: 44].
* [cite_start]`billing.txt`: Records all financial transactions and invoices[cite: 44].

## 🚀 Getting Started
1.  [cite_start]**Prerequisites:** Ensure you have Python 3.x installed[cite: 56].
2.  **Run the Application:** Execute the main script via terminal:
    ```bash
    python hospital.py
    ```
3.  [cite_start]**Navigation:** Use the numerical menu options to access Patient Records, Appointments, or Billing[cite: 53, 59].

## 🛠️ Resources Used
* [cite_start]**Language:** Python 3.x[cite: 56, 186].
* [cite_start]**Libraries:** `os`, `uuid`, `datetime` (Standard Python Library)[cite: 56, 186, 187, 188].
* [cite_start]**IDE:** Visual Studio Code[cite: 56].

## 📈 Future Improvements
* [cite_start]Migration from flat text files to a relational database like MySQL or SQLite for concurrent access[cite: 170].
* [cite_start]Development of a Graphical User Interface (GUI) using Tkinter[cite: 171].
* [cite_start]Integration of automated SMS/Email appointment reminders[cite: 172].
