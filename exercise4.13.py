menu_buffet = ("nasi goreng", "sup ayam", "ikan bakar", "steak daging", "salad")

print("Menu asli:")
for makanan in menu_buffet:
    print(makanan)

# Baris ini akan menimbulkan TypeError jika di-uncomment:
# menu_buffet[0] = "mie goreng"

menu_buffet = ("nasi goreng", "sup ayam", "mie goreng", "steak daging", "burger")

print("\nMenu revisi:")
for makanan in menu_buffet:
    print(makanan)