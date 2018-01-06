import json
import requests
from nba_py import game




def get_player_stats_from_game(game_id):
    boxscore = game.Boxscore(game_id)
    return boxscore.player_stats()