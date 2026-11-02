pizza_saya = ["pepperoni", "pecinta daging", "keju"]
pizza_teman = pizza_saya[:]

pizza_saya.append("hawaiian")
pizza_teman.append("sayuran")

print("Pizza favorit saya adalah:")
for pizza in pizza_saya:
    print(pizza)

print("\nPizza favorit teman saya adalah:")
for pizza in pizza_teman:
    print(pizza)