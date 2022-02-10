from user.client import User


class ArtistUser(User):
    def __init__(self, albums: list, userName, userPassword):
        super().__init__(userName, userPassword, True)
        self.albums = albums

    def addNewAlbum(self, album):
        self.albums.append(album)
