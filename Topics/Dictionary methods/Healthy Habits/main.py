all_walks = 0
days_number = 0

for walk in walks:
    all_walks += walk["distance"]
    days_number += 1

print(all_walks // days_number)