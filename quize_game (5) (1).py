# Pro Python Quiz Game (Tkinter - Final UI Upgrade)

import tkinter as tk
from tkinter import messagebox
import random

quiz = [
    ("What is Python?", ["Programming Language","Snake","Game","None"], 0),
    ("HTML stands for?", ["Wrong","Hyper Text Markup Language","No","None"], 1),
    ("CSS used for?", ["Styling","Logic","DB","Server"], 0),
    ("JavaScript used for?", ["Styling","Logic","Structure","None"], 1),
    ("Which is database?", ["MySQL","HTML","CSS","JS"], 0),
    ("Python comment symbol?", ["#","//","/* */","--"], 0),
    ("Loop keyword?", ["for","loop","iterate","repeat"], 0),
    ("Print in Python?", ["print()","echo()","log()","show()"], 0),
    ("Backend language?", ["Python","HTML","CSS","None"], 0),
    ("CSS full form?", ["Cascading Style Sheets","Color Style","Creative Style","None"], 0)
]

random.shuffle(quiz)

root = tk.Tk()
root.title("Quiz Game 🎯")
root.geometry("750x700")
root.config(bg="#0a0f1f")

current = 0
score = 0
time_left = 30

# ===== HEADER (ALWAYS VISIBLE) =====
header = tk.Frame(root, bg="#111827")
header.pack(fill="x")

title = tk.Label(header, text="QUIZ GAME 🎯", font=("Segoe UI",24,"bold"), bg="#111827", fg="#38bdf8")
title.pack(pady=5)

team = tk.Label(header, text="Piyush Eghe | Nikhil Gaikwad | Prasad Dhore | Nishant Thakre",
                font=("Segoe UI",11), bg="#111827", fg="#cbd5f5")
team.pack(pady=3)

# ===== MAIN FRAME =====
main = tk.Frame(root, bg="#0a0f1f")
main.pack(expand=True, fill="both")

# ===== WELCOME SCREEN =====
welcome_frame = tk.Frame(main, bg="#0a0f1f")
welcome_frame.pack(expand=True)

welcome = tk.Label(welcome_frame,
                   text="WELCOME TO QUIZ GAME",
                   font=("Segoe UI",32,"bold"),
                   bg="#0a0f1f", fg="#22d3ee")
welcome.pack(pady=40)

sub = tk.Label(welcome_frame,
               text="Test Your Knowledge 🚀",
               font=("Segoe UI",16),
               bg="#0a0f1f", fg="#94a3b8")
sub.pack(pady=10)

start_btn = tk.Button(welcome_frame,
                      text="▶ START QUIZ",
                      font=("Segoe UI",18,"bold"),
                      bg="#22c55e", fg="white",
                      padx=30, pady=12,
                      relief="flat",
                      activebackground="#16a34a",
                      command=lambda: start_quiz())
start_btn.pack(pady=30)

# ===== QUIZ FRAME =====
quiz_frame = tk.Frame(main, bg="#1e293b")

question_label = tk.Label(quiz_frame, text="", font=("Segoe UI",18,"bold"),
                          bg="#1e293b", fg="white", wraplength=600)
question_label.pack(pady=25)

buttons = []
for i in range(4):
    btn = tk.Button(quiz_frame, text="", font=("Segoe UI",14), width=28, height=2,
                    bg="#3b82f6", fg="white", relief="flat",
                    activebackground="#2563eb")
    btn.pack(pady=8)
    buttons.append(btn)

# ===== TIMER =====
timer_label = tk.Label(root, text="", font=("Segoe UI",14,"bold"),
                       bg="#0a0f1f", fg="#facc15")

# ===== FUNCTIONS =====

def start_quiz():
    welcome_frame.pack_forget()
    quiz_frame.pack(expand=True)
    timer_label.pack(pady=5)
    load_question()


def load_question():
    global current, time_left
    if current < len(quiz):
        q, opts, ans = quiz[current]
        question_label.config(text=f"Q{current+1}: {q}")
        for i in range(4):
            buttons[i].config(text=opts[i], command=lambda i=i: check_answer(i))
        time_left = 30
        countdown()
    else:
        show_result()


def check_answer(i):
    global score, current
    _, _, ans = quiz[current]

    # Show feedback color
    if i == ans:
        buttons[i].config(bg="#22c55e")  # Green for correct
        score += 1
    else:
        buttons[i].config(bg="#ef4444")  # Red for wrong
        buttons[ans].config(bg="#22c55e")

    # Delay before next question
    root.after(800, next_after_feedback)


def next_after_feedback():
    global current
    current += 1

    # Reset button colors
    for btn in buttons:
        btn.config(bg="#3b82f6")

    load_question()


def countdown():
    global time_left
    timer_label.config(text=f"⏱ Time: {time_left}s")
    if time_left > 0:
        time_left -= 1
        root.after(1000, countdown)
    else:
        next_question()


def next_question():
    global current
    current += 1
    load_question()


def show_result():
    percent = (score/len(quiz))*100
    if percent >= 80:
        rank = "Pro 🏆"
    elif percent >= 50:
        rank = "Good 👍"
    else:
        rank = "Beginner"
    messagebox.showinfo("Result", f"Score: {score}/{len(quiz)}\nRank: {rank}")
    root.quit()

root.mainloop()
