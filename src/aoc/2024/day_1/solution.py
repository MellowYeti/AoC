from collections import defaultdict
from pathlib import Path
from typing import Generator


class Solution:
    def __init__(self):
        self.input_path = Path(__file__).parent.joinpath(Path("input.txt"))

    def silver(self, input_feed: Generator):
        left = list()
        right = list()

        for line in input_feed:
            left_value, right_value = line.split()
            left.append(int(left_value))
            right.append(int(right_value))

        left.sort()
        right.sort()

        total_distance = 0
        while len(left):
            total_distance += abs(left.pop(0) - right.pop(0))

        return total_distance

    def gold(self, input_feed: Generator):
        left = list()
        right = list()

        for line in input_feed:
            left_value, right_value = line.split()

            left.append(int(left_value))
            right.append(int(right_value))

        frequencies: defaultdict = defaultdict(int)

        for element in right:
            frequencies[element] += 1

        total_similarity = 0

        while len(left):
            index = left.pop(0)

            if not frequencies.get(index):
                continue

            total_similarity += index * frequencies[index]

        return total_similarity
