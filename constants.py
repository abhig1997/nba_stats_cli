import pprint



printer = pprint.PrettyPrinter(indent=4) # my PrettyPrinter


# global upcoming_teams
# global upcoming_times

teams_played = []

all_scores = []

final_scores = []

box_score_urls = []

full_urls = []

statuses = []

upcoming_teams = []

upcoming_times = []

team_ids = {
	"Atlanta Hawks":"1610612737",
	"Boston Celtics": "1610612738",
	"Cleveland Cavaliers": "1610612739",
	"New Orleans Pelicans":"1610612740",
	"Chicago Bulls":"1610612741",
	"Dallas Mavericks":"1610612742",
	"Denver Nuggets":"1610612743",
	"Golden State Warriors":"1610612744",
	"Houston Rockets":"1610612745",
	"Los Angeles Clippers":"1610612746",
	"Los Angeles Lakers":"1610612747",
	"Miami Heat":"1610612748",
	"Milwaukee Bucks":"1610612749",
	"Minnesota Timberwolves":"1610612750",
	"Brooklyn Nets":"1610612751",
	"New York Knicks":"1610612752",
	"Orlando Magic":"1610612753",
	"Indiana Pacers":"1610612754",
	"Philadelphia 76ers":"1610612755",
	"Phoenix Suns":"1610612756",
	"Portland Trail Blazers": "1610612757",
	"Sacramento Kings": "1610612758",
	"San Antonio Spurs": "1610612759",
	"Oklahoma City Thunder": "1610612760",
	"Toronto Raptors": "1610612761",
	"Utah Jazz": "1610612762",
	"Memphis Grizzlies": "1610612763",
	"Washington Wizards": "1610612764",
	"Detroit Pistons": "1610612765",
	"Charlotte Hornets": "1610612766"

}