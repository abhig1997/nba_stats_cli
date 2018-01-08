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

    teams_played = []
    filteredteams = []

    # print(parsed)

    for i in parsed.find_all("td", "shsLeaderTtl"):
    	# print(teams_that_played.string)
    	if "Leaders" not in i.string:
    		teams_played.append(i.string)
    	# teams_played.append(teams_that_played.string)

    # for i in range(0, len(teams_played)):
    # 	if (i % 3 != 0):
    # 		print(teams_played[i])
    print(teams_played)




if __name__ == "__main__":
    find_games()