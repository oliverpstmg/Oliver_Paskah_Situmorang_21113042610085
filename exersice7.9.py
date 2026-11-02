sandwich_orders = [
    'pastrami', 'tuna', 'chicken', 'pastrami', 
    'roast beef', 'egg salad', 'pastrami'
]
finished_sandwiches = []

print("Maaf, kedai kami sedang kehabisan pastrami hari ini.\n")

# Menghapus semua kemunculan 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Memproses pesanan tersisa
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya telah membuatkan {current_sandwich} sandwich Anda.")
    finished_sandwiches.append(current_sandwich)

print("\n--- Daftar Sandwich yang Selesai Dibuat ---")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")