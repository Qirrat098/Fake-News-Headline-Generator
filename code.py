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
    "Auto Rickshaw Driver"]

actions= [
    "jumps over",
    "runs around", 
    "sings to",
    "paints",
    "teaches",
    "cooks for",
    "plays with",
    "drives",
    "explains to",
    "dances with"
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
    subjects = randome.choice(subjects)
    actions = random.choice(actions)
    places = random.choice(places)

    headline = f "Breaking News: {subjects} {actions} at {places}!" 
    print("n" + headline)  
