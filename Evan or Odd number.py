import tkinter as tk
from tkinter import ttk


# Color palette
BG_COLOR = "#071426"
CARD_COLOR = "#0D2038"
CYAN = "#00E5FF"
TEXT_COLOR = "#E6F7FF"
MUTED_TEXT = "#8EA9BA"
GREEN = "#19D36B"
ORANGE = "#FF9F43"
RED = "#FF4D6D"
ENTRY_COLOR = "#102B46"


def check_number():
    value = number_var.get().strip()

    try:
        number = int(value)
    except ValueError:
        result_label.config(
            text="Please enter a valid number.",
            foreground=RED,
            background="#321522"
        )
        return

    if number % 2 == 0:
        result_label.config(
            text=f"{number} is Even",
            foreground=GREEN,
            background="#103522"
        )
    else:
        result_label.config(
            text=f"{number} is Odd",
            foreground=ORANGE,
            background="#3A2815"
        )


def reset():
    number_var.set("")
    result_label.config(
        text="Your result will appear here",
        foreground=MUTED_TEXT,
        background="#102B46"
    )
    number_entry.focus()


def add_hover_effect(button, normal_style, hover_style):
    button.bind(
        "<Enter>",
        lambda event: button.configure(style=hover_style)
    )
    button.bind(
        "<Leave>",
        lambda event: button.configure(style=normal_style)
    )


root = tk.Tk()
root.title("Even or Odd Checker")
root.geometry("450x500")
root.configure(background=BG_COLOR)
root.resizable(False, False)

# Center the window
root.update_idletasks()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_position = (screen_width - 450) // 2
y_position = (screen_height - 500) // 2
root.geometry(f"450x500+{x_position}+{y_position}")

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Check.TButton",
    font=("Segoe UI Semibold", 11),
    foreground=BG_COLOR,
    background=CYAN,
    padding=(20, 12),
    borderwidth=0
)
style.configure(
    "CheckHover.TButton",
    font=("Segoe UI Semibold", 11),
    foreground=BG_COLOR,
    background="#66F1FF",
    padding=(20, 12),
    borderwidth=0
)
style.configure(
    "Reset.TButton",
    font=("Segoe UI Semibold", 11),
    foreground=TEXT_COLOR,
    background="#24415D",
    padding=(20, 12),
    borderwidth=0
)
style.configure(
    "ResetHover.TButton",
    font=("Segoe UI Semibold", 11),
    foreground=TEXT_COLOR,
    background="#35617F",
    padding=(20, 12),
    borderwidth=0
)
style.configure(
    "Number.TEntry",
    font=("Segoe UI", 20),
    fieldbackground=ENTRY_COLOR,
    foreground=TEXT_COLOR,
    insertcolor=CYAN,
    padding=12
)

card = tk.Frame(
    root,
    background=CARD_COLOR,
    highlightbackground="#123A58",
    highlightthickness=1
)
card.place(relx=0.5, rely=0.5, anchor="center", width=370, height=420)

title_label = tk.Label(
    card,
    text="EVEN OR ODD",
    font=("Segoe UI Semibold", 24),
    foreground=CYAN,
    background=CARD_COLOR
)
title_label.pack(pady=(35, 6))

subtitle_label = tk.Label(
    card,
    text="Enter a number to check its type",
    font=("Segoe UI", 10),
    foreground=MUTED_TEXT,
    background=CARD_COLOR
)
subtitle_label.pack(pady=(0, 30))

number_var = tk.StringVar()

number_entry = ttk.Entry(
    card,
    textvariable=number_var,
    style="Number.TEntry",
    justify="center",
    width=18
)
number_entry.pack(pady=(0, 25))
number_entry.focus()

button_frame = tk.Frame(card, background=CARD_COLOR)
button_frame.pack()

check_button = ttk.Button(
    button_frame,
    text="Check Number",
    style="Check.TButton",
    command=check_number
)
check_button.grid(row=0, column=0, padx=5)

reset_button = ttk.Button(
    button_frame,
    text="Reset",
    style="Reset.TButton",
    command=reset
)
reset_button.grid(row=0, column=1, padx=5)

add_hover_effect(check_button, "Check.TButton", "CheckHover.TButton")
add_hover_effect(reset_button, "Reset.TButton", "ResetHover.TButton")

result_label = tk.Label(
    card,
    text="Your result will appear here",
    font=("Segoe UI Semibold", 15),
    foreground=MUTED_TEXT,
    background="#102B46",
    width=28,
    height=3,
    wraplength=280
)
result_label.pack(pady=(35, 0))

number_entry.bind("<Return>", lambda event: check_number())

root.mainloop()