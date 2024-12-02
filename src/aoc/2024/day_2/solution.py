from copy import copy
from itertools import pairwise
from typing import Generator


class Solution:
    def _get_report_from_line(self, line: str) -> list:
        return [int(number) for number in line.split()]

    def _is_report_safe(self, report: list) -> bool:
        if report[0] > report[-1]:
            report.reverse()

        for first, second in pairwise(report):
            delta = second - first

            if not 0 < delta < 4:
                return False

        return True

    def _is_dampened_report_safe(self, report: list) -> bool:
        if self._is_report_safe(report):
            return True

        for index, _ in enumerate(report):
            doctored = copy(report)
            doctored.pop(index)

            if self._is_report_safe(doctored):
                return True

        return False

    def silver(self, input_feed: Generator):
        safety_count = 0

        for line in input_feed:
            report = self._get_report_from_line(line)

            if not self._is_report_safe(report):
                continue

            safety_count += 1

        return safety_count

    def gold(self, input_feed: Generator):
        safety_count = 0

        for line in input_feed:
            report = self._get_report_from_line(line)

            if not self._is_dampened_report_safe(report):
                continue

            safety_count += 1

        return safety_count
