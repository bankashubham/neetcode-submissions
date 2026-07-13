class CountSquares:

    def __init__(self):
        self.points = Counter()

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        x, y = point
        ans = 0

        for (px, py), cnt in self.points.items():

            # Must be a valid diagonal
            if abs(px - x) != abs(py - y) or px == x:
                continue

            ans += (
                cnt *
                self.points[(px, y)] *
                self.points[(x, py)]
            )

        return ans
        
