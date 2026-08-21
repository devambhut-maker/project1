import tkinter as tk
from tkinter import ttk


def calculate_age():
	name = name_entry.get().strip()

	if not name:
		show_result("Please enter your name.", "#b42318")
		return

	try:
		birth_year = int(birth_year_entry.get())
		current_year = int(current_year_entry.get())
	except ValueError:
		show_result("Please enter valid years.", "#b42318")
		return

	if birth_year > current_year:
		show_result("Birth year cannot be after the current year.", "#b42318")
		return

	age = current_year - birth_year
	show_result(f"{name}, your age is {age}.", "#166534")


def show_result(message, color):
	result_label.config(text=message, foreground=color)


def clear_form():
	name_entry.delete(0, tk.END)
	birth_year_entry.delete(0, tk.END)
	current_year_entry.delete(0, tk.END)
	show_result("Your result will appear here.", "#64748b")
	name_entry.focus_set()


root = tk.Tk()
root.title("Age Calculator")
root.geometry("440x430")
root.minsize(360, 360)
root.configure(bg="#e0f2fe")

style = ttk.Style()
style.theme_use("clam")
style.configure("Card.TFrame", background="#ffffff")
style.configure("Title.TLabel", background="#ffffff", foreground="#0c4a6e", font=("Segoe UI", 24, "bold"))
style.configure("Subtitle.TLabel", background="#ffffff", foreground="#64748b", font=("Segoe UI", 10))
style.configure("Field.TLabel", background="#ffffff", foreground="#334155", font=("Segoe UI", 10, "bold"))
style.configure("TEntry", padding=9, font=("Segoe UI", 12))
style.configure("Accent.TButton", background="#0284c7", foreground="#ffffff", padding=10, font=("Segoe UI", 10, "bold"))
style.map("Accent.TButton", background=[("active", "#0369a1")])
style.configure("Quiet.TButton", background="#e2e8f0", foreground="#334155", padding=10, font=("Segoe UI", 10, "bold"))

card = ttk.Frame(root, style="Card.TFrame", padding=30)
card.pack(fill="both", expand=True, padx=24, pady=24)

ttk.Label(card, text="Age Calculator", style="Title.TLabel").pack(anchor="w")
ttk.Label(card, text="Find an age from two years.", style="Subtitle.TLabel").pack(anchor="w", pady=(4, 24))

ttk.Label(card, text="Name", style="Field.TLabel").pack(anchor="w")
name_entry = ttk.Entry(card)
name_entry.pack(fill="x", pady=(6, 16))

ttk.Label(card, text="Birth year", style="Field.TLabel").pack(anchor="w")
birth_year_entry = ttk.Entry(card)
birth_year_entry.pack(fill="x", pady=(6, 16))

ttk.Label(card, text="Current year", style="Field.TLabel").pack(anchor="w")
current_year_entry = ttk.Entry(card)
current_year_entry.pack(fill="x", pady=(6, 22))

button_row = ttk.Frame(card, style="Card.TFrame")
button_row.pack(fill="x")
ttk.Button(button_row, text="Calculate", command=calculate_age, style="Accent.TButton").pack(side="left", expand=True, fill="x", padx=(0, 6))
ttk.Button(button_row, text="Clear", command=clear_form, style="Quiet.TButton").pack(side="left", expand=True, fill="x", padx=(6, 0))

result_label = tk.Label(card, text="Your result will appear here.", background="#ffffff", foreground="#64748b", font=("Segoe UI", 12, "bold"), pady=24)
result_label.pack(fill="x")

root.bind("<Return>", lambda event: calculate_age())
name_entry.focus_set()
root.mainloop()