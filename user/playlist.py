class PlayList:
    def __init__(self, playListName):
        self.playListName = playListName
        self.songList = []

    def addSong(self, songName):
        self.songList.append(songName)

    def removeSong(self, songName):
        self.songList.remove(songName)

    def numOfSongInPlayList(self):
        return len(self.songList)

    def __str__(self):
        return "playListName: {0}, songInPlayList: {1}".format(self.playListName, self.songList)


def addPlayListToPlaylistFile(playList):
    file = open("playlists.txt", "w")
    file.write(playList.__str__())
    file.close()
