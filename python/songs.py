class Songs:
    def __init__(self, song_id, song_name, popularity):
        self.__song_id = song_id
        self.__song_name = song_name
        self.__popularity = popularity

    def get_song_id(self):
        return self.__song_id

    def get_song_name(self):
        return self.__song_name

    def get_popularity(self):
        return self.__popularity
