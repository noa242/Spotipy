import os
import csv
import itertools
from python.User.User import User
from python.User.playlists import Playlists
from python.CsvToStack import CsvToStack
from python.User.PlayListSongs import PlaylistSongs

class UserPlaylists:
    def __init__(self, user_id, playlist_name=''):
        self.__user_id = user_id
        self.__playlist_name = playlist_name

    def __init__(self, user_id):
        self.__user_id = user_id

    def create_playlist(self):
        path = "../info/playlists.csv"
        if not os.path.exists(path):
            with open(path, 'w', newline='') as empty_csv:
                pass

        playlist_name = input("please enter your playlist_name: ")
        csv_to_stack = CsvToStack(path)
        playlists_stack = csv_to_stack.read_scv()
        if len(playlists_stack) != 0:
            for one_playlist in playlists_stack:
                if one_playlist[0] == playlist_name:
                    print('sorry, this name is already exists')
                    return 0

        else:
            playlist = Playlists(playlist_name, self.__user_id)
            file = open(path, 'w', newline='')
            write = csv.writer(file)
            write.writerow([playlist.name(), playlist.user_id()])
            print(f'playlist: {playlist_name} was added successfully')

    def get_all_songs(self):
        path = "../songs"
        file = open(path, 'r')

    def add_song(self, song_id):
        path = "../info/playlistSongs.csv"
        if not os.path.exists(path):
            with open(path, 'w', newline='') as empty_csv:
                pass
        play_list_song = PlaylistSongs(self.__playlist_name, song_id)
        file = open(path, 'w', newline='')
        write = csv.writer(file)
        write.writerow([play_list_song.name(), play_list_song.song_id()])
        print(f'your song was added successfully to playlist: {self.__playlist_name}')

    def set_playlist_name(self, playlist_name):
        self.__playlist_name = playlist_name


def main():
    user_play_list = UserPlaylists(1)
    user_play_list.create_playlist()


if __name__ == '__main__': main()
