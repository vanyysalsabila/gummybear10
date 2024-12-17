import tkinter as tk
from tkinter import messagebox
import random

print("Welcome to my computer quiz!")

class QuizApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Aplikasi Kuis Sederhana TUBES")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.users = {}  # {username: {password: str, mode: 'teacher' or 'student'}}
        self.questions = []  # List of questions
        self.current_user = None
        self.current_question = None
        self.score = 0
        self.attempts = 0

        self.login_screen()

    def login_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Quiz Pak Tirta", font=("Times New Roman", 18)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.input_username = tk.Entry(self.root)
        self.input_username.pack()

        tk.Label(self.root, text="Password").pack()
        self.input_password = tk.Entry(self.root, show="0")
        self.input_password.pack()

        tk.Button(self.root, text="Sign In", command=self.sign_in).pack(pady=5)
        tk.Button(self.root, text="Sign Up", command=self.sign_up_screen).pack()

    def sign_up_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Sign Up", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.new_username_entry = tk.Entry(self.root)
        self.new_username_entry.pack()

        tk.Label(self.root, text="Password").pack()
        self.new_input_password = tk.Entry(self.root, show="*")
        self.new_input_password.pack()

        tk.Label(self.root, text="Select Mode").pack(pady=10)

        # Tombol untuk memilih mode Teacher
        self.selected_mode = tk.StringVar(value="")  # Variabel untuk menyimpan mode
        teacher_button = tk.Button(self.root, text="Teacher", bg="blue", fg="white",
                                    command=lambda: self.set_mode("teacher"))
        teacher_button.pack(pady=5)

        # Tombol untuk memilih mode Student
        student_button = tk.Button(self.root, text="Student", bg="green", fg="white",
                                    command=lambda: self.set_mode("student"))
        student_button.pack(pady=5)

        # Tombol daftar dan kembali
        tk.Button(self.root, text="Register", command=self.sign_up).pack(pady=10)
        tk.Button(self.root, text="Back to Login", command=self.login_screen).pack()

    def set_mode(self, mode):
        """Mengatur mode yang dipilih pada tombol Sign-Up"""
        self.selected_mode.set(mode)
        messagebox.showinfo("Mode Selected", f"You selected: {mode.capitalize()}")

    def sign_in(self):
        username = self.input_username.get()
        password = self.input_password.get()
        if username in self.users and self.users[username]["password"] == password:
            self.current_user = username
            if self.users[username]["mode"] == "teacher":
                self.teacher_dashboard()
            else:
                self.student_dashboard()
        else:
            messagebox.showerror("Error", "Invalid username or password")


    def sign_up(self):
        username = self.new_username_entry.get()
        password = self.new_input_password.get()
        mode = self.selected_mode.get()

        if username in self.users:
            messagebox.showerror("Error", "Username sudah terdaftar!")
        else:
            self.users[username] = {"password": password, "mode": mode}
            messagebox.showinfo("Success", "Selamat anda sudah terdaftar!")
            self.login_screen()


    def teacher_dashboard(self):
        self.clear_screen()

        tk.Label(self.root, text="Teacher Dashboard", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="Add Question", command=self.add_question_screen).pack(pady=5)
        tk.Button(self.root, text="Edit/Delete Questions", command=self.edit_questions_screen).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=5)

    def add_question_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Add Question", font=("Arial", 18)).pack(pady=10)

        tk.Label(self.root, text="Question").pack()
        self.question_entry = tk.Entry(self.root, width=50)
        self.question_entry.pack()

        tk.Label(self.root, text="Answer").pack()
        self.answer_entry = tk.Entry(self.root, width=50)
        self.answer_entry.pack()

        tk.Button(self.root, text="Add", command=self.add_question).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.teacher_dashboard).pack()

    def add_question(self):
        question = self.question_entry.get()
        answer = self.answer_entry.get()

        if question and answer:
            self.questions.append({"question": question, "answer": answer})
            messagebox.showinfo("Success", "Question added")
            self.add_question_screen()
        else:
            messagebox.showerror("Error", "Tidak boleh ada yang kosong!")

    def edit_questions_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Edit/Delete Questions", font=("Arial", 18)).pack(pady=10)

        for i, q in enumerate(self.questions):
            tk.Label(self.root, text=f"{i + 1}. {q['question']} (Answer: {q['answer']})").pack()

        tk.Label(self.root, text="Select Question Number to Edit/Delete").pack()
        self.question_number_entry = tk.Entry(self.root)
        self.question_number_entry.pack()

        tk.Button(self.root, text="Edit", command=self.edit_question).pack(pady=5)
        tk.Button(self.root, text="Delete", command=self.delete_question).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.teacher_dashboard).pack()

    def edit_question(self):
        try:
            index = int(self.question_number_entry.get()) - 1
            if 0 <= index < len(self.questions):
                self.clear_screen()

                tk.Label(self.root, text="Edit Question", font=("Arial", 18)).pack(pady=10)

                tk.Label(self.root, text="Question").pack()
                self.edit_question_entry = tk.Entry(self.root, width=50)
                self.edit_question_entry.insert(0, self.questions[index]['question'])
                self.edit_question_entry.pack()

                tk.Label(self.root, text="Answer").pack()
                self.edit_answer_entry = tk.Entry(self.root, width=50)
                self.edit_answer_entry.insert(0, self.questions[index]['answer'])
                self.edit_answer_entry.pack()

                tk.Button(self.root, text="Save", command=lambda: self.save_question(index)).pack(pady=5)
                tk.Button(self.root, text="Back", command=self.edit_questions_screen).pack()
            else:
                messagebox.showerror("Error", "Invalid question number")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    def save_question(self, index):
        self.questions[index]["question"] = self.edit_question_entry.get()
        self.questions[index]["answer"] = self.edit_answer_entry.get()
        messagebox.showinfo("Success", "Question updated")
        self.edit_questions_screen()

    def delete_question(self):
        try:
            index = int(self.question_number_entry.get()) - 1
            if 0 <= index < len(self.questions):
                del self.questions[index]
                messagebox.showinfo("Success", "Question deleted")
                self.edit_questions_screen()
            else:
                messagebox.showerror("Error", "Invalid question number")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number")

    def student_dashboard(self):
        self.clear_screen()

        tk.Label(self.root, text="Student Dashboard", font=("Arial", 18)).pack(pady=10)

        tk.Button(self.root, text="Start Quiz", command=self.start_quiz).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.login_screen).pack(pady=5)

    def start_quiz(self):
        if not self.questions:
            messagebox.showerror("Error", "No questions available")
            return

        self.score = 0
        self.attempts = 0
        self.questions = random.sample(self.questions, len(self.questions))
        self.next_question()

    def next_question(self):
        if self.attempts < len(self.questions):
            self.current_question = self.questions[self.attempts]
            self.attempts += 1
            self.quiz_screen()
        else:
            messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(self.questions)}")
            self.student_dashboard()
            return  # Basis untuk menghentikan rekursi
        
        # Rekursif dipanggil di akhir untuk melanjutkan ke pertanyaan berikutnya
        def proceed_to_next_question():
            if self.answer_entry.get().lower() == self.current_question["answer"].lower():
                self.score += 1
            self.next_question()  # Rekursi di sini

        # Tombol Submit sekarang memanggil fungsi dalam fungsi untuk meneruskan rekursi
        self.clear_screen()
        tk.Label(self.root, text=f"Question {self.attempts}", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.root, text=self.current_question["question"], wraplength=400).pack(pady=10)
        self.answer_entry = tk.Entry(self.root, width=50)
        self.answer_entry.pack()
        tk.Button(self.root, text="Submit", command=proceed_to_next_question).pack(pady=5)


    def quiz_screen(self):
        self.clear_screen()

        tk.Label(self.root, text=f"Question {self.attempts}", font=("Arial", 18)).pack(pady=10)
        tk.Label(self.root, text=self.current_question["question"], wraplength=400).pack(pady=10)

        self.answer_entry = tk.Entry(self.root, width=50)
        self.answer_entry.pack()

        tk.Button(self.root, text="Submit", command=self.next_question).pack(pady=5)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()