person_1 = {
    'first_name': 'Budi',
    'last_name': 'Santoso',
    'age': 20,
    'city': 'Surakarta'
}

person_2 = {
    'first_name': 'Siti',
    'last_name': 'Rahma',
    'age': 19,
    'city': 'Yogyakarta'
}

person_3 = {
    'first_name': 'Joko',
    'last_name': 'Widodo',
    'age': 22,
    'city': 'Bandung'
}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"Nama: {full_name}")
    print(f"Usia: {person['age']} tahun")
    print(f"Kota: {person['city']}\n")