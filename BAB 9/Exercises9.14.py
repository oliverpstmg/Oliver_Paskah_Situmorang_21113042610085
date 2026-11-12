from random import choice

# Daftar berisi 10 angka dan 5 huruf
possibilities = [1, 3, 5, 7, 9, 0, 2, 4, 6, 8, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("Pemenang lotere dengan kombinasi 4 karakter berikut akan memenangkan hadiah:")

# Memilih 4 item unik secara acak
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)
    if pulled_item not in winning_ticket:
        winning_ticket.append(pulled_item)

print(winning_ticket)