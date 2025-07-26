import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime

# Headline data
subjects = ["A cat", "The scientist", "A musician"]
actions = ["jumps over", "sings to", "cooks for", "dances with", "explains to"]
places = ["the park", "the lab", "the concert hall", "the beach"]
templates = [
    "Breaking News: {} {} at {}!",
    "Shocking Update: {} {} in {}!",
    "Just In: {} {} near {}!",
    "Live Now: {} {} around {}!"
]

# Generate headline
def generate_headline():
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    template = random.choice(templates)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    headline = f"[{timestamp}] {template.format(subject, action, place)}"
    headline_label.config(text=headline)

# Save headline to file
def save_headline():
    headline = headline_label.cget("text")
    if headline:
        with open("headlines.txt", "a") as file:
            file.write(headline + "\n")
        messagebox.showinfo("Saved", "Headline saved to headlines.txt")
    else:
        messagebox.showwarning("Empty", "Generate a headline first!")

# Exit
def exit_app():
    root.destroy()

# Setup GUI
root = tk.Tk()
root.title("Fake News Headline Generator")
root.geometry("500x300")
root.configure(bg="#f2f2f2")

title = tk.Label(root, text="📰 Fake News Headline Generator", font=("Helvetica", 16, "bold"), bg="#f2f2f2")
title.pack(pady=10)

headline_label = tk.Label(root, text="Click 'Generate' to create a headline", wraplength=450, font=("Arial", 12), bg="#f2f2f2")
headline_label.pack(pady=20)

generate_btn = tk.Button(root, text="Generate Headline", command=generate_headline, width=20, bg="#4CAF50", fg="white")
generate_btn.pack(pady=5)

save_btn = tk.Button(root, text="Save to File", command=save_headline, width=20, bg="#2196F3", fg="white")
save_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", command=exit_app, width=20, bg="#f44336", fg="white")
exit_btn.pack(pady=20)

root.mainloop()
