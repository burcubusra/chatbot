from posixpath import split
from pprint import pprint
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
    
if (user in greetings):
        new_name = input("who am i speaking to?\n")
        names.append(new_name)
        new_answer = input("welcome " + (new_name) + ", wanna chat?\n")
        answers.append(new_answer)
        
        while (user != "no"):
            
         user = input(random.choice(responses))
         user = user.lower()
         
         if (user in answers):
            user = new_answer = input(
                "good to know " + (random.choice(responses)) + "\n")
            answers.append(new_answer)
            user = user.lower()
            
            if any(word in new_answer for word in subjects):
               
               user = input("oh! how nice! tell me more about it.\n")
               
              
            else:
              
              user = input("that's so cool! maybe we can do it together sometime? ")
                 
        if (user == "no"):
          
          print ("allright then." + (random.choice(goodbyes)) + "\n")
          import time
          time.sleep(3)
       
         