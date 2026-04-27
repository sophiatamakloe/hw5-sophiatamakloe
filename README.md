# Homework 5 – Timezone Meeting Planner

## Project Overview

This project solves a common global business problem: scheduling meetings across multiple time zones.

Instead of manually checking clocks in different cities, this planner automatically compares working-hour overlap and recommends the best meeting time.

The tool is useful for remote teams, international clients, consulting firms, and distributed organizations.

---

## What Makes This Project Interesting

Many teams waste time coordinating schedules across countries.

This planner improves that process by:

- Comparing multiple cities at once
- Translating hours across time zones
- Prioritizing business-hour availability
- Recommending the strongest overlap window

This turns a simple time conversion task into a practical scheduling assistant.

---

## Cities Included

- New York
- London
- Tokyo
- Los Angeles
- Dubai
- Sydney

---

## How It Works

The program:

1. Tests multiple meeting hours during the workday  
2. Converts each hour into local time for every city  
3. Checks whether each city falls within business hours (8 AM – 6 PM)  
4. Scores each possible meeting time  
5. Recommends the highest-scoring option

---

## Example Output

```text
Timezone Meeting Planner
------------------------------
Best meeting time in New York: 9:00

New York: 9:00
London: 14:00
Tokyo: 22:00
Los Angeles: 6:00
Dubai: 17:00
Sydney: 23:00
