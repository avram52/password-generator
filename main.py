import tkinter as tk
from tkinter import messagebox, scrolledtext
import random
import string
import datetime

"""
🔐 Password Generator - Learning Edition
========================================
Educational project demonstrating:
- Python GUI with tkinter
- Class-based architecture
- Secure password generation
- Best practices for portfolio projects
"""


class PasswordGeneratorGUI:
    """
    Main application class for the password generator.

    This demonstrates class-based design pattern where we separate:
    - Data (configuration)
    - Methods (functions)
    - UI components (widgets)
    """

    def __init__(self):
        # ===========================================
        # INITIALIZATION SECTION
        # ===========================================

        self.master = tk.Tk()
        self.master.title("🔐 Secure Password Generator")
        self.master.geometry("450x600")
        self.master.minsize(400, 550)

        # Character sets - stored as class attributes
        # This is a best practice: keep constants in __init__
        self.letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.digits = string.digits  # '0123456789'
        self.symbols = string.punctuation  # '!@#$%^&*()_+-=[]{}|;:,.<>?/~`'

        # Password storage - empty initially
        self.password = ""
        self.is_generated = False

        # Build all GUI components
        self._create_widgets()

    def _create_widgets(self):
        """
        Create and arrange all user interface components.
        This demonstrates tkinter widget organization.
        """

        # ===========================================
        # TITLE SECTION (Top Bar)
        # ===========================================
        title_frame = tk.Frame(self.master, bg="#2c3e50", height=45)
        title_frame.pack(fill=tk.X)

        title_label = tk.Label(
            title_frame,
            text="🔐 Password Generator - Learning Edition",
            font=("Helvetica", 18, "bold"),
            fg="white",
            bg="#2c3e50"
        )
        title_label.pack(pady=5)

        # ===========================================
        # PASSWORD DISPLAY SECTION
        # ===========================================
        display_frame = tk.Frame(self.master, bg="#3498db", bd=3, relief="raised")
        display_frame.pack(fill=tk.X, pady=(10, 15))

        self.password_label = tk.Label(
            display_frame,
            text="👆 Drag slider • Select options • Generate!",
            font=("Helvetica", 12),
            fg="#ecf0f1",
            bg="#3498db"
        )
        self.password_label.pack(expand=True)

        # ===========================================
        # VISUAL SLIDER BAR (Proton Pass Style)
        # ===========================================
        slider_frame = tk.Frame(self.master, bg="#ecf0f1")
        slider_frame.pack(fill=tk.X, pady=(0, 20))

        # Slider configuration - range from 8 to 64 characters
        min_len = 8
        max_len = 64

        self.slider = tk.Scale(
            slider_frame,
            from_=min_len,
            to=max_len,
            orient=tk.HORIZONTAL,
            length=300,
            bg="#ecf0f1",
            troughcolor="#bdc3c7",
            highlightthickness=0,
            width=28,
            relief=tk.FLAT,
            activebackground="#e74c3c"  # Red bar when dragging
        )

        # Configure slider visual appearance
        self.slider.pack(pady=10)

        self.value_label = tk.Label(
            slider_frame,
            text=f"Length: {min_len}",
            font=("Helvetica", 11),
            bg="#ecf0f1",
            fg="#2c3e50",
            relief="raised",
            padx=10
        )
        self.value_label.pack()

        # ===========================================
        # CHARACTER TYPE CHECKBOXES
        # ===========================================
        check_frame = tk.Frame(self.master, bg="#ecf0f1")
        check_frame.pack(fill=tk.X, pady=(20, 15))

        # Using BooleanVar for checkbox state management
        self.letters_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.symbols_var = tk.BooleanVar(value=True)

        # Create checkboxes with proper alignment
        tk.Checkbutton(
            check_frame,
            text="✓ Include Letters (a-z A-Z)",
            variable=self.letters_var,
            width=25
        ).pack(anchor=tk.W, pady=5)

        tk.Checkbutton(
            check_frame,
            text="✓ Include Numbers (0-9)",
            variable=self.digits_var,
            width=25
        ).pack(anchor=tk.W, pady=5)

        tk.Checkbutton(
            check_frame,
            text="✓ Include Symbols (!@#$%)",
            variable=self.symbols_var,
            width=25
        ).pack(anchor=tk.W, pady=5)

        # ===========================================
        # GENERATE AND COPY BUTTONS
        # ===========================================
        btn_container = tk.Frame(self.master, bg="#ecf0f1")
        btn_container.pack(fill=tk.X, pady=15)

        self.generate_btn = tk.Button(
            btn_container,
            text="🔐 Generate Password",
            command=self._generate_password,
            bg="#27ae60",
            fg="white",
            font=("Helvetica", 13, "bold"),
            relief=tk.FLAT,
            width=28,
            height=2,
            activebackground="#2ecc71"
        )
        self.generate_btn.pack(pady=(0, 5))

        self.copy_btn = tk.Button(
            btn_container,
            text="📋 Copy to Clipboard",
            command=self._copy_password,
            state=tk.DISABLED,  # Disabled until password generated
            bg="#3498db",
            fg="white",
            font=("Helvetica", 12),
            relief=tk.FLAT,
            width=28,
            height=2
        )
        self.copy_btn.pack(pady=(0, 5))

        # ===========================================
        # OUTPUT TEXT BOX
        # ===========================================
        output_frame = tk.Frame(self.master, bg="#ecf0f1")
        output_frame.pack(fill=tk.BOTH, pady=10)

        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            height=3,
            font=("Helvetica", 12),
            bg="#2c3e50",
            fg="#ecf0f1",
            insertbackground="white"
        )
        self.output_text.pack(fill=tk.X)

        # ===========================================
        # FOOTER INFO
        # ===========================================
        footer_frame = tk.Frame(self.master, bg="#ecf0f1")
        footer_frame.pack(fill=tk.X, padx=20, pady=(15, 20))

        footer_label = tk.Label(
            footer_frame,
            text="📚 LEARNING RESOURCES:\n"
                 "• tkinter = Python GUI framework\n"
                 "• random = Cryptographically safe generation\n"
                 "• Class design = OOP best practices",
            font=("Helvetica", 9),
            bg="#ecf0f1",
            fg="#7f8c8d",
            justify=tk.LEFT,
            anchor=tk.W
        )
        footer_label.pack()

        # ===========================================
        # SECURITY NOTICE
        # ===========================================
        security_frame = tk.Frame(self.master, bg="#e74c3c")
        security_frame.pack(fill=tk.X)

        security_label = tk.Label(
            security_frame,
            text="⚠️ NEVER share passwords publicly\n"
                 "Use a password manager (Bitwarden/1Password)",
            font=("Helvetica", 9),
            fg="white",
            bg="#e74c3c"
        )
        security_label.pack(pady=5)

    def _generate_password(self):
        """
        Main password generation logic.

        This demonstrates:
        - Modular design (separate method)
        - Security considerations
        - User feedback through UI
        """

        try:
            # Get current slider value (convert to int)
            min_len = 8
            max_len = 64
            current_len = int(self.slider.get())

            # Check checkbox states
            use_letters = self.letters_var.get()
            use_digits = self.digits_var.get()
            use_symbols = self.symbols_var.get()

            # Build character pool - security consideration
            available_chars = []

            if use_letters:
                available_chars.extend(self.letters)
            if use_digits:
                available_chars.extend(self.digits)
            if use_symbols:
                available_chars.extend(self.symbols)

            # Validate configuration
            if not (use_letters or use_digits or use_symbols):
                messagebox.showerror(
                    "Configuration Error",
                    "You must select at least one character type!"
                )
                return

            # Edge case: auto-enable letters if nothing selected
            if len(available_chars) == 0:
                available_chars = self.letters
                use_letters = True

            # Generate password using random.choice()
            # This demonstrates secure random selection from pool
            self.password = ''.join(random.choice(available_chars) for _ in range(current_len))

            # Display result in output box
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"\n🔐 Generated Password:\n{self.password}\n" +
                                    "=" * len(self.password) + "\n")

            # Enable copy button
            self.copy_btn.config(state=tk.NORMAL)

            # Update status label
            self.password_label.config(text=f"✅ {current_len}-character password generated!")

            self.is_generated = True

        except Exception as e:
            messagebox.showerror("Error", f"Generation failed:\n{str(e)}")

    def _copy_password(self):
        """Copy password to clipboard with notification."""

        if self.is_generated:
            # Clear and paste - standard clipboard operations
            self.master.clipboard_clear()
            self.master.clipboard_append(self.password)

            # Show success message
            messagebox.showinfo(
                "Copied!",
                f"✓ Password copied to clipboard:\n\n{self.password}\n\n💡 Paste in your password manager!"
            )


class LearningInfo:
    """
    Educational section - explains concepts in the project.

    This demonstrates documentation best practices.
    """
    concepts = {
        "tkinter": "Python's built-in GUI framework",
        "random.choice()": "Secure random selection from list",
        "Class Design": "Organizing code with OOP principles",
        "ScrolledText": "Scrollable text widget for output",
        "BooleanVar": "State management for checkboxes"
    }


def main():
    """
    Application entry point.

    This demonstrates:
    - Main() function as entry point
    - Clean separation of UI code from logic
    """
    print("=" * 60)
    print("🔐 Secure Password Generator - Learning Edition")
    print("=" * 60)
    print()
    print("This project demonstrates:")
    print("✓ Python GUI development with tkinter")
    print("✓ Object-Oriented Programming (classes)")
    print("✓ Security best practices in password generation")
    print("✓ Clean, commented code for portfolio showcase")
    print()
    print("Run 'main.py' to start the application!")
    print("=" * 60)

    app = PasswordGeneratorGUI()
    app.master.mainloop()


if __name__ == "__main__":
    main()