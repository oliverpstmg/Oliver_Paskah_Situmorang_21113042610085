filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

print("--- Membaca dan mengganti kata 'Python' dengan 'C' ---")
for line in lines:
    # Mengganti kata 'Python' menjadi 'C'
    modified_line = line.replace('Python', 'C')
    print(modified_line.strip())