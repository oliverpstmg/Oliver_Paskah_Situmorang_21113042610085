warehouse_inventory = {
    'mesin_cnc': {
        'lokasi': 'Zona A',
        'stok': 5,
        'status': 'Aktif Beroperasi',
        'pemeliharaan_terakhir': '12 Januari 2026'
    },
    'conveyor_belt': {
        'lokasi': 'Zona B',
        'stok': 12,
        'status': 'Dalam Perbaikan',
        'pemeliharaan_terakhir': '20 Februari 2026'
    },
    'forklift': {
        'lokasi': 'Zona C',
        'stok': 3,
        'status': 'Aktif Beroperasi',
        'pemeliharaan_terakhir': '01 Maret 2026'
    }
}

print("=== LAPORAN INVENTARIS GUDANG PABRIK ===")
for equipment, details in warehouse_inventory.items():
    print(f"\nPeralatan: {equipment.replace('_', ' ').upper()}")
    print(f"  - Lokasi Penyimpanan : {details['lokasi']}")
    print(f"  - Jumlah Unit        : {details['stok']} unit")
    print(f"  - Status Operasional : {details['status']}")
    print(f"  - Servis Terakhir    : {details['pemeliharaan_terakhir']}")
print("========================================")