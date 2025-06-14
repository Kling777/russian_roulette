from time import sleep
import random

"""
this program is a russian roulette game inspired of buckshot roulette and squid game s2
that i made with a little bit story going on and run on terminal
"""

def typing_effect(text="", delay=0.05):
    for letter in text:
        print(letter, end="", flush=True)
        sleep(delay)
    print()

def game_intro(cpu_name):
    player_naming_tries = 0

    typing_effect("you live in slum of a city in the middle of nowhere")
    typing_effect("your everyday life is filled with poverty and roughness on the edge")
    typing_effect("but for you that's not a problem at all, because you surrounded with friends, no, they are family")
    sleep(1)
    print()
    typing_effect("but one day, one by one of them went missing. like they dissappeared out of nowhere")
    sleep(1)
    typing_effect("in curiosity, you decided to investigate")
    sleep(1)
    typing_effect("hours and days has passed but no avail of finding a single clue")
    typing_effect("in effect of tired you rest yourself thinking where could they've gone")
    sleep(1)
    print()
    typing_effect("at past midnight, you woken up by knock on your room door")
    typing_effect("thingking why the landlord be in this hour")
    typing_effect("as you approach the door, you notice a letter sliding below the door")
    sleep(1)
    typing_effect("you picked up and open the door with a sight of no one across the hallway")
    typing_effect("strange you thought")
    typing_effect("you close the door and open the letter")
    typing_effect("to which inside is an invitation")
    typing_effect('that reads "your invited to the game of life and death with the winner will given a prize that can change their life forever"')
    typing_effect("strange you thought again. you think this just a prank so you brush it off and continue to sleep")
    sleep(1)
    print()
    typing_effect("at morning because of curiosity, you try to go to the game by following the letters instructions")
    sleep(1)
    typing_effect("you arrive at a backstreet. but no one was there")
    typing_effect("you think again that this really is a prank")
    typing_effect("but after that something stranggled you from behind")
    typing_effect("you try to fight free but in the end the you fell down to unconcious")
    sleep(2)
    print()

    typing_effect("host: wakey wakey~~")
    sleep(1)
    typing_effect("you wake up")

    typing_effect("host: hehe, welcome to russian roulette, a game where you play with your own luck~")
    typing_effect("host: you sleep real cozy huh")
    typing_effect("you: where am i!! who are you!!")
    typing_effect("host: that question is not irrelevant for now")
    typing_effect("host: cuz after this you will face someone mysterious in a game of russian roulette")
    typing_effect("host: wuuuiiiiii, i am excited and the audience must be excited too")
    typing_effect("you: let me go!! i need to find my friend")
    typing_effect("host: now now, you are here because of your own will and now you want to go?")
    typing_effect("host: c'mon light your spirit up, if you win you will get a big prize you know")
    typing_effect("you: ...")
    typing_effect("host: alright ennnough chit chat, let introduce our players~")

    typing_effect("host: what is your name kind sir?")
    player_name = input("-> ")

    while (player_name == ""):
        player_naming_tries += 1

        if (player_naming_tries == 1):
            typing_effect("host: sir, what is your name?")
            player_name = input("-> ")
        elif (player_naming_tries == 2):
            typing_effect("host: could you cooperate will ya?. What is your name?")
            player_name = input("-> ")
        elif (player_naming_tries == 3):
            typing_effect("host: please don't let the audience waiting....")
            player_name = input("-> ")
        elif (player_naming_tries == 4):
            typing_effect("host: i advice you to cooperate with us. This is for your own good")
            player_name = input("-> ")
        else:
            print()
            typing_effect("host: *sigh*")
            sleep(3)
            typing_effect("host: guys get the new candidate and get this guy outta here!")
            typing_effect("host: i wish you have a grreat day with your life man")
            return ""

    typing_effect(f"host: alright {player_name} for today game you will face our last winner")
    typing_effect(f"host: big applause to our previous winner... {cpu_name}!!!")
    typing_effect("you: !!!")
    typing_effect(f"you: {cpu_name}!!!, where do you have been?!")
    typing_effect("you: i've been looking for you. you and a lot of people have been gone")
    typing_effect(f"{cpu_name}: im sorry {player_name}, all of the people you been searching for is dead, all except me")
    typing_effect(f"you: {cpu_name}! why WHY????")
    typing_effect(f"{cpu_name}: because life is hard {player_name}, you know")
    typing_effect(f"{cpu_name}: and this is the only thing that changed it, that change my life")
    typing_effect(f"{cpu_name}: and im sorry... i can't lose it now, im gonna win")
    typing_effect("you: oh no your not")
    typing_effect("host: uuuuuuuuuuui, what a warm encounter, buttt that's gonna be over soon")
    typing_effect("host: cuz both of you gonna facing each other for the prize offffff millions!!!")
    typing_effect("host: that's soooo sad friend versus friend")
    typing_effect("host: but that's enough, let us start the game!!")

    return player_name

def story_visibility_choice():
    user_story_choice = input("show story? [y/n]\n-> ")

    while (user_story_choice == "" or user_story_choice != "y" and user_story_choice != "Y" and user_story_choice != "n" and user_story_choice != "N"):
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

def get_randomize_chamber():
    chambers = open("chambers.txt", "r")
    chambers_list = []
    for chamber in chambers:
        chamber = chamber.strip()
        if chamber != "":
            chambers_list.append(chamber)
    chambers.close()

    chamber = random.choice(chambers_list)
    chamber_array = []

    for bullet in chamber:
        if bullet == "1":
            chamber_array.append(1)
        else:
            chamber_array.append(0)

    random.shuffle(chamber_array)

    return chamber_array

def get_active_bullet_amount(chamber):
    active_bullet = 0

    for bullet in chamber:
        if bullet == 1:
            active_bullet += 1

    return active_bullet

def get_player_name():
    player_name = input("Input player name: ")

    while player_name == "":
        player_name = input("Input player name: ")

    return player_name

def main():
    # input for user, if user wants to see the story or not
    cpu_name = get_random_cpu_name()
    story_visibility = story_visibility_choice()
    print() # for spacing

    # checking if user wants to see the story
    # if user wants to see the story, it will run the game_intro function
    if story_visibility:
        player_name = game_intro(cpu_name)
    else:
        player_name = get_player_name()

    # the game will only run if player name is not empty
    if player_name:
        # spacing
        print()

        # assigning cpu name and printing player and cpu name
        if story_visibility:
            typing_effect(f"host: our defending winner {cpu_name} versus our new challenger {player_name}")
            typing_effect("let's goooooo")
            sleep(2)
        else:
            print()
            print(f"{player_name} vs {cpu_name}")
        print()

        # assigning variables
        player_health, cpu_health = 100, 100
        last_chamber = []

        # game loop, the game will run until player or cpu health is 0
        while player_health > 0 and cpu_health > 0:
                # assigning variables
                turn = "player"
                chamber = get_randomize_chamber()

                # checking if the chamber is the same as the last chamber, if yes then get a new one
                while len(chamber) == len(last_chamber):
                    chamber = get_randomize_chamber()

                active_bullet = get_active_bullet_amount(chamber)
                blank_bullet = len(chamber) - active_bullet

                typing_effect("preparing chamber...", delay=0.03)
                sleep(1)
                print("========================================================")
                print(f"{active_bullet} active bullets, {blank_bullet} blank bullets")
                print("========================================================")
                sleep(2)
                typing_effect("the bullets goes into the chamber in hidden sequence", delay=0.05)
                sleep(2)

                print()
                print()

                # loop for each bullet
                for i in range(len(chamber)):
                    # checking if player or cpu health is 0 while there still some bullet left
                    if player_health > 0 and cpu_health > 0:
                    # player turn
                        if turn == "player":
                            typing_effect(f"***{player_name} turn***", delay=0.02)
                            sleep(1)

                            print(f"you have {player_health} health, {cpu_name} have {cpu_health} health")
                            print("shooting yourself with a blank will skip the opponent turn")
                            print("what's your action?")
                            print("1. shoot self")
                            print(f"2. shoot {cpu_name}")

                            # input for user action
                            player_action = input("-> ")

                            # checking if user input is valid
                            while player_action != "1" and player_action != "2":
                                player_action = input("-> ")

                            # all possible outcomes
                            if player_action == "1" and chamber[i] == 1:
                                typing_effect("you shot yourself", delay=0.05)
                                sleep(1)
                                print("BOOM!!!!!")
                                sleep(1)
                                typing_effect("it was a live bullet", delay=0.05)
                                sleep(1)
                                health_loss = random.randint(10, 25)
                                player_health -= health_loss
                                print(f"you lost {health_loss} health")
                                print()
                                turn = cpu_name
                                sleep(2)
                            elif player_action == "1" and chamber[i] == 0:
                                typing_effect("you shot yourself", delay=0.05)
                                sleep(1)
                                print("Click!!")
                                sleep(1)
                                typing_effect("it was a blank bullet", delay=0.05)
                                print()
                                turn = "player"
                                sleep(2)
                            elif player_action == "2" and chamber[i] == 1:
                                typing_effect(f"you shot {cpu_name}", delay=0.05)
                                sleep(1)
                                print("BOOM!!!!!")
                                sleep(1)
                                typing_effect("it was a live bullet", delay=0.05)
                                sleep(1)
                                health_loss = random.randint(10, 25)
                                cpu_health -= health_loss
                                print(f"{cpu_name} lost {health_loss} health")
                                print()
                                turn = cpu_name
                                sleep(2)
                            elif player_action == "2" and chamber[i] == 0:
                                typing_effect(f"you shot {cpu_name}", delay=0.05)
                                sleep(1)
                                print("Click!!")
                                sleep(1)
                                typing_effect("it was a blank bullet", delay=0.05)
                                print()
                                turn = cpu_name
                                sleep(2)
                        else:
                            # cpu turn
                            typing_effect(f"***{cpu_name} turn***", delay=0.02)
                            sleep(1)
                            cpu_action = random.choice(["1", "2"])

                            # all possible outcomes
                            if cpu_action == "1" and chamber[i] == 1:
                                typing_effect(f"{cpu_name} shot himself", delay=0.05)
                                sleep(1)
                                print("BOOM!!!!!")
                                sleep(1)
                                typing_effect("it was a live bullet", delay=0.05)
                                sleep(1)
                                health_loss = random.randint(10, 25)
                                cpu_health -= health_loss
                                print(f"{cpu_name} lost {health_loss} health")
                                print()
                                turn = "player"
                                sleep(2)
                            elif cpu_action == "1" and chamber[i] == 0:
                                typing_effect(f"{cpu_name} shot himself", delay=0.05)
                                sleep(1)
                                print("Click!!")
                                sleep(1)
                                typing_effect("it was a blank bullet", delay=0.05)
                                print()
                                turn = cpu_name
                                sleep(2)
                            elif cpu_action == "2" and chamber[i] == 1:
                                typing_effect(f"{cpu_name} shot you", delay=0.05)
                                sleep(1)
                                print("BOOM!!!!!")
                                sleep(1)
                                typing_effect("it was a live bullet", delay=0.05)
                                sleep(1)
                                health_loss = random.randint(10, 25)
                                player_health -= health_loss
                                print(f"you lost {health_loss} health")
                                print()
                                turn = "player"
                                sleep(2)
                            elif cpu_action == "2" and chamber[i] == 0:
                                typing_effect(f"{cpu_name} shot you", delay=0.05)
                                sleep(1)
                                print("Click!!")
                                sleep(1)
                                typing_effect("it was a blank bullet", delay=0.05)
                                print()
                                turn = "player"
                                sleep(2)
                    else:
                        break
                # storing the current chamber for next turn
                last_chamber = chamber

        # checking the winner of the game
        player_win = player_health > 0
        cpu_win = cpu_health > 0

        if player_win and story_visibility:
            print()
            typing_effect("host: we got a new winner!!!!")
            typing_effect(f"host: congrats {player_name} for being the new winner!!")
            typing_effect("you: no no this can't be happening no NOOOOO")
            typing_effect("in the end by winning you contributing yourself to this life and death game")
        elif player_win and not story_visibility:
            typing_effect(f"you won the game with {player_health} health left", delay=0.02)
        elif cpu_win and story_visibility:
            print()
            typing_effect("host: wuuuuuui big applause for our defending winner")
            typing_effect(f"host: {cpu_name} for defending his winner title, congrats!!")
            typing_effect(f"{cpu_name}: im sorry {player_name} but it is what it is")
        elif cpu_win and not story_visibility:
            typing_effect(f"you lost the game with your opponent having {cpu_health} health left", delay=0.02)
    else:
        print()
        sleep(2)
        typing_effect("you woken up on the side of the road. thinking what is just happened to you")
        typing_effect("but at least you still alive")

if __name__ == '__main__':
    main()
