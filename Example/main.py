import rpc
import time
from time import mktime
import random

SwordArtOnline_locations = {
    "Floor 1": ["Town of Beginnings",
                "Black Iron Palace",
                "Hidden Dungeon",
                "Monument of Swordsmen",
                "Monument of Life",
                "Chamber of Resurrection",
                "Tolbana",
                "Horunka Village",
                "Medai Village"]
}

current_floor = "Floor 1"

print("Sword Art Online Rich Presence")
client_id = ''  # Your application's client ID as a string. (This isn't a real client ID)

time.sleep(1)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "Exploring " + random.choice(SwordArtOnline_locations[current_floor]),  # anything you like
            "details": f"Aincrad {current_floor}",  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Online",  # anything you like
                "small_image": "green",  # must match the image key
                "large_text": "Swordsman - Level 10",  # anything you like
                "large_image": "default"  # must match the image key
            },
            "buttons": [
                {"label": "??? Sword Art Online ???", "url": "https://www.youtube.com/watch?v=onYSNgHbbW8&ab_channel=Gigguk"},
                {"label": "*----* 🅶🅸🆃🅷🆄🅱 *----*", "url": "https://github.com/MahdeenSky"}
            ]
        }
    try:
        rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
        print("RPC connection successful.")
        rpc_obj.set_activity(activity)
        time.sleep(900)
    except:
        print("Failed to set activity, trying again in 5 seconds")
        time.sleep(5)
