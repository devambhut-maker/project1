import tkinter as tk
from tkinter import ttk


SUBJECTS = ("Maths", "Hindi", "Gujarati", "English", "Science", "Accountancy")


def calculate_marksheet():
	name = name_entry.get().strip()
	if not name:
		show_error("Please enter the student's name.")
		return

	marks = []
	for subject, entry in zip(SUBJECTS, mark_entries):
		try:
			mark = float(entry.get())
		except ValueError:
			show_error(f"Enter a valid mark for {subject}.")
			return
		if not 0 <= mark <= 100:
			show_error(f"{subject} must be between 0 and 100.")
			return
		marks.append(mark)

	total = sum(marks)
	average = total / len(marks)
	percentage = total / 600 * 100
	grade = get_grade(percentage)

	result_label.config(
		text=(
			f"Student: {name}\n"
			f"Total: {total:g} / 600\n"
			f"Average: {average:.2f}\n"
			f"Percentage: {percentage:.2f}%\n"
			f"Grade: {grade}"
		),
		foreground="#166534",
	)


def get_grade(percentage):
	if percentage >= 90:
		return "A+"
	if percentage >= 80:
		return "A"
	if percentage >= 70:
		return "B"
	if percentage >= 60:
		return "C"
	if percentage >= 50:
		return "D"
	return "Needs improvement"


def show_error(message):
	result_label.config(text=message, foreground="#b42318")


def clear_form():
	name_entry.delete(0, tk.END)
	for entry in mark_entries:
		entry.delete(0, tk.END)
	result_label.config(text="Enter marks to generate the result.", foreground="#64748b")
	name_entry.focus_set()


root = tk.Tk()
root.title("Student Marksheet")
root.geometry("520x650")
root.minsize(420, 560)
root.configure(bg="#f1f5f9")

style = ttk.Style()
style.theme_use("clam")
style.configure("Card.TFrame", background="#ffffff")
style.configure("Title.TLabel", background="#ffffff", foreground="#0f172a", font=("Segoe UI", 24, "bold"))
style.configure("Subtitle.TLabel", background="#ffffff", foreground="#64748b", font=("Segoe UI", 10))
style.configure("Field.TLabel", background="#ffffff", foreground="#334155", font=("Segoe UI", 10, "bold"))
style.configure("TEntry", padding=9, font=("Segoe UI", 11))
style.configure("Accent.TButton", background="#0f766e", foreground="#ffffff", padding=10, font=("Segoe UI", 10, "bold"))
style.map("Accent.TButton", background=[("active", "#115e59")])
style.configure("Quiet.TButton", background="#e2e8f0", foreground="#334155", padding=10, font=("Segoe UI", 10, "bold"))

card = ttk.Frame(root, style="Card.TFrame", padding=30)
card.pack(fill="both", expand=True, padx=24, pady=24)

ttk.Label(card, text="Student Marksheet", style="Title.TLabel").pack(anchor="w")
ttk.Label(card, text="Enter the student's details and subject marks.", style="Subtitle.TLabel").pack(anchor="w", pady=(4, 22))

ttk.Label(card, text="Student name", style="Field.TLabel").pack(anchor="w")
name_entry = ttk.Entry(card)
name_entry.pack(fill="x", pady=(6, 18))

marks_frame = ttk.Frame(card, style="Card.TFrame")
marks_frame.pack(fill="x")
mark_entries = []
for subject in SUBJECTS:
	ttk.Label(marks_frame, text=subject, style="Field.TLabel").pack(side="left", padx=(0, 8), pady=5)
	entry = ttk.Entry(marks_frame, width=8)
	entry.pack(side="right", pady=5)
	mark_entries.append(entry)

button_row = ttk.Frame(card, style="Card.TFrame")
button_row.pack(fill="x", pady=(22, 0))
ttk.Button(button_row, text="Generate Marksheet", command=calculate_marksheet, style="Accent.TButton").pack(side="left", expand=True, fill="x", padx=(0, 6))
ttk.Button(button_row, text="Clear", command=clear_form, style="Quiet.TButton").pack(side="left", expand=True, fill="x", padx=(6, 0))

result_label = tk.Label(card, text="Enter marks to generate the result.", bg="#ffffff", fg="#64748b", font=("Segoe UI", 12, "bold"), justify="left", anchor="w", pady=24)
result_label.pack(fill="x")

root.bind("<Return>", lambda event: calculate_marksheet())
name_entry.focus_set()
root.mainloop()