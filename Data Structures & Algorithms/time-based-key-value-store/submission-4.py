from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        if len(values) < 1:
            return ""
        left = 0
        right = len(values) - 1
        ans = ""
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                left = mid + 1
                ans = values[mid][1]
            else:
                right = mid - 1
        return ans

        
