from enum import Enum
from typing import Generator


class Direction(Enum):
    N = "n"
    NE = "ne"
    E = "e"
    SE = "se"
    S = "s"
    SW = "sw"
    W = "w"
    NW = "nw"


class Solution:
    def build_grid(self, input_feed: Generator):
        self._grid = [line.strip() for line in input_feed]

    def check_direction(
        self,
        position_x: int,
        position_y: int,
        letters: str,
        direction: Direction,
    ) -> bool:
        if not letters:
            return True

        if position_x < 0 or position_x >= len(self._grid[0]):
            return False

        if position_y < 0 or position_y >= len(self._grid):
            return False

        if self._grid[position_y][position_x] != letters[0]:
            return False

        next_x = position_x
        next_y = position_y

        if direction in {Direction.NE, Direction.E, Direction.SE}:
            next_x += 1

        if direction in {Direction.NW, Direction.W, Direction.SW}:
            next_x -= 1

        if direction in {Direction.NW, Direction.N, Direction.NE}:
            next_y -= 1

        if direction in {Direction.SW, Direction.S, Direction.SE}:
            next_y += 1

        return self.check_direction(next_x, next_y, letters[1:], direction)

    def silver(self, input_feed: Generator):
        self.build_grid(input_feed)
        count = 0
        for y, line in enumerate(self._grid):
            for x, _ in enumerate(line):
                for direction in Direction:
                    if self.check_direction(x, y, "XMAS", direction):
                        count += 1

        return count


    def gold(self, input_feed: Generator):
        self.build_grid(input_feed)
        grid_height = len(self._grid)
        grid_width = len(self._grid[0])

        count = 0
        for y in range(1, grid_height - 1):
            for x in range(1, grid_width - 1):
                if self.is_valid_pattern(x, y):
                    count += 1

        return count


    def is_valid_pattern(self, x, y):
        valid_patterns = {"MMASS", "SSAMM", "SMASM", "MSAMS"}
        check_str = "".join(
            [
                self._grid[y + 1][x - 1],
                self._grid[y + 1][x + 1],
                self._grid[y][x],
                self._grid[y - 1][x - 1],
                self._grid[y - 1][x + 1],
            ]
        )
        return check_str in valid_patterns
