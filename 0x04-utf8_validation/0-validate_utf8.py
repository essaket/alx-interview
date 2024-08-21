#!/usr/bin/python3
"""0. UTF-8 Validation"""


def validUTF8(data):
    """A method that determines if a given data set represents
       a valid UTF-8 encoding"""
    number_bytes = 0

    # Masks to check the most significant bits of a byte
    mask_1 = 1 << 7  # 10000000
    mask_2 = 1 << 6  # 01000000

    for i in data:
        mask_byte = 1 << 7  # Start with the first bit

        if number_bytes == 0:
            # Count leading 1s to determine the number of bytes
            while mask_byte & i:
                number_bytes += 1
                mask_byte >>= 1

            # 1-byte character or invalid byte count
            if number_bytes == 0:
                continue
            if number_bytes == 1 or number_bytes > 4:
                return False
        else:
            # Check if the byte is of the form 10xxxxxx
            if not (i & mask_1 and not (i & mask_2)):
                return False

        number_bytes -= 1

    return number_bytes == 0  # All bytes should be processed
