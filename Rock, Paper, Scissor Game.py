from tkinter import *
from PIL import Image
from PIL import ImageTk
from random import randint

#main window
root = Tk()
root.title("Rock Paper Scissor")
root.configure(background="#e4ebdd")

#picture
rock_img_user = ImageTk.PhotoImage(Image.open("rock_user.png"))
paper_img_user = ImageTk.PhotoImage(Image.open("paper_user.png"))
scissor_img_user = ImageTk.PhotoImage(Image.open("scissor_user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock_comp.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper_comp.png"))
scissor_img_comp = ImageTk.PhotoImage(Image.open("scissor_comp.png"))

#insert picture
user_label = Label(root,image=scissor_img_user,bg="#e4ebdd")
comp_label = Label(root,image=scissor_img_comp,bg="#e4ebdd")
comp_label.grid(row=1,column=4)
user_label.grid(row=1,column=0)

#scores
playerScore = Label(root,text=0,font=("fixedsys", 100, "bold"),bg="#e4ebdd",fg="#043927")
computerScore = Label(root,text=0,font=("fixedsys", 100, "bold"),bg="#e4ebdd",fg="#043927")
computerScore.grid(row=1,column=3)
playerScore.grid(row=1,column=1)

#indicators
user_indicator = Label(root,font=("fixedsys", 25, "bold"),text="PLAYER",bg="#e4ebdd",fg="#1a2421").grid(row=0,column=1)
comp_indicator = Label(root,font=("fixedsys", 25, "bold"),text="COMPUTER",bg="#e4ebdd",fg="#1a2421").grid(row=0,column=3)

#messages
msg = Label(root,font=("Arial", 15, "bold"),bg="#e4ebdd",fg="Green")
msg.grid(row=3,column=2)

#update message
def updateMessage(x):
    msg['text'] = x


#update user score
def updateUserScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

#update computer score
def updateCompScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

#check winner
def checkWin(player,computer):
    if player == computer:
        updateMessage("It's a Tie!")
    elif player == "rock":
        if computer == "paper":
            updateMessage("You Lose :(")
            updateCompScore()
        else:
            updateMessage ("You Win :D")
            updateUserScore()
    elif player == "paper":
        if computer == "scissor":
            updateMessage("You Lose! :(")
            updateCompScore()
        else:
            updateMessage ("You Win! :D")
            updateUserScore()            
    elif player == "scissor":
        if computer == "rock":
            updateMessage("You Lose! :(")
            updateCompScore()
        else:
            updateMessage ("You Win! :D")
            updateUserScore()

    else:
        pass

#update choices
choices = ["rock","paper","scissor"]

def updateChoice(x):

#for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    elif compChoice == "paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)


#for user 
    if x=="rock":
        user_label.configure(image=rock_img_user)
    elif x=="paper":
        user_label.configure(image=paper_img_user)
    else:
        user_label.configure(image=scissor_img_user)
    
    checkWin(x,compChoice)

#buttons
rock = Button(root, width=30,height=2,text="ROCK", 
              bg="#123524",fg="white",command = lambda:updateChoice("rock")).grid(row=2,column=1)
paper = Button(root,width=30,height=2,text="PAPER",
              bg="#123524",fg="white",command = lambda:updateChoice("paper")).grid(row=2,column=2)
scissor = Button(root,width=30,height=2,text="SCISSOR",
              bg="#123524",fg="white",command = lambda:updateChoice("scissor")).grid(row=2,column=3)


root.mainloop()