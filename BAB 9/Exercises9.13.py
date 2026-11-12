from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

# Membuat dadu 6 sisi dan melemparnya 10 kali
print("--- Lemparan Dadu 6 Sisi (10 kali) ---")
d6 = Die()
results_6 = [d6.roll_die() for _ in range(10)]
print(results_6)

# Membuat dadu 10 sisi dan melemparnya 10 kali
print("\n--- Lemparan Dadu 10 Sisi (10 kali) ---")
d10 = Die(10)
results_10 = [d10.roll_die() for _ in range(10)]
print(results_10)

# Membuat dadu 20 sisi dan melemparnya 10 kali
print("\n--- Lemparan Dadu 20 Sisi (10 kali) ---")
d20 = Die(20)
results_20 = [d20.roll_die() for _ in range(10)]
print(results_20)