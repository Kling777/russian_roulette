from time import sleep
import random

"""
this program is a russian roulette game inspired of buckshot roulette and squid game s2
that i made with a little bit story going on and run on terminal
"""

def typing_effect(text="", delay=0.05):
    """
    A function to print out a string with a typing effect.

    Args:
        text (str): The string to be printed out.
        delay (float): The delay between each character being printed out.
    """
    for letter in text:
        print(letter, end="", flush=True)
        sleep(delay)
    print()

# todo finish story
def game_intro():
    player_naming_tries = 0

    typing_effect("welcome to russian roulette, a game where you play with your own luck~")
    sleep(2)
    # Todo continue this
    typing_effect("for today game we got two gentlemen ")
    sleep(2)
    typing_effect("where you two gonna compete for the prize of tomorrow still waking up peacefully")
    sleep(2)
    typing_effect("\nalright ennnough chit chat, let introduce our players~")

    typing_effect("what is your name kind sir?")
    player_name = input("->")

    while (player_name == ""):
        player_naming_tries += 1

        if (player_naming_tries == 1):
            typing_effect("sir, what is your name?")
            player_name = input("->")
        elif (player_naming_tries == 2):
            typing_effect("sir, please cooperate with us. What is your name?")
            player_name = input("->")
        elif (player_naming_tries == 3):
            typing_effect("please don't let the audience waiting....")
            player_name = input("->")
        elif (player_naming_tries == 4):
            typing_effect("sir, i advice you to cooperate with us. This is for your own good")
            player_name = input("->")
        else:
            typing_effect("\n*sigh*")
            sleep(3)
            typing_effect("alrright sir thankyou for participating in today game")
            typing_effect("i wish you have a grreat day with your little time left~~")
            break

    return player_name

def story_visibility_choice():
    user_story_choice = input("show story? [y/n]\n-> ")

    while user_story_choice == "":
        user_story_choice = input("show story? [y/n]\n-> ")

    if user_story_choice == "y" or user_story_choice == "Y":
        return True
    else:
        return False

def get_random_cpu_name():
    cpu_names = open("cpu_names.txt", "r")
    cpu_names_list = []
    for cpu_name in cpu_names:
        cpu_name = cpu_name.strip()
        if cpu_name != "":
            cpu_names_list.append(cpu_name)
    cpu_names.close()

    return (random.choice(cpu_names_list))

def main():
    story_visibility = story_visibility_choice()
    print()

    if story_visibility:
        player_name = game_intro()
    else:
        player_name = input("Input player name: ")

        while player_name == "":
            player_name = input("Input player name: ")

    #  todo made the game here
    if player_name:
        cpu_name = get_random_cpu_name()
        print(cpu_name)


if __name__ == '__main__':
    main()
