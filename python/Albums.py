class Albums:
    def __init__(self, album_id, album_name):
        self.__album_id = album_id
        self.__album_Name = album_name

    def get_album_id(self):
        return self.__album_id

    def get_album_name(self):
        return self.__album_Name
