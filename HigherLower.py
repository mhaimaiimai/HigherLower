from art import logo
from game_data import data
import os
import random

def star_selected(exception):
    if exception >= 0:
        allowed_stars = [star for star in data if star != data[exception]]
    else:
        allowed_stars = data
    star = random.randint(0,len(allowed_stars)-1)
    return star

def star_display(star_A, star_B):
    print(f"Compare A: {data[star_A]['name']}, a {data[star_A]['description']}, from {data[star_A]['country']}")
    print(""" 
     _    __    
    | |  / /____
    | | / / ___/
    | |/ (__  ) 
    |___/____(_)""")
    print(f"Against B: {data[star_B]['name']}, a {data[star_B]['description']}, from {data[star_B]['country']}")

def judgment(star_more, star_less, score):
    os.system('clear')
    print(logo)
    if data[star_more]['follower_count'] >= data[star_less]['follower_count']:
        score+=1
        game_end=False
        print(f"You're right! Current score: {score}")
    else:
        game_end=True
        print(f"Sorry, that's wrong. Final score: {score}")
    return score,game_end
########################################################

def main():
    print(logo)
    
    star_A = star_selected(-1)
    score = 0
    game_end = False
    while not game_end:
        #select B
        star_B = star_selected(star_A)
        star_display(star_A, star_B)

        #ask
        guess = ""
        while not (guess in ('A','B')):
            guess = input("Who has more followers? Type 'A' or 'B': ")
        if guess == "A":
            score,game_end = judgment(star_A, star_B, score)
        else:
            score,game_end = judgment(star_B, star_A, score)
        
        star_A = star_B
main()



