import pygameextra as pe
pe.init()
from os import path
scriptpath = str(path.realpath(__file__)).replace("test_sound.py",'')
sound = None
def test_load():
    global sound
    sound = pe.sound.load(scriptpath+"testing_assets/test-sound.mp3")
def test_play():
    global sound
    pe.sound.play(sound)
    pe.time.sleep(3000)