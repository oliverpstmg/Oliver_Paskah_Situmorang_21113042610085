favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_people = ['jen', 'budi', 'sarah', 'andi', 'edward']

for person in poll_people:
    if person in favorite_languages.keys():
        print(f"Terima kasih {person.title()}, karena telah berpartisipasi dalam jajak pendapat!")
    else:
        print(f"Halo {person.title()}, kami mengundang Anda untuk mengikuti jajak pendapat bahasa favorit kami.")