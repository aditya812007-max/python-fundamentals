from random import choice

import random

import statistics

import sys

import cowsay


try:
       print("hello my name is", sys.argv[1]) #this pritns the thing you typed while trying to run the program in command line, for example 'python day6.py aditya bsiwal' here this is treated as a list and day6.py is at 0th index, aditya is at 1st index and biswal is at 3rd index
except IndexError:
       print("too few arguements")

for arg in sys.argv[1:]:
      print(arg)       

if len(sys.argv) > 2:
      sys.exit("TMI")
elif len(sys.argv) < 2:
      sys.exit("too few given")
else:
     print("hello my name is", sys.argv[1])        

print(statistics.mean([100,90,]))

coin = choice(["heads", "tails"])

number = random.randint(1, 10)

cards = ["jack", "king", "queen"]
random.shuffle(cards)

for card in cards:
    print(card) 

print(coin, number, card)

cowsay.cow("helo kiki")

cowsay.trex("helo kiki")