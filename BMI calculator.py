import tkinter as tk
from tkinter import ttk, messagebox
import math

class BMICalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        
        # Color Palette - Blue, Purple, Pink Gradient
        self.blue = "#1E3A8A"
        self.purple = "#7C3AED"
        self.pink = "#EC4899"
        self.light_purple = "#A78BFA"
        self.light_pink = "#F472B6"
        self.bg_gradient = "#0F172A"
        self.white = "#FFFFFF"
        self.card_bg = "#F8FAFC"
        
        self.current_bmi = None
        self.setup_ui()
        
    def setup_ui(self):
        """Setup the main UI"""
        # Main background
        main_bg = tk.Frame(self.root, bg=self.bg_gradient)
        main_bg.pack(fill=tk.BOTH, expand=True)
        
        # Title section with gradient effect
        title_frame = tk.Frame(main_bg, bg=self.bg_gradient, height=80)
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame,
            text="BMI Calculator",
            font=("Segoe UI", 28, "bold"),
            bg=self.bg_gradient,
            fg=self.white
        )
        title_label.pack(pady=15)
        
        subtitle_label = tk.Label(
            title_frame,
            text="Know Your Health Status",
            font=("Segoe UI", 11),
            bg=self.bg_gradient,
            fg=self.light_purple
        )
        subtitle_label.pack()
        
        # Main content card (white rounded effect)
        card_frame = tk.Frame(main_bg, bg=self.card_bg, relief=tk.FLAT)
        card_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        # Weight input section
        weight_label = tk.Label(
            card_frame,
            text="Weight (kg)",
            font=("Segoe UI", 12, "bold"),
            bg=self.card_bg,
            fg=self.blue
        )
        weight_label.pack(pady=(20, 5), anchor=tk.W, padx=20)
        
        self.weight_entry = tk.Entry(
            card_frame,
            font=("Segoe UI", 14),
            width=20,
            justify=tk.CENTER,
            bg="#F1F5F9",
            fg=self.blue,
            relief=tk.FLAT,
            insertbackground=self.purple,
            bd=0
        )
        self.weight_entry.pack(pady=5, padx=20, fill=tk.X, ipady=8)
        self.weight_entry.bind("<FocusIn>", lambda e: self.on_focus_in(self.weight_entry))
        self.weight_entry.bind("<FocusOut>", lambda e: self.on_focus_out(self.weight_entry))
        
        # Height input section
        height_label = tk.Label(
            card_frame,
            text="Height (m)",
            font=("Segoe UI", 12, "bold"),
            bg=self.card_bg,
            fg=self.blue
        )
        height_label.pack(pady=(15, 5), anchor=tk.W, padx=20)
        
        self.height_entry = tk.Entry(
            card_frame,
            font=("Segoe UI", 14),
            width=20,
            justify=tk.CENTER,
            bg="#F1F5F9",
            fg=self.blue,
            relief=tk.FLAT,
            insertbackground=self.purple,
            bd=0
        )
        self.height_entry.pack(pady=5, padx=20, fill=tk.X, ipady=8)
        self.height_entry.bind("<FocusIn>", lambda e: self.on_focus_in(self.height_entry))
        self.height_entry.bind("<FocusOut>", lambda e: self.on_focus_out(self.height_entry))
        
        # Buttons frame
        button_frame = tk.Frame(card_frame, bg=self.card_bg)
        button_frame.pack(pady=25, padx=20, fill=tk.X)
        
        # Calculate BMI button
        self.calculate_btn = tk.Button(
            button_frame,
            text="📊 Calculate BMI",
            font=("Segoe UI", 13, "bold"),
            bg=self.purple,
            fg=self.white,
            command=self.calculate_bmi,
            relief=tk.FLAT,
            height=2,
            cursor="hand2",
            activebackground=self.light_purple,
            activeforeground=self.white
        )
        self.calculate_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        self.calculate_btn.bind("<Enter>", lambda e: self.on_btn_enter(self.calculate_btn, self.light_purple))
        self.calculate_btn.bind("<Leave>", lambda e: self.on_btn_leave(self.calculate_btn, self.purple))
        
        # Clear button
        self.clear_btn = tk.Button(
            button_frame,
            text="🗑️ Clear",
            font=("Segoe UI", 13, "bold"),
            bg=self.pink,
            fg=self.white,
            command=self.clear_fields,
            relief=tk.FLAT,
            height=2,
            cursor="hand2",
            activebackground=self.light_pink,
            activeforeground=self.white
        )
        self.clear_btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        self.clear_btn.bind("<Enter>", lambda e: self.on_btn_enter(self.clear_btn, self.light_pink))
        self.clear_btn.bind("<Leave>", lambda e: self.on_btn_leave(self.clear_btn, self.pink))
        
        # Result section
        self.result_frame = tk.Frame(card_frame, bg="#F0F9FF", relief=tk.FLAT, highlightthickness=0)
        self.result_frame.pack(pady=(20, 0), padx=20, fill=tk.BOTH, expand=True)
        
        # BMI Display
        self.bmi_display = tk.Label(
            self.result_frame,
            text="--",
            font=("Segoe UI", 32, "bold"),
            bg="#F0F9FF",
            fg=self.blue
        )
        self.bmi_display.pack(pady=(15, 0))
        
        # Category Display
        self.category_display = tk.Label(
            self.result_frame,
            text="Enter your details",
            font=("Segoe UI", 12),
            bg="#F0F9FF",
            fg=self.purple
        )
        self.category_display.pack(pady=(5, 15))
        
    def on_focus_in(self, entry):
        """Highlight entry on focus"""
        entry.config(bg="#E0E7FF", fg=self.purple)
        
    def on_focus_out(self, entry):
        """Reset entry color on focus out"""
        entry.config(bg="#F1F5F9", fg=self.blue)
        
    def on_btn_enter(self, btn, color):
        """Hover effect on button"""
        btn.config(bg=color)
        
    def on_btn_leave(self, btn, color):
        """Reset button color"""
        btn.config(bg=color)
    
    def calculate_bmi(self):
        """Calculate BMI and display result"""
        try:
            weight_text = self.weight_entry.get().strip()
            height_text = self.height_entry.get().strip()
            
            if not weight_text or not height_text:
                messagebox.showwarning("Input Error", "Please enter both weight and height!")
                return
            
            weight = float(weight_text)
            height = float(height_text)
            
            if weight <= 0 or height <= 0:
                messagebox.showerror("Invalid Input", "Weight and Height must be positive numbers!")
                return
            
            if height > 3:
                messagebox.showwarning("Height Check", "Height seems too high. Use meters (e.g., 1.75)")
                return
            
            self.current_bmi = weight / (height * height)
            self.display_result()
            
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers only!")
    
    def display_result(self):
        """Display BMI result with color coding"""
        bmi = self.current_bmi
        bmi_rounded = round(bmi, 1)
        
        self.bmi_display.config(text=f"{bmi_rounded}")
        
        # Color coding for categories
        if bmi < 18.5:
            category = "Underweight"
            color = "#0369A1"  # Blue
            self.result_frame.config(bg="#F0F9FF")
        elif bmi < 25:
            category = "Normal Weight"
            color = "#15803D"  # Green
            self.result_frame.config(bg="#F0FDF4")
        elif bmi < 30:
            category = "Overweight"
            color = "#EA580C"  # Orange
            self.result_frame.config(bg="#FFF7ED")
        else:
            category = "Obese"
            color = "#DC2626"  # Red
            self.result_frame.config(bg="#FEF2F2")
        
        self.bmi_display.config(fg=color)
        self.category_display.config(text=f"Status: {category}", fg=color)
    
    def clear_fields(self):
        """Clear all input fields and reset display"""
        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)
        self.bmi_display.config(text="--", fg=self.blue)
        self.category_display.config(text="Enter your details", fg=self.purple)
        self.result_frame.config(bg="#F0F9FF")
        self.weight_entry.focus()
        self.current_bmi = None

if __name__ == "__main__":
    root = tk.Tk()
    app = BMICalculator(root)
    root.mainloop()