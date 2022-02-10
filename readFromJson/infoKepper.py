from music.album import Album
from music.artist import Artist
from music.song import Song
from readFromJson.readJsonFiles import dataStorage


class InfoKepper:
    def __init__(self):
        self.albums = []
        self.artists = []
        self.songs = []

    def insertDataToAlbum(self, dataStorage):
        for song in dataStorage:
            newAlbum = Album(song["track"]["album"]["id"], song["track"]["album"]["name"])
            self.albums.append(newAlbum)
            print(newAlbum)
        return self.albums

    def insertDataToArtistList(self, dataStorage):
        for artist in dataStorage:
            newArtist = Artist(artist["track"]["artists"][0]["id"], artist["track"]["artists"][0]["name"])
            self.artists.append(newArtist)
            print(newArtist)
        return self.artists

    def insertDataToSongsList(self, dataStorage):
        for song in dataStorage:
            newSong = Song(song["track"]["id"], song["track"]["name"], song["track"]["popularity"])
            self.songs.append(newSong)
            print(newSong)
        return self.songs


info = InfoKepper()
info.insertDataToAlbum(dataStorage)
info.insertDataToSongsList(dataStorage)
info.insertDataToArtistList(dataStorage)
