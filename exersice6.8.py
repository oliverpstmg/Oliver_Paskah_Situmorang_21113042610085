pet_1 = {'kind': 'kucing', 'owner': 'ani'}
pet_2 = {'kind': 'anjing', 'owner': 'budi'}
pet_3 = {'kind': 'burung', 'owner': 'citra'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"Jenis Hewan: {pet['kind'].title()}")
    print(f"Pemilik    : {pet['owner'].title()}\n")