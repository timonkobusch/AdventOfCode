import re

def p1(lines):
    count = sum(1 for s in lines
                if len([x for x in s if x in "aeiou"]) > 2
                and not any(x in s for x in ["ab", "cd", "pq", "xy"])
                and re.search(r"([a-z])\1", s)
                )
    return count