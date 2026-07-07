class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        l = list(zip(position, speed))
        l.sort(reverse = True)
        stack = []
        for car in l:
            time = (target - car[0]) / car[1]
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)

        return len(stack)