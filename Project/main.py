import tkinter as tk
from tkinter import messagebox
import random
import sqlite3

# Function to fetch 5 random questions from the database
def fetch_questions_from_db():
    conn = sqlite3.connect("questions.db")
    cursor = conn.cursor()

    # Fetch 5 random questions from the database
    cursor.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 5")
    rows = cursor.fetchall()

    # Prepare questions
    questions = []
    for q in rows:
        question = {
            "question": q[1],
            "options": [q[2], q[3], q[4], q[5]],
            "answer": q[6],
            "explanation": q[7]
        }
        questions.append(question)

    conn.close()
    return questions

class QuizApp:
    def __init__(self, root, questions):
        self.root = root
        self.root.title("MCQ Quiz Game")

        self.score = 0
        self.question_index = 0
        self.questions = questions

        # Question Label
        self.question_label = tk.Label(root, text="", font=("Arial", 18), wraplength=500, justify="center")
        self.question_label.pack(pady=20)

        # Options Frame
        self.options_frame = tk.Frame(root)
        self.options_frame.pack(pady=20)

        # Radio Buttons for Options
        self.selected_option = tk.StringVar(value="")  # To store user's choice
        self.option_buttons = []
        for i in range(4):  # Four options
            button = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected_option,
                value=f"Option{i}",  # Unique value for each option
                font=("Arial", 14),
                anchor="w",
                justify="left",
                padx=10,  # Add padding to make it look bigger
            )
            button.pack(fill="x", padx=10, pady=8)
            self.option_buttons.append(button)

        # Next Button
        self.next_button = tk.Button(
            root,
            text="Next",
            command=self.check_answer,
            font=("Arial", 16, "bold"),
            bg="green",
            fg="white",
            height=2,
            width=10
        )
        self.next_button.pack(pady=20)

        # Start with the first question
        self.load_question()

    def load_question(self):
        """Loads the current question and options."""
        if self.question_index < len(self.questions):
            current_question = self.questions[self.question_index]
            self.question_label.config(text=f"Q{self.question_index + 1}: {current_question['question']}")

            # Set options
            self.selected_option.set("")  # Reset selection
            for i, option in enumerate(current_question["options"]):
                self.option_buttons[i].config(text=option, value=option)
        else:
            self.show_result()

    def check_answer(self):
        """Checks the user's answer and provides feedback with an explanation."""
        current_question = self.questions[self.question_index]
        selected = self.selected_option.get()

        if selected == current_question["answer"]:
            self.score += 1
            self.show_feedback("You're correct!", "green")  # Show 'You're correct!' message
        else:
            # Show the incorrect answer in a popup
            messagebox.showinfo(
                "Incorrect Answer",
                f"Wrong! The correct answer is: {current_question['answer']}\n\nExplanation: {current_question['explanation']}",
            )

        self.question_index += 1
        self.load_question()

    def show_feedback(self, message, color):
        """Shows feedback on the screen."""
        feedback_label = tk.Label(self.root, text=message, font=("Arial", 14), fg=color)
        feedback_label.pack(pady=10)

        # Hide feedback after 1 second
        self.root.after(1000, feedback_label.destroy)

    def show_result(self):
        """Displays the final score."""
        messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}/{len(self.questions)}")
        self.root.quit()  # Exit the application


class Homepage:
    def __init__(self, root):
        self.root = root
        self.root.title("Homepage - Heritage Quiz Game")

        # Background Image (Use the correct path)
        self.bg_image = tk.PhotoImage(file=r"C:\Users\dsouz\OneDrive\Desktop\python\ccp\IMAGES\HOME_PAGE.png")  # Updated path
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)  # Place the image as background
        self.bg_label.lower()  # Send the image to the background

        # Title Label
        self.title_label = tk.Label(
            root,
            text="Welcome to the Heritage Quiz Game!",
            font=("Arial", 24),
            justify="center",
            bg="#ffffff",
            fg="#000000"
        )
        self.title_label.pack(pady=40)

        # Start Button
        self.start_button = tk.Button(
            root,
            text="Start Quiz",
            command=self.start_quiz,
            font=("Arial", 16, "bold"),
            bg="green",
            fg="white",
            height=2,
            width=12
        )
        self.start_button.pack(pady=200)

        # Keep reference to the image to prevent garbage collection
        self.bg_label.image = self.bg_image  # Prevent image from being garbage collected

    def start_quiz(self):
        """Switches to the quiz app."""
        self.root.destroy()  # Close homepage window
        quiz_window = tk.Tk()

        # Fetch 5 random questions from the database
        questions = fetch_questions_from_db()

        # Start the quiz application
        app = QuizApp(quiz_window, questions)
        quiz_window.mainloop()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    homepage = Homepage(root)
    root.mainloop()
