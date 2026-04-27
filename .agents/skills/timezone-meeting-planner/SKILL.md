---
name: timezone-meeting-planner
description: Converts meeting times across cities, finds overlap windows, and recommends the best business-hour meeting time. Use when scheduling across multiple time zones.
---

# Timezone Meeting Planner

## When to use

Use this skill when a user needs to schedule meetings across multiple countries or cities.

Examples:
- New York + London + Tokyo meeting
- Convert 3 PM EST to global times
- Find overlap for remote teams

## When not to use

- Single-city scheduling
- Calendar booking
- Sending invites

## Expected Inputs

- Base city
- Base meeting time
- Other cities to compare

## Steps

1. Read the input cities and meeting time.
2. Run the planner script.
3. Convert all times accurately.
4. Identify normal business-hour overlaps.
5. Recommend best meeting slot.

## Output Format

- Converted times by city
- Best meeting option
- Warnings for late/night hours

## Limitations

- Uses current timezone rules
- Does not book calendar invites
