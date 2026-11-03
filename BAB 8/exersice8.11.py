def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)

text_messages = [
    "Halo, jadwal kuliah TI dimajukan jam 8.",
    "Jangan lupa kumpulkan tugas praktikum.",
    "Meeting kelompok fix jam 3 sore."
]
sent_messages = []

# Mengirim salinan daftar (menggunakan irisan / slicing [:] )
send_messages(text_messages[:], sent_messages)

print("\n--- Memeriksa Daftar Setelah Fungsi Dijalankan ---")
print(f"Daftar asli masih utuh: {text_messages}")
print(f"Daftar terkirim berisi: {sent_messages}")