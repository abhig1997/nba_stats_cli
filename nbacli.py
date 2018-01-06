import json
import pprint
import requests
from nba_py import player
from nba_py import constants
from nba_py import game
import boxscore_functions
import player_functions

printer = pprint.PrettyPrinter(indent=4) # my PrettyPrinter

# def get_player():
#     response = player.get_player(first_name='Kyrie', last_name='Irving', season='2016-17', only_current=0, just_id=False)
#     # print(type(response))
#     # print(response)
#
#
# def test():
#     dataframe = game.BoxscoreSummary("0021700570")
#     print(dataframe.line_score())


def get_career_totals(id):
    player_career = player.PlayerCareer(id)
    printer.pprint(player_career.regular_season_career_totals())


"""
To run the program
"""
def main():


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
            print("2. View Season Averages")
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
            # submenu for season averages
            elif int(choice) == 2:
                id = player_functions.get_player_id(first_name, last_name)  # the id of the player requested
                if id is None:
                    print("The player was not found")
                else:
                    print("1. View Regular Season Totals")
                    print("2. View Career Regular Season Totals")
                    print("3. View Post Season Totals")
                    print("4. View Career Post Season Totals")
                    print("5. View All Star Season Totals")
                    print("6. View Career All Star Season Totals")
                    print("7. View College Season Totals")
                    print("8. View Career College Season Totals")
                    player_career = player.PlayerCareer(id)
                    choice = input("Pick a number from the list above.\n")
                    num = int(choice)

                    if num == 1:
                        # view regular season totals
                        printer.pprint(player_career.regular_season_totals())
                    elif num == 2:
                        printer.pprint(player_career.regular_season_career_totals())
                    elif num == 3:
                        printer.pprint(player_career.post_season_totals())
                    elif num == 4:
                        printer.pprint(player_career.post_season_career_totals())
                    elif num == 5:
                        printer.pprint(player_career.all_star_season_totals())
                    elif num == 6:
                        printer.pprint(player_career.career_all_star_season_totals())
                    elif num == 7:
                        printer.pprint(player_career.college_season_totals())
                    elif num == 8:
                        printer.pprint(player_career.college_season_career_totals())
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