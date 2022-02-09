class ArtistsAndAlbums:
    def __init__(self, artist_id, album_id):
        self.__artist_id = artist_id
        self.__album_id = album_id

    def get_artist_id(self):
        return self.__artist_id

    def get_album_id(self):
        return self.__album_id
