import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk

# ---------------- MySQL Connection ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pass",
    database="hospital_db"
)
cursor = conn.cursor()

# ---------------- Tkinter App ----------------
root = Tk()
root.title("Hospital Management System")
root.geometry("1000x700")
root.config(bg="skyblue")

# ---------------- Functions ----------------

# --- Patient Registration ---
def open_patient_registration():
    reg_window = Toplevel(root)
    reg_window.title("Patient Registration")
    reg_window.geometry("400x400")
    reg_window.configure(bg="lightblue")

    Label(reg_window, text="Patient Registration", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

    Label(reg_window, text="Name:", bg="lightblue").pack()
    name_entry = Entry(reg_window, width=30)
    name_entry.pack(pady=5)

    Label(reg_window, text="Age:", bg="lightblue").pack()
    age_entry = Entry(reg_window, width=30)
    age_entry.pack(pady=5)

    Label(reg_window, text="Gender:", bg="lightblue").pack()
    gender_var = StringVar()
    gender_var.set("Select")
    OptionMenu(reg_window, gender_var, "Male", "Female", "Other").pack(pady=5)

    Label(reg_window, text="Phone:", bg="lightblue").pack()
    phone_entry = Entry(reg_window, width=30)
    phone_entry.pack(pady=5)

    def save_patient():
        name = name_entry.get()
        age = age_entry.get()
        gender = gender_var.get()
        phone = phone_entry.get()
        if name and age and gender != "Select" and phone:
            query = "INSERT INTO patients (name, age, gender, phone) VALUES (%s, %s, %s, %s)"
            values = (name, age, gender, phone)
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success", "Patient Registered Successfully!")
            reg_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    Button(reg_window, text="Register", bg="green", fg="white", command=save_patient).pack(pady=15)


# --- Doctor Registration ---
def open_doctor_registration():
    doc_window = Toplevel(root)
    doc_window.title("Doctor Registration")
    doc_window.geometry("400x450")
    doc_window.configure(bg="lightgreen")

    Label(doc_window, text="Doctor Registration", font=("Arial", 16, "bold"), bg="lightgreen").pack(pady=10)

    Label(doc_window, text="Name:", bg="lightgreen").pack()
    name_entry = Entry(doc_window, width=30)
    name_entry.pack(pady=5)

    Label(doc_window, text="Specialization:", bg="lightgreen").pack()
    specialization_entry = Entry(doc_window, width=30)
    specialization_entry.pack(pady=5)

    Label(doc_window, text="Phone:", bg="lightgreen").pack()
    phone_entry = Entry(doc_window, width=30)
    phone_entry.pack(pady=5)

    Label(doc_window, text="Experience (in years):", bg="lightgreen").pack()
    experience_entry = Entry(doc_window, width=30)
    experience_entry.pack(pady=5)

    def save_doctor():
        name = name_entry.get()
        spec = specialization_entry.get()
        phone = phone_entry.get()
        exp = experience_entry.get()
        if name and spec and phone and exp:
            query = "INSERT INTO doctors (name, specialization, phone, experience) VALUES (%s, %s, %s, %s)"
            values = (name, spec, phone, exp)
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success", "Doctor Registered Successfully!")
            doc_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    Button(doc_window, text="Register", bg="green", fg="white", command=save_doctor).pack(pady=15)


# --- Appointment Booking ---
def open_appointment_details():
    app_window = Toplevel(root)
    app_window.title("Appointment Details")
    app_window.geometry("400x500")
    app_window.configure(bg="lightyellow")

    Label(app_window, text="Book Appointment", font=("Arial", 16, "bold"), bg="lightyellow").pack(pady=10)

    Label(app_window, text="Patient Name:", bg="lightyellow").pack()
    patient_entry = Entry(app_window, width=30)
    patient_entry.pack(pady=5)

    Label(app_window, text="Doctor Name:", bg="lightyellow").pack()
    doctor_entry = Entry(app_window, width=30)
    doctor_entry.pack(pady=5)

    Label(app_window, text="Date (DD/MM/YYYY):", bg="lightyellow").pack()
    date_entry = Entry(app_window, width=30)
    date_entry.pack(pady=5)

    Label(app_window, text="Time (HH:MM):", bg="lightyellow").pack()
    time_entry = Entry(app_window, width=30)
    time_entry.pack(pady=5)

    def save_appointment():
        patient = patient_entry.get()
        doctor = doctor_entry.get()
        date = date_entry.get()
        time = time_entry.get()
        if patient and doctor and date and time:
            query = "INSERT INTO appointments (patient_name, doctor_name, app_date, app_time) VALUES (%s, %s, %s, %s)"
            values = (patient, doctor, date, time)
            cursor.execute(query, values)
            conn.commit()
            messagebox.showinfo("Success", f"Appointment booked for {patient} with Dr. {doctor}")
            app_window.destroy()
        else:
            messagebox.showerror("Error", "All fields are required!")

    Button(app_window, text="Book Appointment", bg="blue", fg="white", command=save_appointment).pack(pady=20)


# --- View Records ---
def view_records():
    view_window = Toplevel(root)
    view_window.title("View Records")
    view_window.geometry("800x600")
    view_window.configure(bg="lightgrey")

    Label(view_window, text="View Records", font=("Arial", 16, "bold"), bg="lightgrey").pack(pady=10)

    # Tabs for patients, doctors, and appointments
    tab_frame = Frame(view_window)
    tab_frame.pack(pady=10)

    def show_patients():
        for widget in view_frame.winfo_children():
            widget.destroy()
        query = "SELECT * FROM patients"
        cursor.execute(query)
        records = cursor.fetchall()
        columns = ("ID", "Name", "Age", "Gender", "Phone")
        create_table(records, columns)

    def show_doctors():
        for widget in view_frame.winfo_children():
            widget.destroy()
        query = "SELECT * FROM doctors"
        cursor.execute(query)
        records = cursor.fetchall()
        columns = ("ID", "Name", "Specialization", "Phone", "Experience")
        create_table(records, columns)

    def show_appointments():
        for widget in view_frame.winfo_children():
            widget.destroy()
        query = "SELECT * FROM appointments"
        cursor.execute(query)
        records = cursor.fetchall()
        columns = ("ID", "Patient Name", "Doctor Name", "Date", "Time")
        create_table(records, columns)

    def create_table(records, columns):
        tree = ttk.Treeview(view_frame, columns=columns, show="headings")
        tree.pack(fill=BOTH, expand=True)

        for col in columns:
            tree.heading(col, text=col)

        for record in records:
            tree.insert("", "end", values=record)

    # Buttons to switch between tabs
    view_frame = Frame(view_window)
    view_frame.pack(pady=10)

    Button(tab_frame, text="Patients", command=show_patients).pack(side=LEFT, padx=10)
    Button(tab_frame, text="Doctors", command=show_doctors).pack(side=LEFT, padx=10)
    Button(tab_frame, text="Appointments", command=show_appointments).pack(side=LEFT, padx=10)

    show_patients()  # default to show patients


# --- Main Window UI ---
Label(root, text="HOSPITAL MANAGEMENT SYSTEM", font=('Arial', 35), bg='skyblue').pack(pady=30)

btn_style = {'height': 3, 'width': 20, 'font': ('Arial', 20), 'relief': 'solid'}

Button(root, text="Patient Registration", command=open_patient_registration, **btn_style).pack(pady=10)
Button(root, text="Doctor Registration", command=open_doctor_registration, **btn_style).pack(pady=10)
Button(root, text="Appointment Details", command=open_appointment_details, **btn_style).pack(pady=10)
Button(root, text="View Records", command=view_records, **btn_style).pack(pady=10)

root.mainloop()

# Close MySQL connection when the app is closed
conn.close()
