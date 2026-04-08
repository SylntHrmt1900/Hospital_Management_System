# Hospital_Management_System
A Python-based Hospital Management System designed for small clinics to digitize patient records, manage doctor appointments, and automate billing processes using a lightweight, file-based database.

## 📋 Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Team Members](#team-members)
- [Future Improvements](#future-improvements)

## 🌟 Overview
[cite_start]This project provides a lightweight and portable digital solution for outpatient clinics that currently rely on paper registers or spreadsheets. [cite: 20, 633] [cite_start]It focuses on reducing administrative burden, improving data accuracy, and eliminating manual billing errors. [cite: 24, 637]

## ✨ Key Features
- [cite_start]**Patient Record Management:** Add, search, update, and delete patient information with unique UUID-based identification. [cite: 46, 47]
- [cite_start]**Appointment Scheduling:** Book and cancel appointments with specialized doctors while maintaining a persistent booking history. [cite: 49, 50]
- [cite_start]**Automated Billing:** Generate professional invoices including consultation fees, diagnostic services, and automated GST (5%) calculation. [cite: 51, 167]
- [cite_start]**File-Based Persistence:** Data is stored in pipe-delimited text files (`.txt`), ensuring portability without requiring a database installation. [cite: 23, 43]

## 🏗️ System Architecture
[cite_start]The system is built using a modular design with four primary data storage files: [cite: 44]
- `patients.txt`: Stores demographics and medical history.
- `doctors.txt`: Maintains a roster of available doctors and their fees.
- `appointments.txt`: Tracks all scheduled and completed visits.
- `billing.txt`: Records all financial transactions and payment statuses.

## 🚀 Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/hospital-management-system.git](https://github.com/your-username/hospital-management-system.git)
