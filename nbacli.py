import pandas as pd
import json
import pprint
import requests
from nba_py import player
from nba_py import constants
from nba_py import game
import boxscore_functions

# def get_player():
#     response = player.get_player(first_name='Kyrie', last_name='Irving', season='2016-17', only_current=0, just_id=False)
#     # print(type(response))
#     # print(response)
#
#
# def test():
#     dataframe = game.BoxscoreSummary("0021700570")
#     print(dataframe.line_score())

"""
Prints the main menu for the program
"""
def print_main_menu():
    print('What would you like to do?')
    print('1. Access boxscore functions')
    print('9. Exit the program')


"""
To run the program
"""
def main():
    print('Welcome to Abhi\'s NBA CLI!')
    loop=True
    while loop:
        print('What would you like to do?')
        print('1. View a boxscore')
        print('9. Exit the program')
        main_choice = input("Pick a number from the list below\n")
        if int(main_choice) == 1:
            print()



        elif int(main_choice) == 9:
            print("Thank you for using Abhi's NBA Stats CLI!")
            return

    last_choice = input("Would you like to run the program again? Press 1 to run again, or 2 to exit\n")
    if int(last_choice) == 1:
        main()
    elif int(last_choice) == 2:
        print("Thank you for using Abhi's NBA Stats CLI!")
        return





if __name__ == "__main__":
    # print(constants.SeasonType.Regular)
    # get_player()
    main()