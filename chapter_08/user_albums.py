while True:
    artist_name = input("Write album's artist: ")
    if artist_name == 'q':
        break
    album_title = input("Write album's title: ")
    if album_title == 'q':
        break
    if artist_name and album_title:
        break

def make_album(artist_name, album_title, number_of_songs=None):
    album = {
        'artist_name': artist_name,
        'album_title': album_title,
    }
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album

if artist_name != 'q' and album_title != 'q':
    print(make_album(artist_name, album_title))
