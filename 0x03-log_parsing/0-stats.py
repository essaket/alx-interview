#!/usr/bin/python3
"""0. Log parsing"""
import sys

# Initialize counters and storage
total_file_size = 0
line_counter = 0
status_code_counts = {
        str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}


def print_stats():
    """Print the total file size and the count of each status code."""
    print(f"File size: {total_file_size}")
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")


try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) < 7:
            continue

        file_size = parts[-1]
        status_code = parts[-2]

        try:
            total_file_size += int(file_size)
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
        except ValueError:
            continue

        line_counter += 1
        if line_counter == 10:
            print_stats()
            line_counter = 0

except KeyboardInterrupt:
    pass
finally:
    print_stats()
