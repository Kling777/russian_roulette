"""
this file is for testing purposes,
it is not used in the actual game
please run the main.py for the actual game
"""

import sys, time, random
def typing_effect(text, delay=0.05):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(delay)
    print()

def main():
    print("hello python")

if __name__ == '__main__':
    main()
