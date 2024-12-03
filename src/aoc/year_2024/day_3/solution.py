import re
from enum import Enum
from typing import Generator


class Solution:
    def silver(self, input_feed: Generator):
        regex = re.compile(r"mul\(\d+,\d+\)")
        instructions = list()
        mul_total = 0

        for line in input_feed:
            instructions.extend(regex.findall(line))

        for mul_instruction in instructions:
            trimmed_instruction = mul_instruction[4:-1]
            num1, num2 = trimmed_instruction.split(",")

            mul_total += int(num1) * int(num2)

        return mul_total

    def gold(self, input_feed: Generator):
        regex = re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)")
        instructions = list()
        mul_total = 0
        switch = True

        for line in input_feed:
            instructions.extend(regex.findall(line))

        for instruction in instructions:
            if instruction == "do()":
                switch = True
                continue

            if instruction == "don't()":
                switch = False
                continue

            if switch:
                trimmed = instruction[4:-1]
                num1, num2 = trimmed.split(",")
                mul_total += int(num1) * int(num2)

        return mul_total
