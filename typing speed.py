import tkinter as tk
from tkinter import messagebox
import time
import random

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        
        # Initialize variables
        self.start_time = None
        self.end_time = None
        self.typing_speed = 0
        self.accuracy = 0
        self.passage = self.generate_passage()
        
        # Create and place widgets
        self.create_widgets()
        self.reset_test()

    def create_widgets(self):
        self.passage_label = tk.Label(self.root, text="Passage:")
        self.passage_label.pack(pady=5)
        
        self.passage_text = tk.Label(self.root, text="", wraplength=500)
        self.passage_text.pack(pady=5)
        
        self.entry_label = tk.Label(self.root, text="Type the passage below:")
        self.entry_label.pack(pady=5)
        
        self.typing_entry = tk.Entry(self.root, width=80)
        self.typing_entry.pack(pady=5)
        self.typing_entry.bind("<KeyRelease>", self.on_key_release)
        
        self.start_button = tk.Button(self.root, text="Start Test", command=self.start_test)
        self.start_button.pack(pady=5)
        
        self.stop_button = tk.Button(self.root, text="Stop Test", command=self.stop_test, state=tk.DISABLED)
        self.stop_button.pack(pady=5)
        
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)

    def generate_passage(self):
        # Generates a random passage for typing
        words = ["quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog", "lorem", "ipsum", "dolor", "sit", "amet"]
        passage = ' '.join(random.choices(words, k=50))
        return passage

    def reset_test(self):
        self.passage = self.generate_passage()
        self.passage_text.config(text=self.passage)
        self.typing_entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.end_time = None
        self.typing_speed = 0
        self.accuracy = 0

    def start_test(self):
        self.reset_test()
        self.start_time = time.time()
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

    def stop_test(self):
        if self.start_time is None:
            messagebox.showwarning("Warning", "Test has not been started.")
            return
        
        self.end_time = time.time()
        elapsed_time = (self.end_time - self.start_time) / 60  # Time in minutes
        typed_text = self.typing_entry.get()
        
        words_typed = len(typed_text.split())
        self.typing_speed = words_typed / elapsed_time if elapsed_time > 0 else 0

        passage_words = self.passage.split()
        typed_words = typed_text.split()
        correct_words = sum(1 for p, t in zip(passage_words, typed_words) if p == t)
        self.accuracy = (correct_words / len(passage_words)) * 100 if passage_words else 0
        
        result_text = (
            f"Typing Speed: {self.typing_speed:.2f} WPM\n"
            f"Accuracy: {self.accuracy:.2f}%"
        )
        self.result_label.config(text=result_text)
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def on_key_release(self, event):
        # Optional: you can add real-time feedback here if desired
        pass

# Create the main window
root = tk.Tk()
app = TypingSpeedTestApp(root)
root.mainloop()
