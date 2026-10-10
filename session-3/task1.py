songs = {
    "Vhalam Aavo Ne": "4:15",
    "Moj Ma Revu": "3:45",
    "Gori Radha Ne Kalo Kaan": "4:30",
    "Daldu Lagyu": "4:10"
}


def get_song_duration(song_name):
    try:
        return songs[song_name]
    except KeyError:
        print("Song not found on Spotify!")


song = input("Enter song name: ")
duration = get_song_duration(song)

if duration:
    print("Duration:", duration)