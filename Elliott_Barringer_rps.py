# This file was created by Elliott Barringer

# import all needed functions
from random import randint
import turtle
from turtle import *
import os

# designate the possible choices in the rock paper scissors game and the corresponding win conditions. Compact the two lists into a dictionary that associates each instance with its counterpart
rps_choice = ["rock", "paper", "scissors"]
corres_val = [rps_choice[2], rps_choice[0], rps_choice[1]]
win_vals_dict = dict(zip(rps_choice, corres_val))

player_img = turtle.Turtle()
CPU_img = turtle.Turtle()

# dictionary that allows inputs of 'r' or 's' to be interpreted as rock and scissors, respectively
translate_dict = {
    "r": "rock",
    "p": "paper",
    "s": "scissors"
}

# dictionary that keeps track of the number of times that the player chooses an option
P_choice_count = {
    "rock": 0,
    "paper": 0,
    "scissors": 0
}

# dictionary that keeps track of the number of times that the computer chooses an option
CPU_choice_count = {
    "rock": 0,
    "paper": 0,
    "scissors": 0
}

rock_w = 256
rock_h = 280
paper_w = 256
paper_h = 204
scissors_w = 256
scissors_h = 170

# define a function that updates the counts of each dictionary
def update_choice_count(a, dict):

    dict[a] += 1

    return dict

# define a function that intakes a choice 'r' or 's' or 'p' and returns 'rock' or 'scissors' or 'paper'
def translate(a):

    return translate_dict[a]

# function to check whether an integer a is greater than an integer b. takes value True if a > b, takes value False otherwise
def greater(a, b):
    checker = a > b
    if checker:

        return True
    
    else:

        return False

# define a function to check wheher or not a value 'a' corresponds to a win condition 'b'. in other words, checks whether or not the player's input beats the computers'
def round_eval(a, b):

    if win_vals_dict[a] == b:

        return True
    
    else:

        return False

# define a function that returns the percentage of games won by the player. calculates total rounds and returns the win percentage
def win_loss_ratio(a, b):

    total_rounds = a + b
    win_percentage = (a / total_rounds) * 100

    return str(win_percentage)


image_dict = {
    "rock": 'rock.gif',
    "paper": 'paper.gif',
    "scissors": 'scissors.gif'
}

WIDTH, HEIGHT = 1000, 400

game_folder = os.path.dirname(__file__)
images_folder = game_folder

screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
screen.screensize(canvwidth = WIDTH, canvheight = HEIGHT, bg="gray")

class CreateImage:

    def __init__(image_chosen, x = 0, y = 0):

        image = image_dict[image_chosen]
        image_f = os.path.join(images_folder, image)
        
        image_instance = turtle.Turtle()

        image_instance.penup()
        image_instance.setpos(x, y)

        screen.addshape(image_f)
        image_instance.shape(image_f)
    
    def get_pos(image_chosen):

        pass
    

def display_image_p(choice, pos_x, pos_y, screen_clear):

    image_chosen_p = image_dict[choice]

    image_p = os.path.join(images_folder, image_chosen_p)
    image_instance_p = turtle.Turtle()

    image_instance_p.penup()
    image_instance_p.setpos(pos_x, pos_y)

    screen.addshape(image_p)
    image_instance_p.shape(image_p)

    confirmer = "yes"
    if screen_clear == confirmer:
        
        screen.clear()
    else:
        pass

#def display_image_CPU(choice, pos_x, pos_y, screen_clear):



def display_text(string, pos_x, pos_y, screen_clear):

    text = turtle.Turtle()

    text.hideturtle()
    text.penup()
    text.goto(pos_x, pos_y)
    text.write(string, align="center", font=("Times New Roman", 16, "normal"))

    confirmer = "yes"
    if screen_clear == confirmer:
        
        screen.clear()
    else:
        pass


def moveon():

    move = screen.textinput("Move on?", "Would you like to move on? Type 'yes' to continue, or type 'end' to end the game.")
    
    if move == "yes":
        return True
    else:
        return False

def check_click(x, y, obj_x, obj_y, w, h):

    if x < obj_x + w/2 and x > obj_x -  w/2 and y < obj_y + h/2 and y > obj_y - h/2:

        return True
    
    else:

        return False

def abc(x, y):

    if check_click(x, y, -300, 0, rock_w, rock_h):

        return "rock"
    
    elif check_click(x, y, 0, 0, paper_w, paper_h):

        return "paper"

    elif check_click(x, y, 300, 0, scissors_w, scissors_h):

        return "scissors"
    

'''
function that the game is played through. Intakes value 'num_rounds' 
and uses while loop to iterate through the game as the number of rounds
left is greater than 0
'''
def rps_game(x, y):
    global rounds

    abc(x, y)

    player_score = 0
    CPU_score = 0

    while rounds > 0:
        
        # intake the players choice and translate it from 'r' to 'rock' so that the computer can process it. Designate computer choice as a random value from rps_choices

        #player_choice = screen.textinput("Choice", "Enter your choice. Type 'r' for rock, 'p' for paper, and 's' for scissors.")
        #player = translate(player_choice)
        computer = rps_choice[randint(0, 2)]

        player = abc(x, y)
        print(player)

        display_image_p(player, 250, 0, "no")
        display_image_p(computer, -250, 0, "no")
        display_text("The player has chosen " + player, 250, 100, "no")
        display_text("The computer has chosen " + computer, -250, 100, "no")
        

        
        # checks to see whether or not the round was a draw
        if player == computer:

            screen.clear()
            display_image_p(player, 0, 0, "no")
            display_text("The round was a draw. The computer and the player both chose " + player, 0, 100, "no")

        # uses round_eval function to check whether or not the player's input is mapped to the computer's value as a winning relationship. player's score is increased by one if so
        elif round_eval(player, computer):

            display_text("The player has won!", 0, 100, "no")
            player_score += 1
            rounds -= 1
        
        # instance in which the computer beats the player. The computer's score is increased by one
        else: 

            display_text("The computer has won!", 0, 100, "no")
            CPU_score +=1
            rounds -= 1

        # use update_choice_count function to keep track of how many times the player and the computer are choosing things. intakes the first value as the index, and the second as the dictionary
        update_choice_count(player, P_choice_count)
        update_choice_count(computer, CPU_choice_count)

        cont = moveon()
        
        if cont:
            
            screen.clear()

        elif not cont:

            screen.clear()
            rounds = 0
            

    # instance at which there are no more rounds to play
    if rounds == 0:
        
        # uses greater function to evaluate whether or not the player's score was greater than the computer's score
        if greater(player_score, CPU_score):
            
            display_text("The player had a higher score than the computer!", 0, 0, "no")
        
        else:

            display_text("The computer had a higher score than the player had!", 0, 0, "no")
        
        # instance in which user is prompted on whether or not to show statistics before ending the game
        stats = screen.textinput("View Statistics?", "Type 'yes' if you would like to view the game statistics or type 'exit' to exit the game.")
        if stats == "yes":

            screen.reset()

            
            #block of code that displays various stats about the rounds. first, block displays the win percentage
            #utilizing the win_loss_ration function, and then displays the most common choice of the player
            #and the computer based on the P_choice_count and CPU_choice_count dictionaries
            
            display_text("You won " + win_loss_ratio(player_score, CPU_score) + " percent of the rounds.", 0, 200, "no")
            P_most_common_choice = str(max(P_choice_count, key=P_choice_count.get))
            display_text("Your most common choice was " + P_most_common_choice, 0, 0, "no")
            CPU_most_common_choice = str(max(CPU_choice_count, key=CPU_choice_count.get))
            display_text("The computer's most common choice was " + CPU_most_common_choice, 0, -200, "no")
            turtle.done()

        # ends the program if the user types exit
        elif stats == "exit":
            quit()

# prompts the user to enter a number of rounds to play, utilizes the input as the number of rounds for the rps_game function
rounds = int(screen.textinput("Rounds", "How many rounds would you like to play?"))

display_image("rock", -300, 0, "no")
display_image("paper", 0, 0, "no")
display_image("scissors", 300, 0, "no")

screen.onclick(rps_game)
screen.mainloop()



RPS_choices = ["rock", "paper", "scissors"]

computer = RPS_choices[randint(0, 2)]