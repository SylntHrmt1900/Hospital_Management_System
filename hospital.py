"""
Hospital Management System
Storage: plain .txt files, pipe-delimited (no JSON, no CSV libraries)
"""

import os
import uuid
from datetime import date, datetime

# ─────────────────────────────────────────
#  FILE PATHS  (same folder as this script)
# ─────────────────────────────────────────
BASE      = os.path.dirname(os.path.abspath(__file__))
PAT_FILE  = os.path.join(BASE, "patients.txt")
DOC_FILE  = os.path.join(BASE, "doctors.txt")
APT_FILE  = os.path.join(BASE, "appointments.txt")
BILL_FILE = os.path.join(BASE, "billing.txt")

SEP = "|"   # field separator inside each line


# ─────────────────────────────────────────
#  LOW-LEVEL FILE HELPERS
# ─────────────────────────────────────────

def read_records(filepath):
    """Return list of dicts from a pipe-delimited txt file."""
    records = []
    if not os.path.exists(filepath):
        return records
    with open(filepath, "r") as f:
        lines = f.readlines()
    if len(lines) < 2:          # need at least header + 1 data row
        return records
    headers = lines[0].strip().split(SEP)
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue
        values = line.split(SEP)
        records.append(dict(zip(headers, values)))
    return records


def write_records(filepath, records, headers):
    """Write list of dicts to a pipe-delimited txt file."""
    with open(filepath, "w") as f:
        f.write(SEP.join(headers) + "\n")
        for r in records:
            f.write(SEP.join(str(r.get(h, "")) for h in headers) + "\n")


def append_record(filepath, record, headers):
    """Append one record; creates file with header if it doesn't exist."""
    file_exists = os.path.exists(filepath)
    with open(filepath, "a") as f:
        if not file_exists or os.path.getsize(filepath) == 0:
            f.write(SEP.join(headers) + "\n")
        f.write(SEP.join(str(record.get(h, "")) for h in headers) + "\n")


def new_id(prefix):
    return f"{prefix}-{str(uuid.uuid4())[:8].upper()}"


# ─────────────────────────────────────────
#  DISPLAY HELPERS
# ─────────────────────────────────────────

def bar(title="", w=60):
    if title:
        print(f"\n{'='*4} {title} {'='*(w - len(title) - 6)}")
    else:
        print("-" * w)

def pause():
    input("\n  [Press Enter to continue]")


# ═════════════════════════════════════════
#  PATIENT RECORD MANAGEMENT
# ═════════════════════════════════════════

PAT_HEADERS = ["patient_id","name","age","gender","phone",
               "blood_group","address","medical_history","registered_on"]

def add_patient():
    bar("ADD PATIENT")
    pid  = new_id("PAT")
    name = input("  Full Name       : ").strip()
    age  = input("  Age             : ").strip()
    gen  = input("  Gender (M/F/O)  : ").strip().upper()
    ph   = input("  Phone           : ").strip()
    bg   = input("  Blood Group     : ").strip().upper()
    addr = input("  Address         : ").strip()
    hist = input("  Medical History : ").strip()

    record = {
        "patient_id"     : pid,
        "name"           : name,
        "age"            : age,
        "gender"         : gen,
        "phone"          : ph,
        "blood_group"    : bg,
        "address"        : addr,
        "medical_history": hist,
        "registered_on"  : str(date.today())
    }
    append_record(PAT_FILE, record, PAT_HEADERS)
    print(f"\n  Patient added! ID: {pid}")


def view_all_patients():
    bar("ALL PATIENTS")
    patients = read_records(PAT_FILE)
    if not patients:
        print("  No patients found.")
        return
    print(f"  {'ID':<14} {'Name':<22} {'Age':<5} {'Blood':<7} {'Phone'}")
    bar()
    for p in patients:
        print(f"  {p['patient_id']:<14} {p['name']:<22} {p['age']:<5} "
              f"{p['blood_group']:<7} {p['phone']}")


def search_patient():
    bar("SEARCH PATIENT")
    patients = read_records(PAT_FILE)
    q = input("  Enter Patient ID or Name: ").strip().lower()
    found = [p for p in patients
             if q in p["patient_id"].lower() or q in p["name"].lower()]
    if not found:
        print("  No match found.")
        return
    for p in found:
        bar()
        for k, v in p.items():
            print(f"  {k.replace('_',' ').title():<22}: {v}")


def update_patient():
    bar("UPDATE PATIENT")
    patients = read_records(PAT_FILE)
    pid = input("  Patient ID to update: ").strip().upper()
    for p in patients:
        if p["patient_id"] == pid:
            print("  (Leave blank to keep current value)")
            for field in ["name","age","gender","phone","blood_group","address","medical_history"]:
                val = input(f"  {field.replace('_',' ').title()} [{p[field]}]: ").strip()
                if val:
                    p[field] = val
            write_records(PAT_FILE, patients, PAT_HEADERS)
            print("  Patient record updated.")
            return
    print("  Patient not found.")


def delete_patient():
    bar("DELETE PATIENT")
    patients = read_records(PAT_FILE)
    pid = input("  Patient ID to delete: ").strip().upper()
    new = [p for p in patients if p["patient_id"] != pid]
    if len(new) == len(patients):
        print("  Patient not found.")
    else:
        write_records(PAT_FILE, new, PAT_HEADERS)
        print("  Patient deleted.")


# ═════════════════════════════════════════
#  APPOINTMENT SCHEDULING
# ═════════════════════════════════════════

DOC_HEADERS = ["doctor_id","name","specialty","fee"]
APT_HEADERS = ["appointment_id","patient_id","patient_name","doctor_id",
               "doctor_name","specialty","date","time","reason","status","booked_on"]

DOCTORS_DEFAULT = [
    {"doctor_id":"DOC-001","name":"Dr. Meera Nair",   "specialty":"Cardiology",     "fee":"800"},
    {"doctor_id":"DOC-002","name":"Dr. Arjun Sharma", "specialty":"Neurology",      "fee":"750"},
    {"doctor_id":"DOC-003","name":"Dr. Priya Iyer",   "specialty":"Orthopedics",    "fee":"600"},
    {"doctor_id":"DOC-004","name":"Dr. Rohan Menon",  "specialty":"Dermatology",    "fee":"500"},
    {"doctor_id":"DOC-005","name":"Dr. Kavita Rao",   "specialty":"Pediatrics",     "fee":"450"},
    {"doctor_id":"DOC-006","name":"Dr. Suresh Gupta", "specialty":"General Medicine","fee":"350"},
]

def seed_doctors():
    if not os.path.exists(DOC_FILE) or os.path.getsize(DOC_FILE) == 0:
        write_records(DOC_FILE, DOCTORS_DEFAULT, DOC_HEADERS)


def view_doctors():
    bar("AVAILABLE DOCTORS")
    doctors = read_records(DOC_FILE)
    print(f"  {'ID':<10} {'Name':<25} {'Specialty':<20} {'Fee'}")
    bar()
    for d in doctors:
        print(f"  {d['doctor_id']:<10} {d['name']:<25} {d['specialty']:<20} Rs.{d['fee']}")


def schedule_appointment():
    bar("SCHEDULE APPOINTMENT")
    patients = read_records(PAT_FILE)
    doctors  = read_records(DOC_FILE)
    if not patients:
        print("  Add a patient first.")
        return

    pid = input("  Patient ID: ").strip().upper()
    patient = next((p for p in patients if p["patient_id"] == pid), None)
    if not patient:
        print("  Patient not found.")
        return

    view_doctors()
    did = input("\n  Doctor ID: ").strip().upper()
    doctor = next((d for d in doctors if d["doctor_id"] == did), None)
    if not doctor:
        print("  Doctor not found.")
        return

    dt     = input("  Date (YYYY-MM-DD)  : ").strip()
    tm     = input("  Time (HH:MM, 24h)  : ").strip()
    reason = input("  Reason for Visit   : ").strip()

    record = {
        "appointment_id": new_id("APT"),
        "patient_id"    : pid,
        "patient_name"  : patient["name"],
        "doctor_id"     : did,
        "doctor_name"   : doctor["name"],
        "specialty"     : doctor["specialty"],
        "date"          : dt,
        "time"          : tm,
        "reason"        : reason,
        "status"        : "Scheduled",
        "booked_on"     : datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    append_record(APT_FILE, record, APT_HEADERS)
    print(f"\n  Appointment scheduled! ID: {record['appointment_id']}")


def view_appointments():
    bar("ALL APPOINTMENTS")
    appts = read_records(APT_FILE)
    if not appts:
        print("  No appointments found.")
        return
    print(f"  {'Appt ID':<13} {'Patient':<20} {'Doctor':<22} {'Date':<12} {'Time':<7} Status")
    bar()
    for a in appts:
        print(f"  {a['appointment_id']:<13} {a['patient_name']:<20} {a['doctor_name']:<22} "
              f"{a['date']:<12} {a['time']:<7} {a['status']}")


def cancel_appointment():
    bar("CANCEL APPOINTMENT")
    appts = read_records(APT_FILE)
    aid = input("  Appointment ID to cancel: ").strip().upper()
    for a in appts:
        if a["appointment_id"] == aid:
            a["status"] = "Cancelled"
            write_records(APT_FILE, appts, APT_HEADERS)
            print("  Appointment cancelled.")
            return
    print("  Appointment not found.")


# ═════════════════════════════════════════
#  BILLING
# ═════════════════════════════════════════

BILL_HEADERS = ["bill_id","patient_id","patient_name","appointment_id",
                "doctor_name","date","services","subtotal","tax","grand_total","status"]

SERVICES = {
    "1": ("Blood Test",    300),
    "2": ("X-Ray",         500),
    "3": ("ECG",           400),
    "4": ("MRI Scan",     2500),
    "5": ("CT Scan",      2000),
    "6": ("Physiotherapy", 600),
    "7": ("Room Charges",  800),
    "8": ("Medicines",       0),   # custom amount
}

TAX = 0.05


def generate_bill():
    bar("GENERATE BILL")
    patients = read_records(PAT_FILE)
    appts    = read_records(APT_FILE)
    doctors  = read_records(DOC_FILE)

    pid = input("  Patient ID: ").strip().upper()
    patient = next((p for p in patients if p["patient_id"] == pid), None)
    if not patient:
        print("  Patient not found.")
        return

    active = [a for a in appts if a["patient_id"] == pid and a["status"] == "Scheduled"]
    if not active:
        print("  No active (Scheduled) appointments for this patient.")
        return

    print(f"\n  Appointments for {patient['name']}:")
    for i, a in enumerate(active, 1):
        print(f"  {i}. {a['appointment_id']}  {a['doctor_name']}  {a['date']} {a['time']}")
    idx   = int(input("  Select number: ")) - 1
    appt  = active[idx]
    doctor = next((d for d in doctors if d["doctor_id"] == appt["doctor_id"]), None)

    # Consultation is always first
    consult_fee = int(doctor["fee"]) if doctor else 350
    items = [("Consultation", consult_fee)]
    total = consult_fee

    # Additional services
    print("\n  Additional Services:")
    for k, (name, cost) in SERVICES.items():
        label = f"Rs.{cost}" if cost else "custom"
        print(f"    {k}. {name:<18} {label}")
    sel = input("\n  Enter numbers (comma-separated, blank to skip): ").strip()
    if sel:
        for code in sel.split(","):
            code = code.strip()
            if code in SERVICES:
                sname, scost = SERVICES[code]
                if scost == 0:
                    scost = float(input(f"  Amount for {sname}: Rs."))
                items.append((sname, scost))
                total += scost

    tax   = round(total * TAX, 2)
    grand = round(total + tax, 2)

    # Encode items as a single string: "Consultation:800;Blood Test:300"
    items_str = ";".join(f"{name}:{amt}" for name, amt in items)

    bill = {
        "bill_id"       : new_id("BILL"),
        "patient_id"    : pid,
        "patient_name"  : patient["name"],
        "appointment_id": appt["appointment_id"],
        "doctor_name"   : appt["doctor_name"],
        "date"          : str(date.today()),
        "services"      : items_str,
        "subtotal"      : total,
        "tax"           : tax,
        "grand_total"   : grand,
        "status"        : "Unpaid"
    }
    append_record(BILL_FILE, bill, BILL_HEADERS)

    # Mark appointment as Completed
    for a in appts:
        if a["appointment_id"] == appt["appointment_id"]:
            a["status"] = "Completed"
    write_records(APT_FILE, appts, APT_HEADERS)

    print_bill(bill)


def print_bill(bill):
    w = 58
    # Parse services back from the stored string
    services = []
    for entry in bill["services"].split(";"):
        if ":" in entry:
            name, amt = entry.rsplit(":", 1)
            services.append((name, float(amt)))

    print("\n" + "=" * w)
    print(f"{'CITY CARE HOSPITAL':^{w}}")
    print(f"{'123, MG Road, Bangalore - 560001':^{w}}")
    print(f"{'Ph: +91-80-12345678':^{w}}")
    print("=" * w)
    print(f"  Bill ID    : {bill['bill_id']}")
    print(f"  Date       : {bill['date']}")
    print(f"  Patient    : {bill['patient_name']}  ({bill['patient_id']})")
    print(f"  Doctor     : {bill['doctor_name']}")
    print(f"  Appt ID    : {bill['appointment_id']}")
    print("-" * w)
    print(f"  {'SERVICE':<35} {'AMOUNT':>10}")
    print("-" * w)
    for name, amt in services:
        print(f"  {name:<35} Rs.{amt:>7.2f}")
    print("-" * w)
    print(f"  {'Subtotal':<35} Rs.{float(bill['subtotal']):>7.2f}")
    print(f"  {'GST (5%)':<35} Rs.{float(bill['tax']):>7.2f}")
    print("=" * w)
    print(f"  {'GRAND TOTAL':<35} Rs.{float(bill['grand_total']):>7.2f}")
    print("=" * w)
    print(f"  Status: {bill['status']}")
    print("=" * w)


def view_all_bills():
    bar("ALL BILLS")
    bills = read_records(BILL_FILE)
    if not bills:
        print("  No bills found.")
        return
    print(f"  {'Bill ID':<13} {'Patient':<20} {'Date':<12} {'Total':>10}  Status")
    bar()
    for b in bills:
        print(f"  {b['bill_id']:<13} {b['patient_name']:<20} {b['date']:<12} "
              f"Rs.{float(b['grand_total']):>7.2f}  {b['status']}")


def view_bill_by_id():
    bar("VIEW BILL")
    bills = read_records(BILL_FILE)
    bid = input("  Bill ID: ").strip().upper()
    bill = next((b for b in bills if b["bill_id"] == bid), None)
    if not bill:
        print("  Bill not found.")
        return
    print_bill(bill)


def mark_paid():
    bar("MARK BILL AS PAID")
    bills = read_records(BILL_FILE)
    bid = input("  Bill ID: ").strip().upper()
    for b in bills:
        if b["bill_id"] == bid:
            b["status"] = "Paid"
            write_records(BILL_FILE, bills, BILL_HEADERS)
            print("  Bill marked as Paid.")
            return
    print("  Bill not found.")


# ═════════════════════════════════════════
#  MENUS
# ═════════════════════════════════════════

def patient_menu():
    while True:
        bar("PATIENT RECORDS")
        print("  1. Add New Patient")
        print("  2. View All Patients")
        print("  3. Search Patient")
        print("  4. Update Patient")
        print("  5. Delete Patient")
        print("  0. Back")
        ch = input("\n  Choice: ").strip()
        if   ch == "1": add_patient()
        elif ch == "2": view_all_patients()
        elif ch == "3": search_patient()
        elif ch == "4": update_patient()
        elif ch == "5": delete_patient()
        elif ch == "0": break
        else: print("  Invalid choice.")
        pause()


def appointment_menu():
    while True:
        bar("APPOINTMENTS")
        print("  1. View Doctors")
        print("  2. Schedule Appointment")
        print("  3. View All Appointments")
        print("  4. Cancel Appointment")
        print("  0. Back")
        ch = input("\n  Choice: ").strip()
        if   ch == "1": view_doctors()
        elif ch == "2": schedule_appointment()
        elif ch == "3": view_appointments()
        elif ch == "4": cancel_appointment()
        elif ch == "0": break
        else: print("  Invalid choice.")
        pause()


def billing_menu():
    while True:
        bar("BILLING")
        print("  1. Generate Bill")
        print("  2. View All Bills")
        print("  3. View Bill by ID")
        print("  4. Mark Bill as Paid")
        print("  0. Back")
        ch = input("\n  Choice: ").strip()
        if   ch == "1": generate_bill()
        elif ch == "2": view_all_bills()
        elif ch == "3": view_bill_by_id()
        elif ch == "4": mark_paid()
        elif ch == "0": break
        else: print("  Invalid choice.")
        pause()


def main():
    seed_doctors()
    while True:
        print("\n")
        print("  +==========================================+")
        print("  |    CITY CARE HOSPITAL SYSTEM            |")
        print("  +==========================================+")
        print("  |  1. Patient Records                     |")
        print("  |  2. Appointments                        |")
        print("  |  3. Billing                             |")
        print("  |  0. Exit                                |")
        print("  +==========================================+")
        ch = input("\n  Select: ").strip()
        if   ch == "1": patient_menu()
        elif ch == "2": appointment_menu()
        elif ch == "3": billing_menu()
        elif ch == "0":
            print("\n  Goodbye!\n")
            break
        else:
            print("  Invalid choice.")


if __name__ == "__main__":
    main()
