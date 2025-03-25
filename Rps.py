import re
import tkinter as tk 
import random as r
from tkinter import messagebox

class Play:
    def __init__(self,root):
        self.root= root
        self.score=0
        self.c_score=0
        self.root.title("Welcome!")
        self.root.configure(bg="#ACE1E8")
        self.root.geometry("750x600")
        self.create_login()
    
    def create_login(self):
        self.clear_window()
        self.root.geometry("760x400")
        self.l1= tk.Label(self.root, text ="Welcome to Rock, Paper & Scissors!", font=("Georgia", 30, "bold"), fg="white", bg="#4EB1DF")
        self.score=0
        self.c_score=0
        self.l1.place(relx=0.5 ,y=40,anchor= "center")
        
        self.l2=tk.Label(self.root, text="Please enter a nickname to continue:", font=("a", 24), fg="white", bg="#4EB1DF")
        self.l2.place(relx=0.5,y=100,anchor="center")
        
        self.e1=tk.Entry(self.root, font=("Georgia", 20), width=30, bg="#D3E3FC", relief="solid")
        self.e1.place(relx=0.5,y=150,height=40,anchor= "center")
        self.b1= tk.Button(self.root,text="BEGIN!", font=("Arial", 20 , "bold"), bg="#81C784", fg="white", relief="raised", command= self.game_window)
        self.b1.place(relx=0.5,y=220,anchor="center")
   
    def game_window(self):
        #creating the main playing window here
        if hasattr(self, "e1") and self.e1.winfo_exists():
            self.name = self.e1.get().strip()
            if bool(re.search(r"[^a-zA-Z0-9\s]", self.name)) or not self.name:
                messagebox.showerror("Error!", "Please enter a valid name without special characters.")
                self.create_login()
                return
        else:
            pass
        self.clear_window()
        self.root.geometry("700x700")
       
        self.player_choice= tk.StringVar()    
        self.root.title("Rock, Paper, Scissors!")
        self.root.configure(bg="#ACE1E8")
        self.label= tk.Label(self.root, text=f"Let's Play, {self.name}!", font=("Georgia", 28, "bold"),bg="#ACE1E8", fg="black").place(relx=0.5, y=50, anchor="center")

        self.rock_button = tk.Radiobutton(self.root, text="Rock", value="rock", variable=self.player_choice, font=("Times New Roman", 24), bg="#ACE1E8", fg="#204681")
        self.rock_button.place(relx=0.5, y=120, anchor="center")

        self.paper_button = tk.Radiobutton(self.root, text="Paper", value="paper", variable=self.player_choice, font=("Times New Roman", 24), bg="#ACE1E8", fg="#204681")
        self.paper_button.place(relx=0.5, y=180, anchor="center")

        self.scissor_button = tk.Radiobutton(self.root, text="Scissors", value="scissors", variable=self.player_choice, font=("Times New Roman", 24), bg="#ACE1E8", fg="#204681")
        self.scissor_button.place(relx=0.5, y=240, anchor="center")

        self.score_label = tk.Label(self.root, text="Your Score: 0 | Computer Score: 0", font=("Georgia", 24, "bold"), fg="white", bg="#0A74DA")
        self.score_label.place(relx=0.5, y=320, anchor="center")

        self.c_choice = tk.Label(self.root, text="Computer Choice : ?", font=("Georgia", 24), fg="black",bg="#ACE1E8")
        self.c_choice.place(relx=0.5, y=400, anchor="center")

        self.display_label = tk.Label(self.root, font=("Georgia", 24), fg="#FFB300", bg="#ACE1E8")
        self.display_label.place(relx=0.5, y=470, anchor="center")

        self.play_button = tk.Button(self.root, text="PLAY!", font=("Arial", 24, "bold"), bg="#81C784", fg="white", relief="raised", command=lambda: self.rps(self.name))
        self.play_button.place(relx=0.5, y=550, anchor="center")

        self.quit_button = tk.Button(self.root, text="Quit", font=("Arial", 24, "bold"), bg="#E57373", fg="white", relief="raised", command=self.create_login)
        self.quit_button.place(relx=0.5, y=620, anchor="center")
    
    def rps(self,n):
        player_choice= self.player_choice.get()
        valid_options=["rock","paper","scissors"]
        computer_choice= r.choice(valid_options)
        self.c_choice.config(text=f"Computer's Choice: {computer_choice}")
        
        if computer_choice == player_choice:
            self.display_label.configure(text=f"It's a tie! Try again!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            self.display_label.config(text="You win this round!")
            self.score += 1
        else:
            self.display_label.config(text=f"Computer Wins! Continue playing")
            self.c_score += 1
        
        self.score_label.config(text=f"Your Score: {self.score} | Computer Score: {self.c_score}")
        
        if self.score == 3:
            self.display_label.config(text=f"Congratulations {n}!\nYou won the game!")
            self.play_button.destroy()
            self.reset_button= tk.Button(self.root, text="Play Again?", font=("Arial", 24, "bold"), bg="#81C784", fg="white", command= self.reset_game)
            self.reset_button.place(relx=0.5, y=550, anchor="center")
        elif self.c_score == 3:
            self.display_label.config(text="Game Over!\nComputer won the game! Try again:(")
            self.play_button.destroy()
            self.reset_button= tk.Button(self.root, text="Play Again?", font=("Arial", 24, "bold"), bg="#81C784", fg="white", command= self.reset_game)
            self.reset_button.place(relx=0.5, y=550, anchor="center")
        else:
            pass
    
    def reset_game(self):
        self.score = 0
        self.c_score = 0
        self.game_window()
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
root= tk.Tk()
root.geometry("400x400")
Play(root)
root.mainloop()
