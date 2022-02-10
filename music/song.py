import json


class Song:
    def __init__(self, songId, songName, songPopularity):
        self.songId = songId
        self.songName = songName
        self.songPopularity = songPopularity

    def __str__(self):
        return "songId: {0}, songName: {1}, songPopularity:{2}".format(self.songId, self.songName,

                                                                       self.songPopularity)


def songDetails(songPath):
    with open(songPath) as song:
        json_song = json.load(song)
        song = Song(json_song["track"]["id"], json_song["track"]["name"], json_song["track"]["popularity"])
    return (song)
