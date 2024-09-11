from tkinter import *
from tkinter import ttk, messagebox
from pymongo import MongoClient

# Setup MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['school_management']
students = db['students']

class StudentPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.configure(bg='lightblue')
        # Add Student
        Label(self, text="Add Student", bg='lightblue').grid(row=0, column=0, padx=10, pady=10)
        Label(self, text="Student ID:", bg='lightblue').grid(row=1, column=0, padx=10, pady=5)
        self.student_id = Entry(self)
        self.student_id.grid(row=1, column=1, padx=10, pady=5)
        Label(self, text="Name:", bg='lightblue').grid(row=2, column=0, padx=10, pady=5)
        self.name = Entry(self)
        self.name.grid(row=2, column=1, padx=10, pady=5)
        Label(self, text="Age:", bg='lightblue').grid(row=3, column=0, padx=10, pady=5)
        self.age = Entry(self)
        self.age.grid(row=3, column=1, padx=10, pady=5)
        Label(self, text="Class:", bg='lightblue').grid(row=4, column=0, padx=10, pady=5)
        self.student_class = Entry(self)
        self.student_class.grid(row=4, column=1, padx=10, pady=5)
        Label(self, text="Parent Name:", bg='lightblue').grid(row=5, column=0, padx=10, pady=5)
        self.parent_name = Entry(self)
        self.parent_name.grid(row=5, column=1, padx=10, pady=5)
        Label(self, text="Phone:", bg='lightblue').grid(row=6, column=0, padx=10, pady=5)
        self.phone = Entry(self)
        self.phone.grid(row=6, column=1, padx=10, pady=5)

        Button(self, text="Add Student", command=self.add_student).grid(row=7, column=0, columnspan=2, pady=10)
        Button(self, text="View Students", command=self.view_students_window).grid(row=8, column=0, columnspan=2, pady=10)
        Button(self, text="Back", command=self.go_back).grid(row=9, column=0, columnspan=2, pady=10)

    def add_student(self):
        try:
            student_data = {
                "student_id": int(self.student_id.get()),
                "name": self.name.get(),
                "age": int(self.age.get()),
                "class": self.student_class.get(),
                "parent_name": self.parent_name.get(),
                "phone": self.phone.get()
            }
            students.insert_one(student_data)
            messagebox.showinfo("Success", "Student added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while adding student: {e}")

    def view_students_window(self):
        view_win = Toplevel(self)
        view_win.title("View Students")
        view_win.geometry('600x400')
        tree = ttk.Treeview(view_win, columns=("ID", "Name", "Age", "Class", "Parent Name", "Phone"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("Age", text="Age")
        tree.heading("Class", text="Class")
        tree.heading("Parent Name", text="Parent Name")
        tree.heading("Phone", text="Phone")
        tree.pack(fill=BOTH, expand=True, padx=10, pady=10)
        tree.delete(*tree.get_children())
        try:
            students_data = students.find()
            for record in students_data:
                tree.insert("", "end", values=(record.get("student_id", "N/A"), record.get("name", "N/A"),
                                                record.get("age", "N/A"), record.get("class", "N/A"),
                                                record.get("parent_name", "N/A"), record.get("phone", "N/A")))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching students data: {e}")

    def go_back(self):
        self.destroy()  # Close this page and return to the parent window

# Usage Example:
# root = Tk()
# app = StudentPage(root)
# app.pack(fill=BOTH, expand=True)
# root.mainloop()
