import json
import requests
from nba_py import player


"""
Gets player id, given first name and last name
Last name is NOT required
"""
def get_player_id(first_name, last_name=None):
    # print("first name is " + first_name)
    # print("last name is " + last_name)

    # if last_name is not None:
    try:
        player_id = player.get_player(first_name, last_name, just_id=True)
    except Exception as e:
        print(e)
        player_id = None

    # player.get_
    # else:
    #     player_id = player.get_player(first_name)

    # print(player_id)
    # print(type(player_id))
    return player_id

def get_player_info(player_id):
    summary = player.PlayerSummary(player_id)
    return summary
