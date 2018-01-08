from bs4 import BeautifulSoup
import requests

teams = []
filteredteams = []
scores = []
filteredscores = []
status = []
urls = []
filteredurls = []

def find_games():
    response = requests.get("http://stats.nesn.com/nba/scoreboard.asp?meta=true")
    parsed = BeautifulSoup(response.text, 'lxml')

    teams_played = [] # the list of teams that have already played today

    all_scores = []
    final_scores = []

    # print(parsed)

    for i in parsed.find_all("td", "shsLeaderTtl"):
    	# print(teams_that_played.string)
    	if "Leaders" not in i.string:
    		teams_played.append(i.string)

    for j in parsed.find_all("td", "shsTotD"):
    	all_scores.append(j.string)

    for k in range(0, len(all_scores)):
    	if all_scores[k] == 'Tot':
    		final_scores.append(all_scores[k+5])
    		final_scores.append(all_scores[k+10])
    		# print(all_scores[k+10])


    # print(teams_played)
    print(teams_played)
    print(final_scores)



if __name__ == "__main__":
    find_games()