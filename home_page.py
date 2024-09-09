from tkinter import Frame, Button, BOTH, LEFT, Y
from tkinter import ttk
from student_page import StudentPage
from attendance_page import AttendancePage
from grades_page import GradesPage

class HomePage(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        # Create a PanedWindow
        paned_window = ttk.PanedWindow(self, orient='horizontal')
        paned_window.pack(fill=BOTH, expand=True)

        # Left Sidebar
        sidebar = Frame(paned_window, width=150, bg='lightgray', padx=10, pady=10)
        sidebar.pack(fill=Y, side=LEFT, padx=5, pady=5)
        
        # Sidebar Buttons
        Button(sidebar, text="Student Management", command=self.open_student_management).pack(fill='x', pady=5)
        Button(sidebar, text="Attendance Management", command=self.open_attendance_management).pack(fill='x', pady=5)
        Button(sidebar, text="Grades Management", command=self.open_grades_management).pack(fill='x', pady=5)

        # Main Content Area
        self.content_frame = Frame(paned_window, bg='lightblue')
        self.content_frame.pack(fill=BOTH, expand=True)
        
        # Add frames to PanedWindow
        paned_window.add(sidebar, weight=1)
        paned_window.add(self.content_frame, weight=3)

    def open_student_management(self):
        self.show_frame(StudentPage)

    def open_attendance_management(self):
        self.show_frame(AttendancePage)

    def open_grades_management(self):
        self.show_frame(GradesPage)

    def show_frame(self, frame_class):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
        frame = frame_class(self.content_frame)
        frame.pack(fill=BOTH, expand=True)
