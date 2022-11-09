<h1 align="center">DiscordEasyRichPresence</h1>
<h5 align="center">"DiscordEasyRichPresence is a script for MacOS and Linux users, for interfacing your game with a locally running Discord desktop client (Supports Buttons)"</h5>
<!--<img align="right" src='https://github.com/niveshbirangal/discord-rpc/blob/master/readmeassets/intro.gif' width="150">-->

### Requirements:
Python 3.0 and above
### Setup:
clone this to your local device
```bash
git clone https://github.com/MahdeenSky/DiscordEasyRichPresence
```
Go to the developer portal and create an application
```bash
https://discord.com/developers/applications
```
<img align="center" src='https://github.com/niveshbirangal/discord-rpc/blob/master/readmeassets/createapp.gif'>
<br><br />
Add assets(image) to your application (Name of asset is image key)
<br><br>
<img align="center" src='https://i.imgur.com/i4dYvnv.png'>
<br><br /> 
Select images and clear all fields except <code>PARTY ID</code> and <code>JOIN SECRET</code>
<br><br>
<img align="center" src='https://i.imgur.com/pPzipuv.png'>
<br><br />
Get your client ID and fill it in the gaps in main.py
<br><br>
<img align="center" src='https://i.imgur.com/X3G0hQy.png'>
<br><br />
Within main.py, change the activity code according to your best fit

```bash
activity = {
            "state": "Exploring Town of Beginnings",  # anything you like
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
            "buttons": [ # optional, add if you want buttons
                {"label": "??? Sword Art Online ???", "url": "https://www.youtube.com/watch?v=onYSNgHbbW8&ab_channel=Gigguk"}, 
                {"label": "*----* 🅶🅸🆃🅷🆄🅱 *----*", "url": "https://github.com/MahdeenSky"} # label = button text, url = link to redirect on click
            ]
        }
```
Make sure your Discord app is running and then run the main.py
```bash
python3 main.py
```
<img align="center" src='https://i.imgur.com/7VdRxrD.png'>

<!-- EXAMPLE -->
## Example
I have included the example provided inside the Example Folder, that you can run if you fill it in by recreating the app, which involves 
1. making an app with the name "Sword Art Online"
2. adding the "default" and "green" assets
3. editing the visualizer section as shown above
4. placing the client ID inside the main.py script.

Finally run `python3 main.py`

<!-- ROADMAP -->
## Roadmap
See the [open issues](https://github.com/MahdeenSky/DiscordEasyRichPresence/issues) for a list of proposed features (and known issues).

<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
