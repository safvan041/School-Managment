from tkinter import *
from tkinter import ttk, messagebox
from database import attendance

class AttendancePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.configure(bg='lightblue') 

        Label(self, text="Add Attendance",bg='lightblue').grid(row=0, column=0, padx=10, pady=10)
        Label(self, text="Student ID:",bg='lightblue').grid(row=1, column=0, padx=10, pady=5)
        self.attendance_id = Entry(self)
        self.attendance_id.grid(row=1, column=1, padx=10, pady=5)
        Label(self, text="Date:",bg='lightblue').grid(row=2, column=0, padx=10, pady=5)
        self.date = Entry(self)
        self.date.grid(row=2, column=1, padx=10, pady=5)
        Label(self, text="Status:",bg='lightblue').grid(row=3, column=0, padx=10, pady=5)
        self.status = Entry(self)
        self.status.grid(row=3, column=1, padx=10, pady=5)
        Button(self, text="Add Attendance", command=self.add_attendance).grid(row=4, column=0, columnspan=2, pady=10)
        Button(self, text="View Attendance", command=self.view_attendance_window).grid(row=5, column=0, columnspan=2, pady=10)

    def add_attendance(self):
        try:
            attendance_data = {
                "student_id": int(self.attendance_id.get()),
                "date": self.date.get(),
                "status": self.status.get()
            }
            attendance.insert_one(attendance_data)
            messagebox.showinfo("Success", "Attendance added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while adding attendance: {e}")

    def view_attendance_window(self):
        
        view_win = Toplevel(self)
        view_win.title("View Attendance")
        view_win.geometry('600x400')
        tree = ttk.Treeview(view_win, columns=("Student ID", "Date", "Status"), show='headings')
        tree.heading("Student ID", text="Student ID")
        tree.heading("Date", text="Date")
        tree.heading("Status", text="Status")
        tree.pack(fill=BOTH, expand=True, padx=10, pady=10)
        tree.delete(*tree.get_children())
        try:
            attendance_data = attendance.find()
            for record in attendance_data:
                tree.insert("", "end", values=(record.get("student_id", "N/A"), record.get("date", "N/A"),
                                                record.get("status", "N/A")))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching attendance data: {e}")
