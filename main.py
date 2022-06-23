# Get the Spotify Playback status, and updates the Bio using the bot.
# Or if nothing is playing, then read from a list and ocassionaly update
import spotifyGetListening as sgl
import whatsappBioBot as wbb

import random, time

random.seed(int(time.time()))
idleTexts = ["Why are we still here? Just to suffer??",
             "Haloo, lagi nyari apa nih",
             "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]

time.sleep(2)

try:
    pP = sgl.nowPlaying()
    while True:
        
        cP = sgl.nowPlaying()
        print(cP)
        if cP['nowplaying']:
            wbb.updateBio(f'lagi denger lagu {cP["title"]} oleh {" & ".join(cP["artists"])} ({str(cP["progress"]//60).rjust(2, "0")}:{str(cP["progress"]%60).rjust(2, "0")}/{str(cP["length"]//60).rjust(2, "0")}:{str(cP["length"]%60).rjust(2, "0")})')
            time.sleep(5)
        elif pP['nowPlaying'] == False and cP['nowPlaying'] == False:
            time.sleep(2) 
        else:
            wbb.updateBio(idleTexts[random.randint(0, len(idleTexts)-1)])
            time.sleep(10)
        pP = cP
except KeyboardInterrupt:
    wbb.driver.close()
    

