"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if item not in frequencies:
            frequencies[item] = 0
        frequencies[item] += 1
    return frequencies

print(frequencies(['a', 'a', 'b', 'b', 'b', 'c']))
print(frequencies([100, 'Hello', '100', '100', 100]))
