import os
import vlc
import time
import subprocess

dirname = os.path.dirname(__file__)

def playerVLC():
    #proces = subprocess.Popen(['obs'])
    #proces
    time.sleep(1)
    from OBS import obsSceneTransition, obsSceneVLC
    playlist = dirname + '/playlistWithCommercials.pls'
    with open(playlist, 'r') as f:
        playlist=[i for line in f for i in line.split(',')]
        playlist = map(lambda s: s.strip(), playlist)
    instance = vlc.Instance('--play-and-exit', '--input-repeat=-1', '--fullscreen', '--mouse-hide-timeout=0')
    for song in playlist:
        obsSceneTransition()
        player = instance.media_player_new()
        media = instance.media_new(song)
        media.get_mrl()
        player.set_media(media)
        player.play()
        playing = set([1, 2, 3, 4])
        time.sleep(10)
        obsSceneVLC()
        duration = player.get_length() / 1000
        mm, ss = divmod(duration, 60)

        while True:
            state = player.get_state()
            if state not in playing:
                break
            continue

playerVLC()




