#!/usr/bin/env python3

import re


def compress(input: str) -> str:
    output = ""
    begin = input[0]
    occurences = 0
    for index, char in enumerate(input):
        if char != begin or index == len(input)-1:
            if index == len(input)-1 and begin == char:
                occurences += 1

            if occurences > 3:
                output += begin + '#' + str(occurences)
            else:
                output += begin * occurences

            if index == len(input)-1 and begin != char:
                output += char

            begin = char
            occurences = 1

        else:
            occurences += 1

    return output


def decompress(input: str) -> str:
    matches = re.findall(r'(.#\d+)', input)
    decompressed = input
    for match in matches:
        char = re.match(r'(.)#\d+', match)
        times = re.search(r'(\d+)', match)

        replacement = char.group(1) * int(times.group(1))
        decompressed = decompressed.replace(match, replacement)

    return decompressed



