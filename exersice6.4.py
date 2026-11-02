glossary = {
    'dictionary': 'Kumpulan pasangan kunci-nilai dalam Python.',
    'string': 'Deretan karakter yang diapit oleh tanda kutip.',
    'loop': 'Blok kode yang berjalan berulang kali.',
    'list': 'Kumpulan item dalam urutan tertentu.',
    'key': 'Nama unik untuk mengakses nilai dalam dictionary.',
    'integer': 'Tipe data untuk bilangan bulat.',
    'float': 'Tipe data untuk bilangan desimal.',
    'boolean': 'Nilai kebenaran yang bernilai True atau False.',
    'tuple': 'Kumpulan item yang tidak dapat diubah (immutable).',
    'set': 'Kumpulan item unik tanpa duplikat.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}:\n\t{meaning}\n")