import json


class Artist():
    def __init__(self, artistId, artistName):
        self.artistId = artistId
        self.artistName = artistName

    def __str__(self):
        return "artistId: {0}, artistName: {1}".format(self.artistId, self.artistName)


def artistDetails(songPath):
    with open(songPath) as artist:
        json_song = json.load(artist)
        artist = Artist(json_song["track"]["artists"][0]["id"], json_song["track"]["artists"][0]["name"])
    return (artist)
