class Playlists:
    def __init__(self, playlist_name, user_id):
        self.__user_id = user_id
        self.__name = playlist_name

    def name(self):
        return self.__name

    def user_id(self):
        return self.__user_id

