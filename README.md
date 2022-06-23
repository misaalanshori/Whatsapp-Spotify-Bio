# Whatsapp Spotify Bio
Show your Spotify listening status on your Whatsapp Bio/About. Kinda like discord

Though now that I'm thinking about it, people very rarely check someones Whatsapp profile, so this is kinda pointless lol.

One interesting thing is that Whatsapp is able to update the About text very quickly, its basically instant. So only after a few seconds, anyone looking at the About text would immediately see it update. 

## Setup
You need Firefox, geckodriver (in your path), Selenium, and Spotipy to run this. You will also need the Spotify api keys from the Spotify Developer dashboard (its very easy to make). And then put your Spotify api credentials to spotifySecret.py and it should be ready to run. 

At first it will ask to login for Spotify (just once), follow the instruction and copy the link, and then a firefox window should open with web.whatsapp.com, here you need to link your whatsapp account with the QR Code and then after everything is fully loaded you can press enter in the terminal. If everything goes right, then the bot should automatically update your Whatsapp bio

## Notes
- Make sure the browser window is visible at all times, as It might cause errors with the automation
- I can't figure out how to keep the Whatsapp session logged in, so you will need to login every time the script starts. There might be a way with the chrome driver. But I have not tested it yet.
- I take no responsibility if your Whatsapp account gets in trouble or if anything else happens. Use this at your own risk