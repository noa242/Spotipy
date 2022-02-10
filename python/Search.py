from python.CsvToStack import CsvToStack
from python.Artists import Artists


def get_artists():
    csv_read = CsvToStack('info/Artists.csv')
    artists_stack = csv_read.read_scv()
    for artist in artists_stack:
        count = 0
        for value in artist:
            count += 1
            if count == 2:
                print(value)


def get_albums(artist_id):
    csv_read_bond = CsvToStack('info/ArtistsAndAlbums.csv')
    artist_albums_stack = csv_read_bond.read_scv()
    csv_read_albums = CsvToStack('info/Albums.csv')
    albums_stack = csv_read_albums.read_scv()
    for bond in artist_albums_stack:
        if bond[0] == artist_id:
            for album in albums_stack:
                if album[0] == bond[1]:
                    album[0]: bytes
                    # what = str(album[1], 'ascii')
                    # what = bytes(album[1], 'ascii')
                    # what = bytes(album[1], 'utf-8')
                    # vprint(what)
                    print(album[1].decode())
                    pass


def get_top_10_songs(artist_id):
    csv_read_bond = CsvToStack('info/ArtistsAndAlbums.csv')
    artist_albums_stack = csv_read_bond.read_scv()
    playlist_id = ""
    for bond in artist_albums_stack:
        if bond[0] == artist_id:
            return 1


def get_all_songs(album_id):
    top_ten = ()
    csv_Songs = CsvToStack('info/Songs.csv')
    songs_stack = csv_Songs.read_scv()
    max_pop = 0
    count = 0
    min_pop = 100
    for song in songs_stack:
        if song[2] == album_id:
            if count < 10:
                if (int(song[3]) > max_pop):
                    max_pop = song[3]
                    top_ten[count] = song
                if (song[3] <= min_pop):
                    min_pop = song[3]
            else:
                if (song[3] > min_pop):
                    for top_song in top_ten:
                        if top_song == min_pop:
                            top_song = song
                    for top_song in top_ten:
                        if (top_song < min_pop):
                            min_pop = top_song[3]

    print(top_ten)


def main():
    # get_albums('39jFFncu6W0phhYK16Dp9g')
    get_all_songs('6UornBmu7FEPziehukocoq')


if __name__ == '__main__': main()
