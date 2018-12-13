from tkinter import *
root = Tk()
root.title('Rock, Paper and Scissors game')
root.geometry('350x350+250+300')
uu_choice = StringVar()
Entry(textvariable= uu_choice).pack()
def hello():
  u_choice = uu_choice.get().capitalize()
  import random
  choices = ["Rock", "Paper", "Scissors"]
  comp_choice = random.choice(choices)
  lost = "Computer's choice is " + comp_choice + ". You Lost!"
  won = "Computer's choice is " + comp_choice + ".  You Won!"
  draw = "Computer's choice is "+ comp_choice + ". It is a draw!"
  if  u_choice == comp_choice:
    Label(text=draw).pack()
  elif u_choice == "Rock"  and comp_choice == "Paper":
    Label(text=lost).pack()
  elif u_choice == "Rock"  and comp_choice == "Scissors":
    Label(text=won).pack()
  elif u_choice == "Paper"  and comp_choice == "Scissors":
    Label(text=lost).pack()
  elif u_choice == "Paper"  and comp_choice == "Rock":
    Label(text=won).pack()
  elif u_choice == "Scissors" and comp_choice == "Rock":
    Label(text=lost).pack()
  elif u_choice == "Scissors" and comp_choice == "Paper":
    Label(text=won).pack()
  else:
    Label(text="Please choose Rock, Paper or Scissors!").pack()
Button(text='Submit', command = hello).pack()
root.mainloop()
