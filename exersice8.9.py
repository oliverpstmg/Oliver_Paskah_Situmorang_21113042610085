def show_messages(messages):
    """Menampilkan setiap pesan dalam daftar."""
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    """Mencetak pesan dan memindahkannya ke daftar sent_messages."""
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim pesan: {current_message}")
        sent_messages.append(current_message)

