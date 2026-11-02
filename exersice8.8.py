def make_album(artist_name, album_title, number_of_songs=None):
    album = {'artist': artist_name, 'title': album_title}
    if number_of_songs:
        album['songs'] = number_of_songs
    return album

print("Masukkan informasi album musik Anda.")
print("(Ketik 'q' kapan saja untuk keluar)\n")

while True:
    artist = input("Nama Artis: ")
    if artist.lower() == 'q':
        break
        
    title = input("Judul Album: ")
    if title.lower() == 'q':
        break
        
    # Memanggil fungsi make_album dan mencetak hasilnya
    album_dict = make_album(artist, title)
    print("\nAlbum yang dibuat:")
    print(album_dict)
    print("\n--- Masukkan data berikutnya atau ketik 'q' untuk keluar ---")