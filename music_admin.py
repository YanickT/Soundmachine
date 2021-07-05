import os

PATH = "sounds/"
FORMATS = ["mp3", "flac"]


class MusicAdmin:

    def __init__(self):
        self.files = {}
        self.sync()

    def sync(self):
        directories = os.listdir(PATH)
        for directiory in directories:
            self.files[directiory] = [file for file in os.listdir(PATH + directiory) if file.split(".")[-1] in FORMATS]


MUSIC = MusicAdmin()
