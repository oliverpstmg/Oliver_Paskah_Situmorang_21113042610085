rivers = {
    'nile': 'mesir',
    'amazon': 'brasil',
    'yangtze': 'china'
}

# 1. Mencetak kalimat tentang setiap sungai
for river, country in rivers.items():
    print(f"Sungai {river.title()} mengalir melalui negara {country.title()}.")

print("\n--- Daftar Sungai ---")
# 2. Mencetak nama setiap sungai
for river in rivers.keys():
    print(f"- {river.title()}")

print("\n--- Daftar Negara ---")
# 3. Mencetak nama setiap negara
for country in rivers.values():
    print(f"- {country.title()}")