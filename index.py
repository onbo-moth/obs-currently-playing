import pygame
import os
import re

def child():
    import signal
    while 1:
        reply = input("Input \"k\" to kill the process.\n")
        if reply == "k":
            os.kill(os.getppid(), signal.SIGKILL)
            # ISSUE: error shows up after updating the screen the second time (pressing up, etc.)

def parent():
    # Check if process is a child.
    newpid = os.fork()
    if newpid == 0:
        child()

    """
    File structure:
    file:
        script:
            index.py
        cp.txt
        [Put mp3 files here.]
    """

    # Get entries of file, filter out extensions other than ".mp3".
    entries = [x for x in os.listdir("../") if re.match(".*.mp3", x)!=None]

    pygame.init()

    pygame.mixer.init()

    while 1:
        for entry in entries:
            # Open currently playing file.
            cp = open("../cp.txt", "w")
            # Play the music.
            pygame.mixer.music.load(f"../{entry}")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.3)
            # Write song name to cp.txt.
            cp.write(f"now playing: {entry[:-4]}")
            cp.close()
            # Wait
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

if __name__=="__main__":
    parent()
