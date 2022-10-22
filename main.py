# 🚨 user input👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#changing to lower function to be able to count all char
name_1 = name1.lower()
name_2 = name2.lower()
# Counting word "True"
t = name_1.count("t")
r = name_1.count("r")
u = name_1.count("u")
e = name_1.count("e")
total1 = 0
total1 = total1 + t + r + u + e

#Counting word  "Love"
l = name_2.count("l")
o = name_2.count("o")
v = name_2.count("v")
e = name_2.count("e")
total2 = 0
total2 = total2 + l + o + v + e

love_score1 = str(total1)
love_score2 = str(total2)
love_score = love_score1 + love_score1

total_love_score = int(love_score)
#Display message
if (total_love_score < 10) or (total_love_score > 90):
  print(f"Your score is {total_love_score} , you go together like coke and mentos ")
elif (total_love_score >= 40) and (total_love_score <= 50):
  print(f"Your score is {total_love_score}, you are alright together.")
else:
  print(f"Your score is {total_love_score} .")
  
