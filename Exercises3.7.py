guests = ["B.J. Habibie", "My Father", "Ed sheran","My Mother","Ir.Soekarno","D.N Aidit"]

print("Mohon maaf, meja baru tidak tiba tepat waktu. Saya hanya bisa mengundang dua orang.")

# Menghapus tamu satu per satu menggunakan pop()
popped_guest = guests.pop(0)
print("Maaf " + popped_guest + ", Anda tidak bisa diundang karena keterbatasan tempat.")

popped_guest = guests.pop(4)
print("Maaf " + popped_guest + ", Anda tidak bisa diundang karena keterbatasan tempat.")

popped_guest = guests.pop(3)
print("Maaf " + popped_guest + ", Anda tidak bisa diundang karena keterbatasan tempat.")

popped_guest = guests.pop(2)
print("Maaf " + popped_guest + ", Anda tidak bisa diundang karena keterbatasan tempat.")

# Dua orang yang tersisa
print("\nHalo " + guests[1] + ", Anda masih diundang untuk makan malam.")
print("Halo " + guests[0] + ", Anda masih diundang untuk makan malam.")

# Menghapus dua nama terakhir menggunakan del
del guests[0]
del guests[0]

# Memastikan list kosong
print("\nIsi akhir list tamu:", guests)