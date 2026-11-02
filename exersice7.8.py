sandwich_orders = ['tuna', 'chicken', 'roast beef', 'egg salad']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"Saya telah membuatkan {current_sandwich} sandwich Anda.")
    finished_sandwiches.append(current_sandwich)

print("\n--- Daftar Sandwich yang Selesai Dibuat ---")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} sandwich")