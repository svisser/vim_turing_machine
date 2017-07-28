"""Descodes a binary string to a json representation of the business's hours
after the  merge business hours turing machine has processed it. Reads json from
stdin and outputs the initial tape."""
import json
import sys

from vim_turing_machine.constants import BLANK_CHARACTER


def decode_hours(hours, num_bits=5):
    result = []
    clean_hours = hours.replace(BLANK_CHARACTER, '')
    index = 0
    while index < len(clean_hours):
        begin = clean_hours[index:index+num_bits]
        begin = int(begin, 2)
        index += num_bits
        end = clean_hours[index:index+num_bits]
        end = int(end, 2)
        index += num_bits
        result.append([begin, end])

    return result