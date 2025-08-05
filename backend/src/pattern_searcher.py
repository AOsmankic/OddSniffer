import json
import re
patterns = {}

def load_patterns():
    global patterns
    with open("config/secret_patterns.json", "r") as f:
        patterns = json.load(f)
        f.close()


def does_string_match_any_pattern(test_string: str):
    if not patterns:
        load_patterns()
    for pattern in patterns:
        if re.match(pattern["pattern"], test_string):
            return (pattern["id"], pattern["description"])
    return None
