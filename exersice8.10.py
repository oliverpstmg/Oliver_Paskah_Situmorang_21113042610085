# Daftar pesan awal
text_messages = [
    "Halo, jadwal kuliah TI dimajukan jam 8.",
    "Jangan lupa kumpulkan tugas praktikum.",
    "Meeting kelompok fix jam 3 sore."
]
sent_messages = []

print("--- Pesan Asli (Sebelum Dikirim) ---")
show_messages(text_messages)

# Memproses pengiriman pesan
send_messages(text_messages, sent_messages)

print("\n--- Status Akhir Daftar ---")
print(f"Daftar pesan asli (messages): {text_messages}")
print(f"Daftar pesan terkirim (sent_messages): {sent_messages}")