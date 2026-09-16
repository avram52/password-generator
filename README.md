# 🔐 Secure Password Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.8+" />
  <img src="https://img.shields.io/badge/GUI-Tkinter-3498DB?style=for-the-badge" alt="Tkinter GUI" />
  <img src="https://img.shields.io/badge/License-MIT-2ECC71?style=for-the-badge" alt="License: MIT" />
  <img src="https://img.shields.io/badge/Platform-Windows%20|%20macOS%20|%20Linux-lightgrey?style=for-the-badge" alt="Cross-Platform" />
</p>

<p align="center">
  <strong>A modern, lightweight, and user-friendly desktop password generator built with Python and Tkinter.</strong><br>
  Features a smooth visual slider, customizable character sets, one-click clipboard copying, and zero third-party dependencies.
</p>

---

## 📑 Table of Contents

- [✨ Features](#-features)
- [🖥️ UI Preview](#️-ui-preview)
- [📋 Prerequisites](#-prerequisites)
- [🚀 Quick Start](#-quick-start)
- [🏗️ Project Architecture](#️-project-architecture)
- [💡 How to Use](#-how-to-use)
- [🛡️ Password Security Tips](#️-password-security-tips)
- [🗺️ Roadmap & Ideas](#️-roadmap--ideas)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## ✨ Features

- 🎚️ **Interactive Slider Bar**: Seamlessly adjust password length from **8 to 64 characters** in real-time.
- ⚙️ **Customizable Character Sets**: Toggle individual character pools on or off:
  - Uppercase & Lowercase Letters (`a-z`, `A-Z`)
  - Digits (`0-9`)
  - Special Symbols (`!@#$%^&*()_+-=[]{}|;:,.<>?/~` `)
- 📋 **One-Click Clipboard Copy**: Instantly copy your generated password to the system clipboard with feedback dialogs.
- 🛡️ **Validation & Error Guarding**: Built-in validation prevents empty configuration errors with helpful user prompts.
- 📦 **Zero External Dependencies**: Powered purely by Python's standard library (`tkinter`, `random`, `string`).
- 🎓 **Clean OOP Codebase**: Organized into clear classes and methods with rich comments—ideal for learning and portfolios.

---

## 🖥️ UI Preview

```text
+-----------------------------------------------+
|  🔐 Password Generator - Learning Edition     |
+-----------------------------------------------+
|  [ ✅ 16-character password generated!     ]  |
+-----------------------------------------------+
|                                               |
|   Length: 16                                  |
|   8 [======●=============================] 64 |
|                                               |
|   [✓] Include Letters (a-z A-Z)               |
|   [✓] Include Numbers (0-9)                   |
|   [✓] Include Symbols (!@#$%)                 |
|                                               |
|   +---------------------------------------+   |
|   |          🔐 Generate Password         |   |
|   +---------------------------------------+   |
|   |          📋 Copy to Clipboard         |   |
|   +---------------------------------------+   |
|                                               |
|   +---------------------------------------+   |
|   | 🔐 Generated Password:                |   |
|   | k9#Fq8$Lm2!xP5@z                      |   |
|   +---------------------------------------+   |
|                                               |
|  ⚠️ NEVER share passwords publicly            |
+-----------------------------------------------+
```

---

## 📋 Prerequisites

- **Python 3.8 or higher** installed on your machine.
- **Tkinter** (included by default in standard Python installers for Windows and macOS).

> **Note for Linux (Ubuntu/Debian) users:**  
> If Tkinter is not pre-installed on your distribution, install it using:
> ```bash
> sudo apt update
> sudo apt install python3-tk
> ```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/password-generator.git
cd password-generator
```

### 2. Run the Application

No `pip install` or virtual environment activation required! Simply run:

```bash
python main.py
```

---

## 🏗️ Project Architecture

The project follows a clean **Object-Oriented Programming (OOP)** design pattern:

```text
password-generator/
│
├── .gitignore          # Excludes virtual environments, caches & IDE files
├── README.md           # Project documentation and guide
└── main.py             # Main application source code
```

### Key Components in `main.py`

| Class / Function | Responsibility |
| :--- | :--- |
| **`PasswordGeneratorGUI`** | Manages the Tkinter root window, layout configuration, widget event listeners, and user feedback. |
| **`_create_widgets()`** | Builds the title bar, status display, length slider, checkboxes, buttons, and scrollable output area. |
| **`_generate_password()`** | Validates user preferences, builds the dynamic character pool, and generates a random password. |
| **`_copy_password()`** | Interfaces with the OS clipboard and displays a confirmation message box. |
| **`LearningInfo`** | Educational dictionary documenting Tkinter widgets and Python standard library concepts used in the code. |
| **`main()`** | Application entry point that initializes and launches the GUI event loop (`mainloop()`). |

---

## 💡 How to Use

1. **Adjust Password Length**: Drag the horizontal slider to select your desired character length (between 8 and 64).
2. **Select Character Types**: Check or uncheck Letters, Numbers, and Symbols according to your password requirements.
3. **Generate**: Click the **🔐 Generate Password** button. The new password will appear in the output box.
4. **Copy**: Click **📋 Copy to Clipboard** to copy the password directly to your clipboard, ready to paste into your password manager.

---

## 🛡️ Password Security Tips

- 🔑 **Use Long Passwords**: Aim for at least 16 characters for critical accounts (e.g., email, banking, cloud storage).
- 🚫 **Never Reuse Passwords**: A data breach on one website should never compromise your other accounts.
- 🗄️ **Use a Password Manager**: Store your generated passwords in a reputable password manager such as [Bitwarden](https://bitwarden.com/), [1Password](https://1password.com/), or [KeePass](https://keepass.info/).
- 📱 **Enable 2FA**: Always turn on Two-Factor Authentication (2FA) wherever available for an extra layer of defense.

---

## 🗺️ Roadmap & Ideas

Future enhancements and portfolio extensions:
- [ ] 🚥 **Password Strength Meter**: Real-time entropy score and strength indicator (Weak / Medium / Strong).
- [ ] 🌙 **Dark Mode / Theme Switcher**: Modern flat dark UI styling.
- [ ] 🚫 **Exclude Ambiguous Characters**: Option to exclude confusing characters like `0`, `O`, `l`, `1`, `I`.
- [ ] 💾 **Export / History Log**: Optional encrypted session history export.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to fork the repository and submit a Pull Request:

1. Fork the project (`git checkout -b feature/AmazingFeature`)
2. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
3. Push to the branch (`git push origin feature/AmazingFeature`)
4. Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.
