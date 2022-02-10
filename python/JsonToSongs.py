import os
import json
import csv
from python.songs import Songs
from python.Albums import Albums
from python.Artists import Artists
from python.ArtistsAndAlbums import ArtistsAndAlbums


def get_files(path):
    artists_stack = []
    albums_stack = []
    songs_stack = []
    artists_and_albums_stack = []
    for file in os.listdir(path):
        file_reader = open(path + '/' + file, 'r')
        data = json.loads(file_reader.read())
        class_transfer(artists_stack, albums_stack, songs_stack, artists_and_albums_stack, data)
        # print(artists_stack.pop().get_artist_id())
    artists_path = "Info/Artists.csv"
    albums_path = "Info/Albums.csv"
    songs_path = "Info/Songs.csv"
    art_and_alb_path = "Info/ArtistsAndAlbums.csv"
    add_to_file('artists', artists_path, artists_stack)
    add_to_file('albums', albums_path, albums_stack)
    add_to_file('songs', songs_path, songs_stack)
    add_to_file('art_and_alb', art_and_alb_path, artists_and_albums_stack)


def class_transfer(artists_stack, albums_stack, songs_stack, artists_and_albums, data):
    # print(data["track"]["artists"][0]["id"])
    artist = Artists(data["track"]["artists"][0]["id"], data["track"]["artists"][0]["name"])
    artists_stack.append(artist)

    album = Albums(data["track"]["album"]["id"], data["track"]["album"]["name"])
    albums_stack.append(album)

    song = Songs(data["track"]["id"], data["track"]["name"], data["track"]["album"]["id"], data["track"]["popularity"])
    songs_stack.append(song)

    art_and_alb = ArtistsAndAlbums(data["track"]["artists"][0]["id"], data["track"]["album"]["id"])
    artists_and_albums.append(art_and_alb)


def add_to_file(class_type, path, objects_stack):
    file = open(path, 'w', newline='')
    write = csv.writer(file)
    # write.writerows(objects_stack)
    if class_type == 'artists':
        for one_object in list(objects_stack):
            write.writerow([one_object.get_artist_id(), one_object.get_artist_name(), one_object.get_genre()])
    if class_type == 'albums':
        for one_object in list(objects_stack):
            # print(one_object.get_album_id(), '-->', one_object.get_album_name())
            # print(str(one_object.get_album_name()).encode('utf-8'))
            # print(str(one_object.get_album_name())[::1])
            write.writerow([one_object.get_album_id(), one_object.get_album_name().encode()])
    if class_type == 'songs':
        for one_object in list(objects_stack):
            write.writerow([one_object.get_song_id(), one_object.get_song_name(), str(one_object.get_album_id()),
                            one_object.get_popularity()])
    if class_type == 'art_and_alb':
        for one_object in list(objects_stack):
            write.writerow([one_object.get_artist_id(), one_object.get_album_id()])


def main():
        path: dir = "C:/NetanyaCollege/python/ma04-Spotipy/songs"
        get_files(path)


if __name__ == '__main__': main()
