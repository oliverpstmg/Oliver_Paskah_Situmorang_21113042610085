def make_album(artist_name, album_title, number_of_songs=None):
    """Membangun dictionary yang mendeskripsikan album musik."""
    album = {
        'artist': artist_name,
        'title': album_title
    }
    if number_of_songs:
        album['songs'] = number_of_songs
    return album

# Membuat tiga album berbeda
album1 = make_album('Tulus', 'Manusia')
album2 = make_album('Noah', 'Keterkaitan Keterikatan')
album3 = make_album('Sheila on 7', 'Kisahnya Klasik', 14) # Menyertakan jumlah lagu

print(album1)
print(album2)
print(album3)