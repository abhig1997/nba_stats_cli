import json
import pprint
import requests
from nba_py import player
from nba_py import constants
from nba_py import team
from nba_py import game
import boxscore_functions
import player_functions
from constants import *
from get_games import *
from nba_py import Scoreboard



def get_career_totals(id):
    player_career = player.PlayerCareer(id)
    printer.pprint(player_career.regular_season_career_totals())

"""
    Prints the main menu for the CLI. This is printed at the beginning of execution, and after a command is executed.
"""
def print_main_menu():
    print('What would you like to do?')
    print('1. Get information about a player')
    # print()
    print('2. View Completed/In Progress Games')
    print('3. View Today\'s Upcoming Games')
    print('4. Get information about a team')
    print('5. View Eastern Conference Standings')
    print('6. View Western Conference Standings')
    # print()
    print('9. Exit the program')
    print('100. Used for testing')


"""
    Helper function to handle when the user wants to view information about a team.
"""
def print_team_information(team_choice):
    # print(team_choice)
    try:
        team_id = team_ids[team_choice]
    except:
        print("Invalid team.")
        print()
        print()
        return
    # print(team_id)
    print('1. View Team Roster')
    print('2. View Team Coaches')
    print('3. View Championship History')
    print('4. View Hall of Fame History')
    print('5. View Retired Jerseys')
    print('6. View Season Totals for Team\'s Players')
    print('7. View Shooting Splits by Area')
    print('8. View Season Totals for 2017-18')
    print('9. Go back to main menu')

    team_info_choice = input("What information about " + team_choice + " would you like to view?\n")

    teamdetails = team.TeamDetails(team_id)

    if int(team_info_choice) == 1:
        teamcommonroster = team.TeamCommonRoster(team_id, season='2017-18')
        printer.pprint(teamcommonroster.roster())

    elif int(team_info_choice) == 2:
        teamcommonroster = team.TeamCommonRoster(team_id, season='2017-18')
        printer.pprint(teamcommonroster.coaches())

    elif int(team_info_choice) == 3:
        # teamdetails = team.TeamDetails(team_id)
        printer.pprint(teamdetails.awards_championships())

    elif int(team_info_choice) == 4:
        # teamdetails = team.TeamDetails(team_id)
        printer.pprint(teamdetails.hof())

    elif int(team_info_choice) == 5:
        # teamdetails == team.TeamDetails(team_id)
        printer.pprint(teamdetails.retired())

    elif int(team_info_choice) == 6:
        teamplayers = team.TeamPlayers(team_id, season='2017-18')
        printer.pprint(teamplayers.season_totals())
        # printer.pprint(teamdetails.social_sites())

    elif int(team_info_choice) == 7:
        shooting = team.TeamShootingSplits(team_id)
        printer.pprint(shooting.shot_areas())

    elif int(team_info_choice) == 8:
        sum = team.TeamSummary(team_id, season='2017-18')
        printer.pprint(sum.season_ranks())

    elif int(team_info_choice) == 9:
        return

    else:
        print("Invalid menu choice")

"""
    Helper function to handle printing information for a player.
"""
def print_player_information(first_name, last_name):
    print("What information about the player would you like to view?")
    print("1. Basic Info (Vitals)")
    print("2. View Season Averages")
    print("3. Compare to Another Player")
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

    elif int(choice) == 3:
        vs_player_first_name = input("What is the first name of the player you'd like to compare against?\n")
        vs_player_last_name = input("What is their last name?\n")

        id = player_functions.get_player_id(first_name, last_name)
        vs_player_id = player_functions.get_player_id(vs_player_first_name, vs_player_last_name)  # the id of the player to be compared against
        printer.pprint(player.PlayerVsPlayer(id, vs_player_id, season='2017-18').overall())



    #tryna dip
    elif int(choice) == 9:
        return

    elif int(choice) == 100:
        printer.pprint(player.get_player(first_name, last_name, season='2017-18', just_id=False))
    else:
        print("Invalid menu choice")


"""
To run the program
"""
def main():


    print('Welcome to Abhi\'s NBA CLI!')
    loop=True
    while loop:
        # print('What would you like to do?')
        # print('1. Get information about a player')
        # # print()
        # print('2. View Completed/In Progress Games')
        # print('3. View Today\'s Upcoming Games')
        # # print()
        # print('9. Exit the program')
        # print('100. Used for testing')
        print_main_menu()
        main_choice = input("Pick a number from the list above\n")
        if int(main_choice) == 1:
            first_name = input("What is the first name of the player you'd like to view?\n")
            last_name = input("What is the last name?\n")

            print_player_information(first_name.strip(), last_name.strip())

        elif int(main_choice) == 2:
            print_scores()

        elif int(main_choice) == 3:
            print_upcoming_games()

        elif int(main_choice) == 4:
            team_choice = input("Enter the name of the team you'd like to view (ex. Boston Celtics)\n")
            print_team_information(team_choice)

        elif int(main_choice) == 5:
            board = Scoreboard()
            printer.pprint(board.east_conf_standings_by_day())
            
        elif int(main_choice) == 6:
            board = Scoreboard()
            printer.pprint(board.west_conf_standings_by_day())

        elif int(main_choice) == 9:
            print("Thank you for using Abhi's NBA Stats CLI!")
            return

        elif int(main_choice) == 100:
            # team_game_logs = team.TeamGameLogs("1610612738")
            # # print(type(team_game_logs))
            # printer.pprint(team_game_logs.info())
            # teamcommonroster = team.TeamCommonRoster("1610612738", season='2017-18')
            # coaches = teamcommonroster.coaches()
            # roster = teamcommonroster.roster()
            # print(coaches)
            # printer.pprint(roster)
            teamlist = team.TeamList(league_id='00')
            printer.pprint(teamlist.info())

        else:
            print("Invalid menu choice")


    last_choice = input("Would you like to run the program again? Press 1 to run again, or 2 to exit\n")
    if int(last_choice) == 1:
        main()
    elif int(last_choice) == 2:
        print("Thank you for using Abhi's NBA Stats CLI!")
        return


def print_scores():
    reset_constants()
    find_games()
    box_score_count = 0

    # print("these are statuses")
    # print(statuses)


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
        if i % 2 == 0:
            print(statuses[box_score_count])
            print()
        print(teams_played[i] + "               " + final_scores[i])

        if i % 2 != 0:
            # finished printing out two teams, need to print out their box score url
            print("Boxscore URL: " + full_urls[box_score_count])
            box_score_count = box_score_count + 1
            print("---------------------------------------")


def print_upcoming_games():

    reset_constants()

    get_upcoming_games()
    find_games()


    # print("these are upcoming teams")
    # print(upcoming_teams)

    # reset_constants()
    # find_games()
#
    # print("these are other teams")
    # print(teams_played)

    print()
    print()
    # print(len(upcoming_teams))
    # print(len(upcoming_times))


    new_teams = []
    for i in upcoming_teams:
        if i not in teams_played:
            new_teams.append(i)

    # print(new_teams)


    # the necessary arrays should be populated now
    time_count = 0

    i = 0   

    while i < len(new_teams):
        print(new_teams[i] + " vs. " + new_teams[i+1] + " at " + upcoming_times[time_count])
        i = i + 2
        time_count = time_count + 1
        print("---------------------------------------") 


    print()
    print()

"""
    Resets the constants to be empty arrays, so that the user can run multiple game queries in one program run
"""
def reset_constants():
    upcoming_teams[:] = []
    upcoming_times[:] = []

    teams_played[:] = []
    statuses[:] = []
    final_scores[:] = []
    full_urls[:] = []
    all_scores[:] = []
     

if __name__ == "__main__":
    # print(constants.SeasonType.Regular)
    # get_player()
    main()