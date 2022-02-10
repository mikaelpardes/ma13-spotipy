class ToMuchPlayLists(Exception):
    print("you can insert only 5 playlists")
    pass


class PlayListNameExsist(Exception):
    print("you already have playlist in this name")
    pass


class ToMuchSongsInPlayList(Exception):
    print("you can insert only 20 songs")
    pass
