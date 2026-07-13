class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]

        left, right = 0, len(values) - 1
        answer = -1 
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][0] <= timestamp:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return "" if answer == -1 else values[answer][1]

        
