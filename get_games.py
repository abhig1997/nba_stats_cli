from bs4 import BeautifulSoup
import requests
from pprint import pprint

from constants import *
# import constants

def find_games():
    response = requests.get("http://stats.nesn.com/nba/scoreboard.asp?meta=true")
    parsed = BeautifulSoup(response.text, 'lxml')

    # teams_played = [] # the list of teams that have already played today

    # all_scores = []
    # final_scores = []
    # box_score_urls = []
    # full_urls = []

    # get all the teams that have finished games today
    for i in parsed.find_all("td", "shsLeaderTtl"):
    	# print(teams_that_played.string)
    	if "Leaders" not in i.string:
    		teams_played.append(i.string)

    # get everything under the shsTotD header, these are scores from games have been played
    for j in parsed.find_all("td", "shsTotD"):
    	all_scores.append(j.string)


   	# get final scores for games that have been played by filtering from all_scores array
    for k in range(0, len(all_scores)):
    	if all_scores[k] == 'Tot':
    		final_scores.append(all_scores[k+5])
    		final_scores.append(all_scores[k+10])


    for i in parsed.find_all("td", "shsLiveNav"):
    	for j in i.find_all("a", href=True):
    		# print(j)
    		# print(type(j["href"]))
    		box_score_urls.append(j["href"])

    for i in range(0, len(box_score_urls)):
    	# print(i)
    	if 'boxscore' in box_score_urls[i]:
    		full_urls.append("http://stats.nesn.com" + box_score_urls[i])

    for h in parsed.find_all("td", "shsTeamCol shsNamD"):
    	statuses.append(h.string)

	# for h in soup.find_all("td","shsTeamCol shsNamD"):
		# statuses.append(h.string)


def get_upcoming_games():
	# upcoming_teams = []

	# global upcoming_teams
	# global upcoming_times

	# constants.upcoming_teams = []
	# constants.upcoming_times = []

	response = requests.get("http://stats.nesn.com/nba/scoreboard.asp?meta=true")
	parsed = BeautifulSoup(response.text, 'lxml')

	for i in parsed.find_all("td", "shsNamD"):
		for j in i.find_all("a"):
			# print(j.string)
			upcoming_teams.append(j.string)

	# upcoming_times = []


	for i in parsed.find_all("span", class_ = "shsTimezone shsETZone"):
		to_string = str(i.string)
		upcoming_times.append(to_string)

if __name__ == "__main__":
    get_upcoming_games()