import tkinter as tk
from tkinter import messagebox


BG = "#120f2d"
PANEL = "#211b4a"
CARD = "#2d255d"
ACCENT = "#8b5cf6"
HOVER = "#a78bfa"
TEXT = "#f8fafc"
MUTED = "#b8b5d6"


def convert_units():
    try:
        kilometers = float(input_entry.get().strip())

        if kilometers < 0:
            raise ValueError

        meters = kilometers * 1000
        centimeters = kilometers * 100000

        meters_value.config(text=f"{meters:,.2f}")
        centimeters_value.config(text=f"{centimeters:,.2f}")

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid non-negative number.",
        )


def reset():
    input_entry.delete(0, tk.END)
    meters_value.config(text="0.00")
    centimeters_value.config(text="0.00")
    input_entry.focus_set()


def add_hover(button, normal, hover):
    button.bind("<Enter>", lambda event: button.config(bg=hover))
    button.bind("<Leave>", lambda event: button.config(bg=normal))


root = tk.Tk()
root.title("Unit Converter")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg=BG)


canvas = tk.Canvas(
    root,
    width=500,
    height=550,
    bg=BG,
    highlightthickness=0,
)
canvas.pack(fill="both", expand=True)

# Decorative background
canvas.create_oval(-100, -80, 160, 180, fill="#29205e", outline="")
canvas.create_oval(390, 390, 620, 620, fill="#1d2855", outline="")

# Header
canvas.create_text(
    250,
    55,
    text="UNIT CONVERTER",
    fill=TEXT,
    font=("Segoe UI", 25, "bold"),
)

canvas.create_text(
    250,
    88,
    text="DISTANCE CONVERSION TOOL",
    fill=MUTED,
    font=("Segoe UI", 9, "bold"),
)

# Main panel
canvas.create_rectangle(
    35,
    115,
    465,
    505,
    fill=PANEL,
    outline=PANEL,
)

canvas.create_text(
    250,
    150,
    text="DISTANCE IN KILOMETERS",
    fill=MUTED,
    font=("Segoe UI", 10, "bold"),
)

input_entry = tk.Entry(
    root,
    justify="center",
    bg="#30285f",
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    font=("Segoe UI", 19, "bold"),
)

input_entry.place(x=105, y=172, width=290, height=50)

convert_button = tk.Button(
    root,
    text="CONVERT",
    command=convert_units,
    bg=ACCENT,
    fg="white",
    activebackground=HOVER,
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    font=("Segoe UI", 10, "bold"),
)

convert_button.place(x=105, y=240, width=140, height=42)
add_hover(convert_button, ACCENT, HOVER)

reset_button = tk.Button(
    root,
    text="RESET",
    command=reset,
    bg="#40386d",
    fg=TEXT,
    activebackground="#514889",
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    font=("Segoe UI", 10, "bold"),
)

reset_button.place(x=255, y=240, width=140, height=42)
add_hover(reset_button, "#40386d", "#514889")

# Result cards
cards = [
    (55, "METERS"),
    (295, "CENTIMETERS"),
]

result_labels = []

for x, title in cards:
    canvas.create_rectangle(
        x,
        325,
        x + 150,
        430,
        fill=CARD,
        outline=CARD,
    )

    canvas.create_text(
        x + 75,
        350,
        text=title,
        fill=MUTED,
        font=("Segoe UI", 9, "bold"),
    )

    value = tk.Label(
        root,
        text="0.00",
        bg=CARD,
        fg=TEXT,
        font=("Consolas", 18, "bold"),
    )

    value.place(x=x + 5, y=365, width=140, height=45)
    result_labels.append(value)

meters_value, centimeters_value = result_labels

canvas.create_text(
    250,
    475,
    text="Convert kilometers into meters and centimeters",
    fill=MUTED,
    font=("Segoe UI", 9),
)

input_entry.focus_set()
root.bind("<Return>", lambda event: convert_units())
root.bind("<Escape>", lambda event: reset())

root.mainloop()
