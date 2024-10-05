import csv
import re
import pprint

# Define your keywords
keywords = ["engineering", "minority", "medical"]  # Replace with your keywords

# Read the CSV file and store scholarships
scholarships = []

with open('scholarships.csv', mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        scholarships.append(row)

# List to store matching scholarships

matching_scholarships = []

# Compile regular expressions for each keyword
keyword_patterns = [re.compile(keyword, re.IGNORECASE) for keyword in keywords]

for scholarship in scholarships:
    # Combine all values into a single string
    scholarship_text = ' '.join(scholarship.values())
    
    # Check if any keyword matches
    if any(pattern.search(scholarship_text) for pattern in keyword_patterns):
        matching_scholarships.append(scholarship)

# Output the matching scholarships
pprint.pprint(matching_scholarships)
