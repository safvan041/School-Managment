from tkinter import *
from tkinter import ttk, messagebox
from pymongo import MongoClient

# Setup MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client.school
grades = db['grades']

class GradesPage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.configure(bg='lightblue') 

        Label(self, text="Add Grades", bg='lightblue').grid(row=0, column=0, padx=10, pady=10)
        Label(self, text="Student ID:", bg='lightblue').grid(row=1, column=0, padx=10, pady=5)
        self.grade_id = Entry(self)
        self.grade_id.grid(row=1, column=1, padx=10, pady=5)
        Label(self, text="Subject:", bg='lightblue').grid(row=2, column=0, padx=10, pady=5)
        self.subject = Entry(self)
        self.subject.grid(row=2, column=1, padx=10, pady=5)
        Label(self, text="Grade:", bg='lightblue').grid(row=3, column=0, padx=10, pady=5)
        self.grade = Entry(self)
        self.grade.grid(row=3, column=1, padx=10, pady=5)

        Button(self, text="Add Grade", command=self.add_grade).grid(row=4, column=0, columnspan=2, pady=10)
        Button(self, text="View Grades", command=self.view_grades_window).grid(row=5, column=0, columnspan=2, pady=10)
        Button(self, text="Update Grade", command=self.update_grades_window).grid(row=6, column=0, columnspan=2, pady=10)
        Button(self, text="Delete Grade", command=self.delete_grades_window).grid(row=7, column=0, columnspan=2, pady=10)
        Button(self, text="Back", command=self.go_back).grid(row=8, column=0, columnspan=2, pady=10)

    def add_grade(self):
        try:
            grade_data = {
                "student_id": int(self.grade_id.get()),
                "subject": self.subject.get(),
                "grade": self.grade.get()
            }
            grades.insert_one(grade_data)
            messagebox.showinfo("Success", "Grade added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while adding grade: {e}")

    def view_grades_window(self):
        view_win = Toplevel(self)
        view_win.title("View Grades")
        view_win.geometry('600x400')
        tree = ttk.Treeview(view_win, columns=("Student ID", "Subject", "Grade"), show='headings')
        tree.heading("Student ID", text="Student ID")
        tree.heading("Subject", text="Subject")
        tree.heading("Grade", text="Grade")
        tree.pack(fill=BOTH, expand=True, padx=10, pady=10)
        tree.delete(*tree.get_children())
        try:
            grades_data = grades.find()
            for record in grades_data:
                tree.insert("", "end", values=(record.get("student_id", "N/A"), record.get("subject", "N/A"),
                                                record.get("grade", "N/A")))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while fetching grades data: {e}")

    def update_grades_window(self):
        update_win = Toplevel(self)
        update_win.title("Update Grades")
        update_win.geometry('300x300')

        Label(update_win, text="Student ID:").grid(row=0, column=0, padx=10, pady=10)
        student_id = Entry(update_win)
        student_id.grid(row=0, column=1)

        Label(update_win, text="Subject:").grid(row=1, column=0, padx=10, pady=10)
        subject = Entry(update_win)
        subject.grid(row=1, column=1)

        Label(update_win, text="New Grade:").grid(row=2, column=0, padx=10, pady=10)
        new_grade = Entry(update_win)
        new_grade.grid(row=2, column=1)

        def update_grade():
            try:
                result = grades.update_one(
                    {"student_id": int(student_id.get()), "subject": subject.get()},
                    {"$set": {"grade": new_grade.get()}}
                )
                if result.matched_count > 0:
                    messagebox.showinfo("Success", "Grade updated successfully!")
                else:
                    messagebox.showerror("Error", "Grade not found!")
                update_win.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while updating grade: {e}")

        Button(update_win, text="Update Grade", command=update_grade).grid(row=3, column=1, pady=10)

    def delete_grades_window(self):
        delete_win = Toplevel(self)
        delete_win.title("Delete Grades")
        delete_win.geometry('300x200')

        Label(delete_win, text="Student ID:").grid(row=0, column=0, padx=10, pady=10)
        student_id = Entry(delete_win)
        student_id.grid(row=0, column=1)

        Label(delete_win, text="Subject:").grid(row=1, column=0, padx=10, pady=10)
        subject = Entry(delete_win)
        subject.grid(row=1, column=1)

        def delete_grade():
            try:
                result = grades.delete_one(
                    {"student_id": int(student_id.get()), "subject": subject.get()}
                )
                if result.deleted_count > 0:
                    messagebox.showinfo("Success", "Grade deleted successfully!")
                else:
                    messagebox.showerror("Error", "Grade not found!")
                delete_win.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while deleting grade: {e}")

        Button(delete_win, text="Delete Grade", command=delete_grade).grid(row=2, column=1, pady=10)

    def go_back(self):
        self.destroy()  # Close this page and return to the parent window

# Usage Example:
# root = Tk()
# app = GradesPage(root)
# app.pack(fill=BOTH, expand=True)
# root.mainloop()
