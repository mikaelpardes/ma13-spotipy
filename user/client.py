import config
import exceptions
import sortingInfo.infoSearch
from playlist import PlayList
import pandas as pd


class User:

    def __init__(self, userName, userPassword, isPrime):
        self.userName = userName
        self.userPassword = userPassword
        self.isPrime = isPrime
        self.playlists = []

    def __str__(self):
        return "userName: {0}, userPassword: {1}, isPrime: {2}".format(self.userName, self.userPassword, self.isPrime)

    def checkPlayListsListLength(self):
        if self.isPrime == False:
            if len(self.playlists) == config.maxPlayListsForRegularUser:
                raise exceptions.ToMuchPlayLists

    def checkIfPlayListNameExsist(self, playListName):
        for playlist in self.playlists:
            if playlist.playListName == playListName:
                raise exceptions.PlayListNameExsist

    def checkPLayListLen(self, playList):
        playListLen = playList.numOfSongInPlayList()
        if self.isPrime == False:
            if playListLen == config.maxSongsForRegularUser:
                raise exceptions.ToMuchSongsInPlayList

    def addNewPlaylist(self, playlistName):
        self.checkPlayListsListLength()
        self.checkIfPlayListNameExsist(playlistName)
        playList = PlayList(playlistName)
        self.playlists.append(playList)

    def changePassword(self, password):
        self.userPassword = password

    def addToExsistPlaylist(self, playList, songName):
        self.checkPLayListLen(playList)
        playList.addSong(songName)

    def getAllArtists(self):
        if self.isPrime == False:
            df = pd.DataFrame(sortingInfo.infoSearch.getAllArtists())
            df1 = df.head(5)
            return df1
        else:
            return sortingInfo.infoSearch.getAllArtists()
