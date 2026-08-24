import tkinter as tk
from tkinter import ttk


def generate_data():
	name = name_entry.get().strip()
	if not name:
		show_error("Please enter a name.")
		return

	try:
		age = int(age_entry.get())
		height = float(height_entry.get())
		favourite_number = int(favourite_entry.get())
	except ValueError:
		show_error("Age and favourite number must be integers; height must be a number.")
		return

	if age < 0:
		show_error("Age cannot be negative.")
		return
	if height < 0:
		show_error("Height cannot be negative.")
		return

	birth_year = 2026 - age
	double = favourite_number * 2
	square = favourite_number ** 2
	height_int = int(height)

	result_label.config(
		text=(
			f"Name: {name}    | type: {type(name).__name__}\n"
			f"Age: {age}    | type: {type(age).__name__}\n"
			f"Height: {height:g} m    | type: {type(height).__name__}\n"
			f"Favourite Number: {favourite_number}    | type: {type(favourite_number).__name__}\n\n"
			f"Birth Year: {birth_year}    | type: {type(birth_year).__name__}\n"
			f"Double: {double}    | type: {type(double).__name__}\n"
			f"Square: {square}    | type: {type(square).__name__}\n"
			f"Height after int(): {height_int}    | type: {type(height_int).__name__}"
		),
		foreground="#166534",
	)


def show_error(message):
	result_label.config(text=message, foreground="#b42318")


def clear_form():
	for entry in (name_entry, age_entry, height_entry, favourite_entry):
		entry.delete(0, tk.END)
	result_label.config(text="Generated data will appear here.", foreground="#64748b")
	name_entry.focus_set()


root = tk.Tk()
root.title("Personal Data Collector")
root.geometry("680x650")
root.minsize(540, 560)
root.configure(bg="#f1f5f9")

style = ttk.Style()
style.theme_use("clam")
style.configure("Card.TFrame", background="#ffffff")
style.configure("Title.TLabel", background="#ffffff", foreground="#0f172a", font=("Segoe UI", 24, "bold"))
style.configure("Subtitle.TLabel", background="#ffffff", foreground="#64748b", font=("Segoe UI", 10))
style.configure("Field.TLabel", background="#ffffff", foreground="#334155", font=("Segoe UI", 10, "bold"))
style.configure("TEntry", padding=9, font=("Segoe UI", 11))
style.configure("Accent.TButton", background="#2563eb", foreground="#ffffff", padding=10, font=("Segoe UI", 10, "bold"))
style.map("Accent.TButton", background=[("active", "#1d4ed8")])
style.configure("Quiet.TButton", background="#e2e8f0", foreground="#334155", padding=10, font=("Segoe UI", 10, "bold"))

card = ttk.Frame(root, style="Card.TFrame", padding=30)
card.pack(fill="both", expand=True, padx=24, pady=24)

ttk.Label(card, text="Personal Data Collector", style="Title.TLabel").pack(anchor="w")
ttk.Label(card, text="Enter your details to generate a personal data summary.", style="Subtitle.TLabel").pack(anchor="w", pady=(4, 22))

fields = ttk.Frame(card, style="Card.TFrame")
fields.pack(fill="x")
fields.columnconfigure(0, weight=1)
fields.columnconfigure(1, weight=1)

ttk.Label(fields, text="Name", style="Field.TLabel").grid(row=0, column=0, sticky="w", padx=(0, 8), pady=(0, 6))
ttk.Label(fields, text="Age", style="Field.TLabel").grid(row=0, column=1, sticky="w", padx=(8, 0), pady=(0, 6))
name_entry = ttk.Entry(fields)
age_entry = ttk.Entry(fields)
name_entry.grid(row=1, column=0, sticky="ew", padx=(0, 8), pady=(0, 16))
age_entry.grid(row=1, column=1, sticky="ew", padx=(8, 0), pady=(0, 16))

ttk.Label(fields, text="Height (meters)", style="Field.TLabel").grid(row=2, column=0, sticky="w", padx=(0, 8), pady=(0, 6))
ttk.Label(fields, text="Favourite Number", style="Field.TLabel").grid(row=2, column=1, sticky="w", padx=(8, 0), pady=(0, 6))
height_entry = ttk.Entry(fields)
favourite_entry = ttk.Entry(fields)
height_entry.grid(row=3, column=0, sticky="ew", padx=(0, 8))
favourite_entry.grid(row=3, column=1, sticky="ew", padx=(8, 0))

button_row = ttk.Frame(card, style="Card.TFrame")
button_row.pack(fill="x", pady=(24, 0))
ttk.Button(button_row, text="Generate", command=generate_data, style="Accent.TButton").pack(side="left", expand=True, fill="x", padx=(0, 6))
ttk.Button(button_row, text="Clear", command=clear_form, style="Quiet.TButton").pack(side="left", expand=True, fill="x", padx=(6, 0))

result_frame = tk.Frame(card, bg="#f8fafc", padx=16, pady=14)
result_frame.pack(fill="both", expand=True, pady=(24, 0))
tk.Label(result_frame, text="RESULT SUMMARY", bg="#f8fafc", fg="#475569", font=("Segoe UI", 9, "bold"), anchor="w").pack(fill="x")
result_label = tk.Label(result_frame, text="Generated data will appear here.", bg="#f8fafc", fg="#64748b", font=("Consolas", 11), justify="left", anchor="nw", pady=8)
result_label.pack(fill="both", expand=True)

root.bind("<Return>", lambda event: generate_data())
name_entry.focus_set()
root.mainloop()