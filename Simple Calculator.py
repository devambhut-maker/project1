import tkinter as tk
from tkinter import ttk


def calculate():
    try:
        first_number = float(first_entry.get())
        second_number = float(second_entry.get())
    except ValueError:
        show_message("Please enter valid numbers.", "#b42318")
        return

    operation = operation_var.get()
    if operation == "Addition (+)":
        result = first_number + second_number
    elif operation == "Subtraction (-)":
        result = first_number - second_number
    elif operation == "Multiplication (*)":
        result = first_number * second_number
    elif operation == "Division (/)":
        if second_number == 0:
            show_message("Division by zero is not allowed.", "#b42318")
            return
        result = first_number / second_number
    else:
        show_message("Choose an operation.", "#b42318")
        return

    show_message(f"Result: {result:g}", "#166534")


def show_message(message, color):
    result_label.config(text=message, foreground=color)


def clear_form():
    first_entry.delete(0, tk.END)
    second_entry.delete(0, tk.END)
    operation_var.set("Addition (+)")
    show_message("Your result will appear here.", "#64748b")
    first_entry.focus_set()


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("430x430")
root.minsize(360, 370)
root.configure(bg="#eef2ff")

style = ttk.Style()
style.theme_use("clam")
style.configure("Card.TFrame", background="#ffffff")
style.configure(
    "Title.TLabel",
    background="#ffffff",
    foreground="#172554",
    font=("Segoe UI", 24, "bold"),
)
style.configure(
    "Subtitle.TLabel",
    background="#ffffff",
    foreground="#64748b",
    font=("Segoe UI", 10),
)
style.configure(
    "Field.TLabel",
    background="#ffffff",
    foreground="#334155",
    font=("Segoe UI", 10, "bold"),
)
style.configure("TEntry", padding=9, font=("Segoe UI", 12))
style.configure("TCombobox", padding=8, font=("Segoe UI", 11))
style.configure(
    "Accent.TButton",
    background="#4f46e5",
    foreground="#ffffff",
    padding=10,
    font=("Segoe UI", 10, "bold"),
)
style.map("Accent.TButton", background=[("active", "#4338ca")])
style.configure(
    "Quiet.TButton",
    background="#e2e8f0",
    foreground="#334155",
    padding=10,
    font=("Segoe UI", 10, "bold"),
)

card = ttk.Frame(root, style="Card.TFrame", padding=30)
card.pack(fill="both", expand=True, padx=24, pady=24)

ttk.Label(card, text="Simple Calculator", style="Title.TLabel").pack(anchor="w")
ttk.Label(
    card,
    text="A quick way to work with two numbers.",
    style="Subtitle.TLabel",
).pack(anchor="w", pady=(4, 24))

ttk.Label(card, text="First number", style="Field.TLabel").pack(anchor="w")
first_entry = ttk.Entry(card)
first_entry.pack(fill="x", pady=(6, 16))

ttk.Label(card, text="Second number", style="Field.TLabel").pack(anchor="w")
second_entry = ttk.Entry(card)
second_entry.pack(fill="x", pady=(6, 16))

ttk.Label(card, text="Operation", style="Field.TLabel").pack(anchor="w")
operation_var = tk.StringVar(value="Addition (+)")
operation_box = ttk.Combobox(
    card,
    textvariable=operation_var,
    values=(
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (*)",
        "Division (/)",
    ),
    state="readonly",
)
operation_box.pack(fill="x", pady=(6, 22))

button_row = ttk.Frame(card, style="Card.TFrame")
button_row.pack(fill="x")
ttk.Button(
    button_row,
    text="Calculate",
    command=calculate,
    style="Accent.TButton",
).pack(side="left", expand=True, fill="x", padx=(0, 6))
ttk.Button(
    button_row,
    text="Clear",
    command=clear_form,
    style="Quiet.TButton",
).pack(side="left", expand=True, fill="x", padx=(6, 0))

result_label = tk.Label(
    card,
    text="Your result will appear here.",
    background="#ffffff",
    foreground="#64748b",
    font=("Segoe UI", 12, "bold"),
    pady=24,
)
result_label.pack(fill="x")

root.bind("<Return>", lambda event: calculate())
first_entry.focus_set()
root.mainloop()