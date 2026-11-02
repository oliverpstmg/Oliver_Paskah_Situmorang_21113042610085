Places = ['Argentina', 'Belanda', 'Jepang', 'Prancis', 'Swis']

# KODE YANG MENYEBABKAN INDEX ERROR (Sengaja):
# List di atas hanya memiliki indeks 0, 1, dan 2. 
# Mengakses indeks 3 akan memicu IndexError.
# print(Places[5]) 

# PERBAIKAN (KODE YANG BENAR):
print(Places[4])