import random

greetings = ["hello!", "hi!", "greetings!", "hello", "hi", "greetings"]
goodbyes = ["bye.", "goodbye", "see you!", "later!"]
responses = ["i like singing. do you like something about music?",
             "i'm learning coding. i hope i will succeed. how is your coding?", "would you play Magic the Gathering with me soon?"]
answers = ["fine", "ok", "good", "sure", "yes", "yea", "yes i do"]
names = []
negatives = ["no", "nope", "i don't like"]

subjects = [
    "music", "game", "magic", "song",
    "singing", "sing", "coding", "code", "python"
]

user = input(random.choice(greetings) + "\n")
user = user.lower()

while (user != "no"):
    print("loop starts here")

    if (user in greetings):
        new_name = input("who am i speaking to?\n")
        names.append(new_name)
        new_answer = input("welcome " + (new_name) + ", wanna chat?\n")
        answers.append(new_answer)
        user = input(random.choice(responses))
        user = user.lower()
        if (user in answers):
            new_answer = input(
                "good to know " + (random.choice(responses)) + "\n")
            answers.append(new_answer)

            found_subject = False
            for sub in subjects:
                if sub in new_answer:
                    found_subject = True

            if(found_subject):
                new_subject = input(
                    "oh! how nice! tell me more about it.\n")
                subjects.append(new_subject)
            else:
                input("that's so cool! maybe we can do it together sometime? ")
