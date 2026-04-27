cities = {
    "New York": -4,
    "London": 1,
    "Tokyo": 9,
    "Los Angeles": -7,
    "Dubai": 4,
    "Sydney": 10
}

base_city = "New York"

print("Timezone Meeting Planner")
print("-" * 30)

best_hour = None
best_score = -1

for hour in range(8, 18):
    score = 0

    for city, offset in cities.items():
        local_hour = hour + (offset - cities[base_city])

        if local_hour < 0:
            local_hour += 24
        elif local_hour >= 24:
            local_hour -= 24

        if 8 <= local_hour <= 18:
            score += 1

    if score > best_score:
        best_score = score
        best_hour = hour

print(f"Best meeting time in {base_city}: {best_hour}:00")
print()

for city, offset in cities.items():
    local_hour = best_hour + (offset - cities[base_city])

    if local_hour < 0:
        local_hour += 24
    elif local_hour >= 24:
        local_hour -= 24

    print(f"{city}: {local_hour}:00")
