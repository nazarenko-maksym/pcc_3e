def make_album(artist_name, album_title, number_of_songs=None):
    album = {
        'artist_name': artist_name,
        'album_title': album_title,
    }

    if number_of_songs:
        album['number_of_songs'] = number_of_songs

    return album

print(make_album('kurt cobain', 'nevermind', 13))
print(make_album('amy lee', 'fallen'))
print(make_album('linkin part', 'meteora'))
