cities = {
    "New York": -4,
    "London": 1,
    "Tokyo": 9,
    "Los Angeles": -7,
    "Dubai": 4,
    "Sydney": 10
}

base_hour = 9

print("Timezone Meeting Planner")
print("-" * 30)

best_hour = None
best_score = -1

for hour in range(8, 18):
    score = 0

    for city, offset in cities.items():
        local = hour + (offset - cities["New York"])

        if 8 <= local <= 18:
            score += 1

    if score > best_score:
        best_score = score
        best_hour = hour

print(f"Best New York Time: {best_hour}:00")
print()

for city, offset in cities.items():
    local = best_hour + (offset - cities["New York"])
    print(f"{city}: {local}:00")
