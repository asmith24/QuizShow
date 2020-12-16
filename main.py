"""" 
Mad Libs 
Core 6 
Alana Smith 
"""

print("Welcome to the Game Show! ")

name = input("What's your name contestant?")

feelings = input("How are you feeling today " + name + "?")

print("\nAwh! Lets get Quizzing!") 
print("Your Category is: ART")

# ART QUESTIONS 


ans = int(input("\nWhat year was the Mona Lisa Painted?"))

if ans == 1503  :
    print ("Correct!")

else :
    print("Nope! Better luck next time.")




anstwo = int(input("\nHow many paintings did Michelangelo make?"))

if anstwo == 182 :
  print("Correct!")

else :
  print("Nope! Better luck next time.")


ansthree = input('Which artist created "a starry night"?')

if ansthree == 'Vincent Van Gogh':
  print("Correct!")

else : print("Nope! Better luck next time.")
