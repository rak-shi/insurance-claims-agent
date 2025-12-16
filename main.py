import sys
import json
from extractor import extract_fields
from validator import find_missing_fields
from router import route_claim

def run(path):
    fields = extract_fields(path)
    missing = find_missing_fields(fields)
    route, reason = route_claim(fields, missing)

    print(json.dumps({
        "extractedFields": fields,
        "missingFields": missing,
        "recommendedRoute": route,
        "reasoning": reason
    }, indent=2))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <fnol.pdf | fnol.txt>")
    else:
        run(sys.argv[1])
