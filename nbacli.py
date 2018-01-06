import json
import pprint
import requests
from nba_py import player
from nba_py import constants
from nba_py import game
import boxscore_functions
import player_functions

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
    printer = pprint.PrettyPrinter(indent=4)

    print('Welcome to Abhi\'s NBA CLI!')
    loop=True
    while loop:
        print('What would you like to do?')
        print('1. Get information about a player')
        print('9. Exit the program')
        main_choice = input("Pick a number from the list above\n")
        if int(main_choice) == 1:
            first_name = input("What is the first name of the player you'd like to view?\n")
            last_name = input("What is the last name?\n")

            print("What information about the player would you like to view?")
            print("1. Basic Info (Vitals)")
            print("2. View Averages For All Seasons")
            print("3. View Regular Season Career Averages")
            print("9. Go back to main menu")
            choice = input("Pick a number from the list above.\n")

            # getting basic info
            if int(choice) == 1:
                id = player_functions.get_player_id(first_name, last_name) # the id of the player requested
                if id is None:
                    print("The player was not found")
                else:
                    # getting the basic player summary
                    player_summary = player.PlayerSummary(id)
                    vitals = player_summary.info()
                    printer.pprint(vitals)
            # getting averages for all seasons
            elif int(choice) == 2:
                id = player_functions.get_player_id(first_name, last_name)  # the id of the player requested
                if id is None:
                    print("The player was not found")
                else:
                    # getting the basic player summary
                    player_career = player.PlayerCareer(id)
                    printer.pprint(player_career.regular_season_totals())
            # getting career regular season averages
            elif int(choice) == 3:
                id = player_functions.get_player_id(first_name, last_name)  # the id of the player requested
                if id is None:
                    print("The player was not found")
                else:
                    # getting the player career highs
                    player_career = player.PlayerCareer(id)
                    printer.pprint(player_career.regular_season_career_totals())
            #tryna dip
            elif int(choice) == 9:
                pass
            else:
                print("Invalid menu choice")


        elif int(main_choice) == 9:
            print("Thank you for using Abhi's NBA Stats CLI!")
            return
        else:
            print("Invalid menu choice")


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