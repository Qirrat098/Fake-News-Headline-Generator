import random
from datetime import datetime

subjects = ["A cat", "The scientist", "A musician"]
actions = ["jumps over", "sings to", "cooks for", "dances with", "explains to"]
places = ["the park", "the lab", "the concert hall", "the beach"]

templates = [
    "Breaking News: {} {} at {}!",
    "Shocking Update: {} {} in {}!",
    "Just In: {} {} near {}!",
    "Live Now: {} {} around {}!"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    template = random.choice(templates)
    
    headline = f"[{timestamp}] {template.format(subject, action, place)}"
    print("\n" + headline)

    with open("headlines.txt", "a") as file:
        file.write(headline + "\n")

    again = input("Generate another headline? (yes/no): ").strip().lower()
    if again == "no":
        print("Thank you for using the Fake News Headline Generator!")
        break
