class PlaylistSongs:
    def __init__(self, name, song_id):
        self.__song_id = song_id
        self.__name = name

    def name(self):
        return self.__name

    def song_id(self):
        return self.__song_id
