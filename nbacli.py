import pandas as pd
import json
import pprint
import requests
from nba_py import player
from nba_py import constants
from nba_py import game

# def get_player():
#     response = player.get_player(first_name='Kyrie', last_name='Irving', season='2016-17', only_current=0, just_id=False)
#     # print(type(response))
#     # print(response)
#
#
# def test():
#     dataframe = game.BoxscoreSummary("0021700570")
#     print(dataframe.line_score())

def main():
    print('Welcome to Abhi\'s NBA CLI!')
    while True:
        print('What would you like to do?')
        print('1. View a boxscore')
        print('9. Exit the program')
        main_choice = input("Pick a number from the list below\n")
        if int(main_choice) == 1:
            print('aight bet, finna access boxscore functions')
        elif int(main_choice) == 9:
            print('Thank you for using the program')
            exit()





if __name__ == "__main__":
    # print(constants.SeasonType.Regular)
    # get_player()
    main()