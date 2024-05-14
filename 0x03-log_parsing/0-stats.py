#!/usr/bin/python3
"""
Pyhton script
"""


import sys
import signal


# Helper function to handle signals
def signal_handler(sig, frame):
    # Print statistics and exit when CTRL+C is detected
    print_statistics()
    sys.exit(0)


# Register signal handler for interrupt signal
signal.signal(signal.SIGINT, signal_handler)


# Function to print the collected statistics
def print_statistics():
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


# Initialize variables
total_file_size = 0
status_codes = {str(code): 0 for code in [
    200, 301, 400, 401, 403, 404, 405, 500
    ]}
line_count = 0

try:
    # Process each line from stdin
    for line in sys.stdin:
        parts = line.strip().split('"')
        if len(parts) < 2 or "GET /projects/260 HTTP/1.1" not in parts[1]:
            continue  # Skip lines that don't match the specified format

        # Extract status code and file size
        parts = parts[-1].split()
        status_code, file_size = parts[0], parts[-1]

        # Update status codes count and total file size
        if status_code in status_codes:
            status_codes[status_code] += 1
        total_file_size += int(file_size)

        # Increment line counter
        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interrupt (CTRL+C)
    print_statistics()
