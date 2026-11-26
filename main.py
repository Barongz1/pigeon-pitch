"""Pigeon Pitch, One Line — entry for make.fun.

Writes one line to /output/entry.txt.
"""
import os

# The pitch: a city pigeon sells investors a seed-to-sidewalk lunch platform — and asks for breadcrumbs.
TEXT = "We're disrupting urban lunch with a seed-to-sidewalk platform: zero warehouses, a million rooftops, and a flock that never misses a crumb. Seed round: breadcrumbs."

def write_entry():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

def main():
    write_entry()

if __name__ == "__main__":
    main()
