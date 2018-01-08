from bs4 import BeautifulSoup
import requests
from pprint import pprint

from constants import *

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





if __name__ == "__main__":
    find_games()