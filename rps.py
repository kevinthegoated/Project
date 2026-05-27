import random
import time
win=0
lose=0
tie=0
def rps():
   win=0
   lose=0
   tie=0
   while True:
      print("Welcome to Rock paper siccors")
      choice=input("what will you choose (rock, paper, scissors) ")
      choices=["rock","paper","scissors"]
      Ai=random.choice(choices)
      print(f"You chose {choice}, Ai chose {Ai}")
      time.sleep(2)
      if choice=="rock"and Ai=="paper":
         print("Ai wins")
         lose=lose+1
      if choice=="rock"and Ai=="scissors":
         print("You win")
         win=win+1
      if choice=="rock"and Ai=="rock":
         print("tie")
         tie=tie+1
      if choice=="scissors"and Ai=="rock":
         print("Ai wins")
         lose=lose+1
      if choice=="scissors"and Ai=="scissors":
         print("tie")
         tie=tie+1
      if choice=="scissors"and Ai=="paper":
         print("you win")
         win=win+1
      if choice=="paper"and Ai=="rock":
         print("you win")
         win=win+1
      if choice=="paper"and Ai=="scissors":
         print("Ai win")
         lose=lose+1
      if choice=="paper"and Ai=="paper":
         print("tie")
         tie=tie+1
      print(f"You have {tie} tie, {win} win, {lose} lose")

rps()


