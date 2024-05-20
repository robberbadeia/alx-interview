#!/usr/bin/python3
"""
script that determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Function implementation
    """
    num_bytes = 0

    # Masks to check the bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        # Mask the byte to get only the 8 least significant bits
        byte = byte & 255

        # If this is the start of a new UTF-8 character
        if num_bytes == 0:
            # Determine how many bytes the current UTF-8 character requires
            if (byte & mask1) == 0:
                continue  # 1-byte character (0xxxxxxx)
            while (byte & mask1) != 0:
                num_bytes += 1
                byte = byte << 1

            # UTF-8 supports up to 4 bytes per character
            if num_bytes == 1 or num_bytes > 4:
                return False

            # Reduce num_bytes by 1 to account for the current byte
            num_bytes -= 1

        else:
            # If it's a continuing byte, it must be of the form 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

            # Decrease the number count
            num_bytes -= 1

    # All following bytes should complete the character (num_bytes should be 0)
    return num_bytes == 0
