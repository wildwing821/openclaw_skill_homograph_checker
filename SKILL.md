# Homograph Checker (homograph_checker)

## Description
Analyzes domains for potential homograph (IDN) spoofing attacks. Identifies mixed script usage (e.g., Cyrillic 'a' vs Latin 'a') which often signals a phishing attempt.

## Location
/app/.openclaw/workspace/skills/homograph_checker/

## Usage
python3 /app/.openclaw/workspace/skills/homograph_checker/checker.py

## Integration
- Use this skill before navigating to any new URL via `browser`.
- Use this skill before performing `web_fetch` on suspicious URLs.
- If the risk assessment is 'HIGH', notify the user immediately and do not proceed.
