from typing import Generator


class Solution:
    def _get_report_from_line(self, line: str) -> list:
        return [int(number) for number in line.split()]

    def _is_report_safe(self, report: list) -> bool:
        if report[0] > report[-1]:
            report.reverse()

        while len(report) > 1:
            delta = report[1] - report[0]

            if not 0 < delta < 4:
                return False

            report.pop(0)

        return True

    def silver(self, input_feed: Generator):
        safety_count = 0

        for line in input_feed:
            report = self._get_report_from_line(line)

            if not self._is_report_safe(report):
                continue

            safety_count += 1

        return safety_count

    def gold(self, input_feed: Generator):
        # Part two implementation goes here

        return "🤷"
