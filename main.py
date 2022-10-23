# 🚨 user input👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#changing to lower function to be able to count all char
name_1 = name1.lower()
name_2 = name2.lower()
name_conca = name1 + name2

# Counting word "True"
t = name_conca.count("t")
r = name_conca.count("r")
u = name_conca.count("u")
e = name_conca.count("e")

true = t + r + u + e

#Counting word  "Love"
l = name_conca.count("l")
o = name_conca.count("o")
v = name_conca.count("v")
e = name_conca.count("e")

love = l + o + v + e

love_score =  str(true) + str(love)
total_love_score = int(love_score)

#Display message
if (total_love_score < 10) or (total_love_score > 90):
  print(f"Your score is {total_love_score} , you go together like coke and mentos ")
elif (total_love_score >= 40) and (total_love_score <= 50):
  print(f"Your score is {total_love_score}, you are alright together.")
else:
  print(f"Your score is {total_love_score} .")
  
