import config
from readFromJson.readJsonFiles import dataStorage
from readFromJson.infoKepper import InfoKepper


def getAllArtists():
    info = InfoKepper()
    return info.insertDataToArtistList(dataStorage)


def albumsNamePerArtist(artistId):
    albumsName = []
    for artist in dataStorage:
        if artistId == artist["track"]["artists"][0]["id"]:
            albumsName.append(artist["track"]["album"]["name"])
    return albumsName


def getAllSongsPopularityPerArtist(artistId):
    songsPopularity = []
    for artist in dataStorage:
        if artistId == artist["track"]["artists"][0]["id"]:
            songsPopularity.append(artist["track"]["popularity"])
    return songsPopularity


def mostTenPopularSongPerArtist(artistId):
    mostPopularSong = []
    popularSong = []
    if len(getAllSongsPopularityPerArtist(artistId)) <= config.popularSongMaxNumber:
        return getAllSongsPopularityPerArtist(artistId)
    else:
        PopularSong = sorted(getAllSongsPopularityPerArtist(artistId))
        for song in range(10):
            mostPopularSong.append(popularSong[song])
        return mostPopularSong


def mostPopularSongsNamePerArtist(artistId):
    mostPopularSong = mostTenPopularSongPerArtist(artistId)
    mostTenPopularitySongs = []
    for song in mostPopularSong:
        for songs in dataStorage:
            if song == songs["track"]["popularity"]:
                mostTenPopularitySongs.append(songs["track"]["name"])
    return mostTenPopularitySongs


def getAllAlbumSongs(albumId):
    songsInAlbum = []
    for album in dataStorage:
        if albumId == album["track"]["album"]["id"]:
            songsInAlbum.append(album["track"]["name"])
    return songsInAlbum
