import random
import time

greetings = ["hello!", "hi!", "greetings!", "hello", "hi", "greetings"]
goodbyes = ["bye.", "goodbye", "see you!", "later!"]
responses = ["i like singing. do you like something about music?",
             "i'm learning coding. i hope i will succeed. how is your coding?", "would you play Magic the Gathering with me soon?"]
answers = ["fine", "ok", "good", "sure", "yes", "yea", "yes i do"]
names = []
negatives = ["no", "nope", "i don't like"]

subjects = ["music", "game", "magic", "song",
            "singing", "sing", "coding", "code", "python"]

user = input(random.choice(greetings) + "\n").lower()


if (user in greetings):
    new_name = input("who am i speaking to?\n")
    names.append(new_name)
    user = input("welcome " + (new_name) + ", wanna chat?\n").lower()

    answers.append(user)

    while (user != "no"):

        user = input(random.choice(responses)).lower()

        if (user in answers):
            user = input(
                "good to know " + (random.choice(responses)) + "\n").lower()
            answers.append(user)

            if any(word in user for word in subjects):
                user = input("oh! how nice! tell me more about it.\n").lower()

            else:
                user = input(
                    "that's so cool! maybe we can do it together sometime? ").lower()

    if (user == "no"):
        print("allright then." + (random.choice(goodbyes)) + "\n")
        time.sleep(3)
