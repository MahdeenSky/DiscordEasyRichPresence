import rpc
import time
from time import mktime

print("Discord Rich Presence")
client_id = ''  # Your application's client ID as a string. (This isn't a real client ID)

time.sleep(1)
start_time = mktime(time.localtime())
while True:
    activity = {
            "state": "2nd Header",  # anything you like
            "details": "1st Header",  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "Small Image Hover Text",  # anything you like
                "small_image": "Small Image Key",  # must match the image key
                "large_text": "Large Image Hover Text",  # anything you like
                "large_image": "Large Image Key"  # must match the image key
            },
            "buttons": [
                {"label": "Button 1 Text", "url": "https://www.google.com"},
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
