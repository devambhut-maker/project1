import tkinter as tk
from tkinter import messagebox


BG = "#120f2d"
PANEL = "#211b4a"
CARD = "#2d255d"
ACCENT = "#8b5cf6"
ACCENT_HOVER = "#a78bfa"
TEXT = "#f8fafc"
MUTED = "#b8b5d6"


def rounded_rectangle(canvas, x1, y1, x2, y2, radius, fill, outline=None):
    points = [
        x1 + radius, y1,
        x2 - radius, y1,
        x2, y1 + radius,
        x2, y2 - radius,
        x2 - radius, y2,
        x1 + radius, y2,
        x1, y2 - radius,
        x1, y1 + radius,
    ]
    return canvas.create_polygon(
        points,
        smooth=True,
        fill=fill,
        outline=outline or fill,
    )


def convert_time():
    value = seconds_entry.get().strip()

    if not value:
        messagebox.showerror("Invalid Input", "Please enter total seconds.")
        return

    try:
        total_seconds = int(value)
        if total_seconds < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Enter a valid non-negative whole number.",
        )
        return

    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    hours_value.config(text=f"{hours:02d}")
    minutes_value.config(text=f"{minutes:02d}")
    seconds_value.config(text=f"{seconds:02d}")


def reset_time():
    seconds_entry.delete(0, tk.END)
    hours_value.config(text="00")
    minutes_value.config(text="00")
    seconds_value.config(text="00")
    seconds_entry.focus_set()


def button_hover(button, normal_color, hover_color):
    button.bind("<Enter>", lambda event: button.config(bg=hover_color))
    button.bind("<Leave>", lambda event: button.config(bg=normal_color))


root = tk.Tk()
root.title("Time Converter")
root.geometry("500x550")
root.resizable(False, False)
root.configure(bg=BG)

canvas = tk.Canvas(root, width=500, height=550, bg=BG, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Decorative glassmorphism circles
canvas.create_oval(-100, -80, 160, 180, fill="#29205e", outline="")
canvas.create_oval(390, 380, 620, 610, fill="#1d2855", outline="")

# Title
canvas.create_text(
    250,
    55,
    text="TIME CONVERTER",
    fill=TEXT,
    font=("Segoe UI", 25, "bold"),
)
canvas.create_text(
    250,
    88,
    text="DIGITAL TIME CALCULATOR",
    fill=MUTED,
    font=("Segoe UI", 9, "bold"),
)

# Main glass panel
rounded_rectangle(canvas, 35, 115, 465, 505, 24, PANEL)

canvas.create_text(
    250,
    150,
    text="TOTAL SECONDS",
    fill=MUTED,
    font=("Segoe UI", 10, "bold"),
)

seconds_entry = tk.Entry(
    root,
    width=18,
    justify="center",
    bg="#30285f",
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    bd=0,
    font=("Segoe UI", 19, "bold"),
)
seconds_entry.place(x=105, y=172, width=290, height=50)

convert_button = tk.Button(
    root,
    text="CONVERT",
    command=convert_time,
    bg=ACCENT,
    fg="white",
    activebackground=ACCENT_HOVER,
    activeforeground="white",
    relief="flat",
    bd=0,
    cursor="hand2",
    font=("Segoe UI", 10, "bold"),
)
convert_button.place(x=105, y=240, width=140, height=42)
button_hover(convert_button, ACCENT, ACCENT_HOVER)

reset_button = tk.Button(
    root,
    text="RESET",
    command=reset_time,
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
button_hover(reset_button, "#40386d", "#514889")

# Result cards
result_cards = [
    (55, "HOURS"),
    (175, "MINUTES"),
    (295, "SECONDS"),
]

result_values = []

for x, label in result_cards:
    rounded_rectangle(canvas, x, 325, x + 105, 430, 18, CARD)
    canvas.create_text(
        x + 52,
        350,
        text=label,
        fill=MUTED,
        font=("Segoe UI", 9, "bold"),
    )

    value_label = tk.Label(
        root,
        text="00",
        bg=CARD,
        fg=TEXT,
        font=("Consolas", 27, "bold"),
    )
    value_label.place(x=x + 5, y=365, width=95, height=50)
    result_values.append(value_label)

hours_value, minutes_value, seconds_value = result_values

canvas.create_text(
    250,
    475,
    text="Convert seconds into hours, minutes and seconds",
    fill=MUTED,
    font=("Segoe UI", 9),
)

seconds_entry.focus_set()
root.bind("<Return>", lambda event: convert_time())
root.bind("<Escape>", lambda event: reset_time())

root.mainloop()