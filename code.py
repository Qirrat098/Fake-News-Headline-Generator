import random

subjects = [
    "The cat",
    "A dog",
    "The teacher",
    "A student",
    "The chef",
    "The scientist",
    "A musician",
    "The artist",
    "Auto Rickshaw Driver"
]

actions = [
    "jumps over",
    "runs around", 
    "sings to",
    "paints",
    "teaches",
    "cooks for",
    "plays with",
    "drives to",
    "explains to",
    "dances with",
    "cry with"
]

places = [
    "the park",
    "the school",
    "the kitchen",
    "the stage",
    "the lab",
    "the street",
    "the gallery",
    "the concert hall",
    "the market",
    "the beach"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"Breaking News: {subject} {action} at {place}!" 
    print("\n" + headline)  

    userinput = input("Do you want to generate another headline? (yes/no): ")
    if userinput.lower() == "no":
        print("Thank you for using the Fake News Headline Generator!")
        break
