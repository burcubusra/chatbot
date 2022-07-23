greetings = ["hello!", "hi!", "greetings!" , "hello" , "hi" , "greetings" ]
goodbyes = ["bye." , "goodbye" , "see you!" , "later!"]
responses = ["i like singing. do you like something about music?" , "i'm learning coding. i hope i will succeed. how is your coding?" , "would you play Magic the Gathering with me soon?"]
answers = [ "fine", "ok" , "good" , "sure" , "yes" , "yea" , "yes i do"]
negatives = ["no" , "nope" , "i don't like" ]
 
subjects = {"music" , "game" , "magic" , "song" , "singing" , "sing" , "coding" , "code" , "python"}
import random

user = input(random.choice (greetings))
user = user.lower()

while (user != "no"):

   if (user in (greetings)):
      new_answer = input ("who am i speaking to?")
      answers.append(new_answer)
      new_answer2 = input ("welcome " + (new_answer) + " wanna chat?")
      answers.append (new_answer2)
      user = input(random.choice (responses))
      user = user.lower() 
      if (user in (answers)):
        new_answer3 = input ("good to know " + (random.choice (responses)))
        answers.append(new_answer3)

        if (user in (subjects)):
            new_subject = input ("oh! how nice! tell me more about it.")
            subjects.append(new_subject)

        else :
          input("that's so cool! maybe we can do it together sometime")

