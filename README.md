# Homework 5 – Timezone Meeting Planner

## Project Overview

This project solves a real business problem: scheduling meetings across global teams operating in different time zones.

Instead of manually comparing clocks across cities, the planner automatically evaluates multiple meeting hours and recommends the best time based on business-hour overlap.

This tool is useful for organizations that coordinate work internationally and need faster scheduling decisions.

---

## What Makes This Project Interesting

Many scheduling tools only convert time zones.

This planner goes further by:

- Comparing multiple cities at once  
- Testing several possible meeting times  
- Prioritizing business-hour availability  
- Scoring each candidate time slot  
- Recommending the strongest overlap window  
- Presenting clean, readable output  

This turns simple time conversion into a lightweight decision-support tool.

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
5. Selects the highest-scoring option  
6. Displays participant local times  
7. Explains why the recommendation was chosen  

---

## Improvements Made Through Iteration

After evaluating the first version, I improved the project by:

- Upgrading output formatting  
- Adding clearer labels  
- Showing participant local times  
- Adding reasoning for the recommendation  
- Improving readability for real users  
- Refining the project based on feedback  

This demonstrates learning through evaluation and iteration.

---

## How to Run

Open Terminal inside the repository folder and run:

```bash
python3 .agents/skills/timezone-meeting-planner/scripts/planner.py


Timezone Meeting Planner
------------------------------
Recommended Best Meeting Time

Base City: New York
Optimal Hour: 8:00

Participant Times
------------------------------
New York: 8:00
London: 13:00
Tokyo: 21:00
Los Angeles: 5:00
Dubai: 16:00
Sydney: 22:00

Reason: Maximizes business-hour overlap.

## Walkthrough Video

https://youtu.be/KpHWrefHCYE
