import tkinter as tk
from tkinter import messagebox, ttk
import string

class VigenereCipherGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Vigenère Cipher")
        
        self.mode = tk.StringVar(value="Encrypt")
        
        self.create_widgets()

    def create_widgets(self):
        # Create Frame for Text Entry
        text_frame = ttk.Frame(self.root)
        text_frame.pack(pady=10)

        # Text Entry
        ttk.Label(text_frame, text="Text:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.text_entry = ttk.Entry(text_frame, width=50)
        self.text_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create Frame for Key Entry
        key_frame = ttk.Frame(self.root)
        key_frame.pack(pady=10)

        # Key Entry
        ttk.Label(key_frame, text="Key:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.key_entry = ttk.Entry(key_frame, width=50)
        self.key_entry.grid(row=0, column=1, padx=5, pady=5)

        # Create Frame for Result Display
        result_frame = ttk.Frame(self.root)
        result_frame.pack(pady=10)

        # Result Display
        ttk.Label(result_frame, text="Result:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.result_text = tk.Text(result_frame, width=50, height=6)
        self.result_text.grid(row=1, column=0, padx=5, pady=5)

        # Mode Selection
        ttk.Label(self.root, text="Mode:").pack()
        mode_frame = ttk.Frame(self.root)
        mode_frame.pack(pady=5)
        ttk.Radiobutton(mode_frame, text="Encrypt", variable=self.mode, value="Encrypt").grid(row=0, column=0, padx=5, pady=5)
        ttk.Radiobutton(mode_frame, text="Decrypt", variable=self.mode, value="Decrypt").grid(row=0, column=1, padx=5, pady=5)

        # Process Button
        ttk.Button(self.root, text="Process", command=self.process).pack(pady=10)

    def process(self):
        text = self.text_entry.get()
        key = self.key_entry.get()

        if not text or not key:
            messagebox.showerror("Error", "Please enter both text and key.")
            return

        result = self.vigenere_cipher(text, key, self.mode.get())

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)

    def vigenere_cipher(self, text, key, mode):
        mapping = {char: i for i, char in enumerate(string.ascii_lowercase)}
        reverse_mapping = {i: char for i, char in enumerate(string.ascii_lowercase)}
        result = ''

        if mode == "Encrypt":
            for i in range(len(text)):
                if text[i].isalpha():
                    key_char = key[i % len(key)]
                    shift = mapping[key_char]
                    result += reverse_mapping[(mapping[text[i].lower()] + shift) % 26] if text[i].islower() else reverse_mapping[(mapping[text[i].lower()] + shift) % 26].upper()
                else:
                    result += text[i]
        elif mode == "Decrypt":
            for i in range(len(text)):
                if text[i].isalpha():
                    key_char = key[i % len(key)]
                    shift = mapping[key_char]
                    result += reverse_mapping[(mapping[text[i].lower()] - shift) % 26] if text[i].islower() else reverse_mapping[(mapping[text[i].lower()] - shift) % 26].upper()
                else:
                    result += text[i]

        return result


if __name__ == "__main__":
    root = tk.Tk()
    app = VigenereCipherGUI(root)
    root.mainloop()
