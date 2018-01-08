import json
import pprint
import requests
from nba_py import player
from nba_py import constants
from nba_py import game
import boxscore_functions
import player_functions
from constants import *
from get_games import *



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
        # print()
        print('2. View Finished Games for Today')
        print('3. View Upcoming Games for Today')
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
                first_name.strip()
                last_name.strip()
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
                first_name.strip()
                last_name.strip()
                id = player_functions.get_player_id(first_name, last_name)  # the id of the player requested
                if id is None:
                    print("The player was not found")
                else:
                    print("1. View Headline Stats for this Season")
                    print("2. View Regular Season Totals")
                    print("3. View Career Regular Season Totals")
                    print("4. View Post Season Totals")
                    print("5. View Career Post Season Totals")
                    print("6. View All Star Season Totals")
                    print("7. View Career All Star Season Totals")
                    print("8. View College Season Totals")
                    print("9. View Career College Season Totals")
                    player_career = player.PlayerCareer(id)
                    choice = input("Pick a number from the list above.\n")
                    num = int(choice)

                    print()
                    print()

                    if num == 1:
                        player_summary = player.PlayerSummary(id)
                        printer.pprint(player_summary.headline_stats())
                    elif num == 2:
                        # view regular season totals
                        printer.pprint(player_career.regular_season_totals())
                    elif num == 3:
                        printer.pprint(player_career.regular_season_career_totals())
                    elif num == 4:
                        printer.pprint(player_career.post_season_totals())
                    elif num == 5:
                        printer.pprint(player_career.post_season_career_totals())
                    elif num == 6:
                        printer.pprint(player_career.all_star_season_totals())
                    elif num == 7:
                        printer.pprint(player_career.career_all_star_season_totals())
                    elif num == 8:
                        printer.pprint(player_career.college_season_totals())
                    elif num == 9:
                        printer.pprint(player_career.college_season_career_totals())

                    print()
                    print()
            #tryna dip
            elif int(choice) == 9:
                pass
            else:
                print("Invalid menu choice")

        elif int(main_choice) == 2:
            print_scores()

        elif int(main_choice) == 3:
            print_upcoming_games()

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


def print_scores():
    find_games()
    box_score_count = 0
    print()
    print()

    if len(teams_played) == 0:
        # there havent been any games played yet
        print("No games have been played today")
        print()
        print()
        return



    for i in range(0, len(teams_played)):
        # print the first team that played and their score
        print(teams_played[i] + "               " + final_scores[i])

        if i % 2 != 0:
            # finished printing out two teams, need to print out their box score url
            print("Boxscore URL: " + full_urls[box_score_count])
            box_score_count = box_score_count + 1
            print("---------------------------------------")

def print_upcoming_games():
    get_upcoming_games()

    print()
    print()
    # print(len(upcoming_teams))
    # print(len(upcoming_times))

    # the necessary arrays should be populated now
    time_count = 0

    i = 0   

    while i < len(upcoming_teams):
        print(upcoming_teams[i] + " vs. " + upcoming_teams[i+1] + " at " + upcoming_times[time_count])
        i = i + 2
        time_count = time_count + 1
        print("---------------------------------------") 


    print()
    print()



if __name__ == "__main__":
    # print(constants.SeasonType.Regular)
    # get_player()
    main()