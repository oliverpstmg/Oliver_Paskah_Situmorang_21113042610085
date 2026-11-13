def count_words(filename, word):
    """Menghitung perkiraan kemunculan suatu kata dalam file teks."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Maaf, file {filename} tidak ditemukan.")
    else:
        # 1. Menghitung kemunculan kata secara umum (termasuk di dalam kata lain seperti 'then')
        count_general = contents.lower().count(word)
        print(f"Kata '{word}' (umum) muncul sekitar {count_general} kali dalam {filename}.")
        
        # 2. Menghitung dengan menambahkan spasi di belakang ('the ') untuk hasil yang lebih akurat
        word_with_space = f"{word} "
        count_precise = contents.lower().count(word_with_space)
        print(f"Kata '{word_with_space}' (dengan spasi) muncul sekitar {count_precise} kali dalam {filename}.")

# Contoh pemanggilan fungsi (pastikan file teks sudah tersedia di direktori Anda)
filename = 'alice.txt'
count_words(filename, 'the')