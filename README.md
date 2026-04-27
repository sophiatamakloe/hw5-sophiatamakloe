# Homework 5 – Timezone Meeting Planner

## Project Overview

This project solves a real business problem: scheduling meetings across global teams in different time zones.

Instead of manually comparing clocks across cities, the planner automatically evaluates multiple meeting hours and recommends the best time with the strongest business-hour overlap.

This is useful for:

- Remote teams
- International clients
- Consulting firms
- Global project managers
- Distributed organizations

---

## What Makes This Project Interesting

Many scheduling tools only convert time zones.

This planner goes further by:

- Comparing multiple cities at once
- Scoring candidate meeting times
- Prioritizing business-hour availability
- Recommending the optimal meeting window
- Presenting clean readable output

This turns time conversion into a lightweight decision-support tool.

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
4. Scores each meeting option  
5. Selects the highest-scoring time  
6. Displays all participant local times

---

## Improvements Made Through Iteration

After testing the first version, I improved the project by:

- Upgrading output formatting
- Adding clearer labels
- Showing participant local times
- Adding reasoning for recommendation
- Improving readability for real users

This demonstrates learning through evaluation and refinement.

---

## How to Run

1. Open Terminal  
2. Navigate to the repository folder  
3. Run:

```bash
python3 .agents/skills/timezone-meeting-planner/scripts/planner.py

Open terminal inside the repository folder and run:

```bash
python3 .agents/skills/timezone-meeting-planner/scripts/planner.py
