import tkinter as tk
from tkinter import ttk
import math

class TemperatureConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Temperature Converter")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        
        # Color scheme - Sunset Orange (#FF6B35) and Blue (#004E89)
        self.orange = "#FF6B35"
        self.blue = "#004E89"
        self.dark_orange = "#E55A2B"
        self.light_blue = "#005BA3"
        self.gradient_orange = "#FFB366"
        self.bg_dark = "#1A1A1A"
        self.text_light = "#FFFFFF"
        
        self.conversion_type = tk.StringVar(value="c_to_f")
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the main UI with gradient background"""
        # Main container
        main_frame = tk.Frame(self.root, bg=self.bg_dark)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            main_frame,
            text="Temperature Converter",
            font=("Segoe UI", 24, "bold"),
            bg=self.bg_dark,
            fg=self.text_light
        )
        title_label.pack(pady=20)
        
        # Toggle buttons frame
        toggle_frame = tk.Frame(main_frame, bg=self.bg_dark)
        toggle_frame.pack(pady=15)
        
        # Celsius to Fahrenheit button
        self.c_to_f_btn = tk.Button(
            toggle_frame,
            text="°C → °F",
            font=("Segoe UI", 12, "bold"),
            bg=self.orange,
            fg=self.text_light,
            command=lambda: self.set_conversion_type("c_to_f"),
            relief=tk.FLAT,
            width=15,
            height=2,
            cursor="hand2"
        )
        self.c_to_f_btn.pack(side=tk.LEFT, padx=10)
        self.c_to_f_btn.bind("<Enter>", lambda e: self.c_to_f_btn.config(bg=self.dark_orange))
        self.c_to_f_btn.bind("<Leave>", lambda e: self.update_button_colors())
        
        # Fahrenheit to Celsius button
        self.f_to_c_btn = tk.Button(
            toggle_frame,
            text="°F → °C",
            font=("Segoe UI", 12, "bold"),
            bg=self.blue,
            fg=self.text_light,
            command=lambda: self.set_conversion_type("f_to_c"),
            relief=tk.FLAT,
            width=15,
            height=2,
            cursor="hand2"
        )
        self.f_to_c_btn.pack(side=tk.LEFT, padx=10)
        self.f_to_c_btn.bind("<Enter>", lambda e: self.f_to_c_btn.config(bg=self.light_blue))
        self.f_to_c_btn.bind("<Leave>", lambda e: self.update_button_colors())
        
        # Input section
        input_frame = tk.Frame(main_frame, bg=self.bg_dark)
        input_frame.pack(pady=30)
        
        input_label = tk.Label(
            input_frame,
            text="Enter Temperature",
            font=("Segoe UI", 12),
            bg=self.bg_dark,
            fg=self.text_light
        )
        input_label.pack()
        
        # Styled input box
        self.input_entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 16, "bold"),
            width=15,
            justify=tk.CENTER,
            bg="#2A2A2A",
            fg=self.orange,
            relief=tk.FLAT,
            insertbackground=self.orange
        )
        self.input_entry.pack(pady=10, ipady=8)
        
        # Convert button with glow effect
        self.convert_btn = tk.Button(
            main_frame,
            text="🔄 CONVERT",
            font=("Segoe UI", 13, "bold"),
            bg=self.gradient_orange,
            fg=self.text_light,
            command=self.convert_temperature,
            relief=tk.FLAT,
            width=25,
            height=2,
            cursor="hand2",
            activebackground="#FFC266",
            activeforeground=self.text_light
        )
        self.convert_btn.pack(pady=15)
        self.convert_btn.bind("<Enter>", lambda e: self.convert_btn.config(bg="#FFC266"))
        self.convert_btn.bind("<Leave>", lambda e: self.convert_btn.config(bg=self.gradient_orange))
        
        # Result card
        self.result_frame = tk.Frame(
            main_frame,
            bg="#2A2A2A",
            relief=tk.FLAT,
            highlightthickness=2,
            highlightbackground=self.orange
        )
        self.result_frame.pack(pady=20, padx=30, fill=tk.BOTH, expand=True)
        
        # Result label
        result_label = tk.Label(
            self.result_frame,
            text="Result",
            font=("Segoe UI", 11),
            bg="#2A2A2A",
            fg=self.gradient_orange
        )
        result_label.pack(pady=(15, 5))
        
        # Result display with icon
        self.result_display = tk.Label(
            self.result_frame,
            text="--",
            font=("Segoe UI", 28, "bold"),
            bg="#2A2A2A",
            fg=self.text_light
        )
        self.result_display.pack(pady=10)
        
    def set_conversion_type(self, conv_type):
        """Set the conversion type and update button appearance"""
        self.conversion_type.set(conv_type)
        self.update_button_colors()
        
    def update_button_colors(self):
        """Update button colors based on selected conversion type"""
        if self.conversion_type.get() == "c_to_f":
            self.c_to_f_btn.config(bg=self.orange)
            self.f_to_c_btn.config(bg=self.blue)
        else:
            self.c_to_f_btn.config(bg=self.blue)
            self.f_to_c_btn.config(bg=self.orange)
    
    def convert_temperature(self):
        """Perform temperature conversion"""
        try:
            temp_input = self.input_entry.get().strip()
            if not temp_input:
                self.result_display.config(text="Enter a value", fg="#FF6B6B")
                return
            
            temp = float(temp_input)
            
            if self.conversion_type.get() == "c_to_f":
                result = (temp * 9/5) + 32
                self.result_display.config(text=f"{result:.1f} °F", fg=self.orange)
            else:
                result = (temp - 32) * 5/9
                self.result_display.config(text=f"{result:.1f} °C", fg=self.blue)
                
        except ValueError:
            self.result_display.config(text="Invalid Input", fg="#FF6B6B")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverter(root)
    root.mainloop()