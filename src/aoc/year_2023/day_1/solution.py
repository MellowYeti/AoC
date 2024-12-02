from itertools import filterfalse
from typing import Generator


class Solution:
    def silver(self, input_feed: Generator):
        calibration_total = 0

        for line in input_feed:
            numbers = [
                int(digit) for digit in filterfalse(lambda x: x.isalpha(), line.strip())
            ]
            calibration_value = (numbers[0] * 10) + numbers[-1]
            calibration_total += calibration_value

        return calibration_total

    def replace_words_for_digits(self, line):
        word_digit_map = {
            "one": "one1one",
            "two": "two2two",
            "three": "three3three",
            "four": "four4four",
            "five": "five5five",
            "six": "six6six",
            "seven": "seven7seven",
            "eight": "eight8eight",
            "nine": "nine9nine",
        }

        line = line.strip()

        for k, v in word_digit_map.items():
            line = line.replace(k, v)

        return line

    def gold(self, input_feed: Generator):
        calibration_total = 0

        for line in input_feed:
            numbers = [
                int(digit)
                for digit in filterfalse(
                    lambda x: x.isalpha(), self.replace_words_for_digits(line.strip())
                )
            ]
            calibration_value = (numbers[0] * 10) + numbers[-1]
            calibration_total += calibration_value

        return calibration_total

        return calibration_total
