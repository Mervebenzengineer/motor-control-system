#MOTOR CONTROL LOGIN SYSTEM

import tkinter as tk
from tkinter import messagebox
import sqlite3

TrueAdmin = "Mercedes"
TruePassword = "242503024"

def control_motor():
    Engine_Name = TrueAdmin_Entry.get()
    Password = TruePassword_Entry.get()

    if Engine_Name == TrueAdmin and Password == TruePassword:
        messagebox.showinfo("True", "LOGGED IN")
        open_engine_control_windows()
    else:
        messagebox.showerror("False", "Password or Name False")

    TrueAdmin_Entry.delete(0, tk.END)
    TruePassword_Entry.delete(0, tk.END)

def open_engine_control_windows():
    global EngineName_entry, Temperature_entry, FuelLevel_entry, RPM_entry

    engine_windows = tk.Toplevel()
    engine_windows.title("Engine Control System")
    engine_windows.geometry("500x400")
    
    tk.Label(engine_windows, text="Engine Name:").pack()
    EngineName_entry = tk.Entry(engine_windows)
    EngineName_entry.pack()

    tk.Label(engine_windows, text="Temperature (°C):").pack()
    Temperature_entry = tk.Entry(engine_windows)
    Temperature_entry.pack()

    tk.Label(engine_windows, text="Fuel Level (%):").pack()
    FuelLevel_entry = tk.Entry(engine_windows)
    FuelLevel_entry.pack()

    tk.Label(engine_windows, text="RPM:").pack()
    RPM_entry = tk.Entry(engine_windows)
    RPM_entry.pack()

    save_button = tk.Button(engine_windows, text="Save", command=save_data)
    save_button.pack(pady=10)

    search_button=tk.Button(engine_windows,text="Search",command=search_data)
    search_button.pack()

def save_data():
    EngineName = EngineName_entry.get()
    try:
        Temperature = int(Temperature_entry.get())
        FuelLevel = int(FuelLevel_entry.get())
        RPM = int(RPM_entry.get())
    except ValueError:
        messagebox.showwarning("Warning", "All values must be numbers!")
        return

    conn = sqlite3.connect("engine.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO engine_data VALUES (?, ?, ?, ?)",
                   (EngineName, Temperature, FuelLevel, RPM))
    conn.commit()
    conn.close()

    messagebox.showinfo("Saved", "Engine data has been saved.")

    EngineName_entry.delete(0, tk.END)
    Temperature_entry.delete(0, tk.END)
    FuelLevel_entry.delete(0, tk.END)
    RPM_entry.delete(0, tk.END)

def search_data():
    EngineName = EngineName_entry.get()
    conn=sqlite3.connect("engine.db")
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM engine_data WHERE EngineName=?",(EngineName,))

    data=cursor.fetchall()
    if data:
        messagebox.showinfo("True","Data found")
    else:
        messagebox.showerror("False","Data not found")
    conn.close()

def create_table():
    conn=sqlite3.connect("engine.db")
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS engine_data(
        EngineName TEXT,
        Temperature INTEGER,
        FuelLevel INTEGER,
        RPM INTEGER
    )
    """)
    conn.commit()
    conn.close()

create_table()

windows = tk.Tk()
windows.title("Engine Control Input System")
windows.geometry("500x300")

tk.Label(windows, text="Engine Name:").pack()
TrueAdmin_Entry = tk.Entry(windows)
TrueAdmin_Entry.pack()

tk.Label(windows, text="Password:").pack()
TruePassword_Entry = tk.Entry(windows, show="*")
TruePassword_Entry.pack()

control_button = tk.Button(windows, text="Control", command=control_motor)
control_button.pack(pady=20)

windows.mainloop()
