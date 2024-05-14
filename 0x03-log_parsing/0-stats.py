#!/usr/bin/python3
"""
Pyhton script
"""


import sys
from collections import defaultdict

# Initialize variables
total_file_size = 0
status_code_count = defaultdict(int)
line_count = 0

try:
    # Read stdin line by line
    for line in sys.stdin:
        # Split the line by space
        parts = line.split()

        # Check if the line follows the required format
        if len(parts) == 7 and parts[2] == "GET" and \
            parts[3].startswith("/projects/") and \
                parts[5].isdigit():
            # Extract file size and status code
            file_size = int(parts[6])
            status_code = int(parts[5])

            # Update total file size
            total_file_size += file_size

            # Update status code count
            status_code_count[status_code] += 1

            # Increment line count
            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print("Total file size:", total_file_size)
                for code in sorted(status_code_count.keys()):
                    print(f"{code}: {status_code_count[code]}")
                print()

except KeyboardInterrupt:
    # Handle keyboard interruption
    print("Total file size:", total_file_size)
    for code in sorted(status_code_count.keys()):
        print(f"{code}: {status_code_count[code]}")
