class Artists:
    def __init__(self, artist_id, artist_name, genre='general'):
        self.__artist_id = artist_id
        self.__artist_Name = artist_name
        self.__genre = genre

    def get_artist_id(self):
        return self.__artist_id

    def get_artist_name(self):
        return self.__artist_Name

    def get_genre(self):
        return self.__genre
