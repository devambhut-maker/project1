import tkinter as tk
from tkinter import ttk


def calculate():
    """Read the form values, calculate the result, and update the status."""
    try:
        first_number = float(first_entry.get())
        second_number = float(second_entry.get())
    except ValueError:
        result_label.config(text="Enter valid numbers", foreground="#b42318")
        return

    operation = operation_var.get()
    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        if second_number == 0:
            result_label.config(text="Cannot divide by zero", foreground="#b42318")
            return
        result = first_number / second_number

    result_label.config(text=f"Result: {result:g}", foreground="#166534")


def clear_form():
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    operation_var.set("+")
    result_label.config(text="Your answer will appear here", foreground="#64748b")
    first_entry.focus_set()


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("420x390")
root.minsize(360, 340)
root.configure(bg="#f8fafc")

style = ttk.Style()
style.theme_use("clam")
style.configure("Card.TFrame", background="#ffffff")
style.configure("Title.TLabel", background="#ffffff", foreground="#0f172a", font=("Segoe UI", 22, "bold"))
style.configure("Subtitle.TLabel", background="#ffffff", foreground="#64748b", font=("Segoe UI", 10))
style.configure("Field.TLabel", background="#ffffff", foreground="#334155", font=("Segoe UI", 10, "bold"))
style.configure("TEntry", padding=9, font=("Segoe UI", 12))
style.configure("TCombobox", padding=8, font=("Segoe UI", 12))
style.configure("Accent.TButton", background="#2563eb", foreground="#ffffff", padding=10, font=("Segoe UI", 10, "bold"))
style.map("Accent.TButton", background=[("active", "#1d4ed8")])
style.configure("Quiet.TButton", background="#e2e8f0", foreground="#334155", padding=10, font=("Segoe UI", 10, "bold"))

card = ttk.Frame(root, style="Card.TFrame", padding=28)
card.pack(fill="both", expand=True, padx=24, pady=24)

ttk.Label(card, text="Simple Calculator", style="Title.TLabel").pack(anchor="w")
ttk.Label(card, text="Enter two values and choose an operation.", style="Subtitle.TLabel").pack(anchor="w", pady=(4, 22))

ttk.Label(card, text="First number", style="Field.TLabel").pack(anchor="w")
first_entry = ttk.Entry(card)
first_entry.pack(fill="x", pady=(6, 14))

ttk.Label(card, text="Second number", style="Field.TLabel").pack(anchor="w")
second_entry = ttk.Entry(card)
second_entry.pack(fill="x", pady=(6, 14))

operation_var = tk.StringVar(value="+")
ttk.Label(card, text="Operation", style="Field.TLabel").pack(anchor="w")
operation_box = ttk.Combobox(card, textvariable=operation_var, values=("+", "-", "*", "/"), state="readonly")
operation_box.pack(fill="x", pady=(6, 18))

button_row = ttk.Frame(card, style="Card.TFrame")
button_row.pack(fill="x")
ttk.Button(button_row, text="Calculate", command=calculate, style="Accent.TButton").pack(side="left", expand=True, fill="x", padx=(0, 6))
ttk.Button(button_row, text="Clear", command=clear_form, style="Quiet.TButton").pack(side="left", expand=True, fill="x", padx=(6, 0))

result_label = tk.Label(card, text="Your answer will appear here", bg="#ffffff", fg="#64748b", font=("Segoe UI", 12, "bold"), pady=20)
result_label.pack(fill="x")

root.bind("<Return>", lambda event: calculate())
first_entry.focus_set()
root.mainloop()