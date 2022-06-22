# Get the Spotify Playback status, and updates the Bio using the bot.
# Or if nothing is playing, then read from a list and ocassionaly update
import spotifyGetListening as sgl
import whatsappBioBot as wbb

import random, time

random.seed(int(time.time()))
idleTexts = ["Why are we still here? Just to suffer??",
             "Ngapain liat liat hei",
             "gak lagi dengerin lagu"]
             
time.sleep(2)
try:
    while True:
        cP = sgl.nowPlaying()
        print(cP)
        if cP['nowplaying']:
            wbb.updateBio(f'lagi denger lagu {cP["title"]} oleh {" & ".join(cP["artists"])} ({cP["progress"]//60}:{cP["progress"]%60}/{cP["length"]//60}:{cP["length"]%60})')
            time.sleep(5)
        else:
            wbb.updateBio(idleTexts[random.randint(0, len(idleTexts)-1)])
            time.sleep(10)
except KeyboardInterrupt:
    wbb.driver.close()
    

