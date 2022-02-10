import json


class Album():
    def __init__(self, albumId, albumName):
        self.albumId = albumId
        self.albumName = albumName

    def __str__(self):
        return "albumId: {0}, albumName: {1}".format(self.albumId, self.albumName)


def songDetails(songPath):
    with open(songPath) as album:
        json_song = json.load(album)
        album = Album(json_song["track"]["album"]["id"], json_song["track"]["album"]["name"])
    return (album)
