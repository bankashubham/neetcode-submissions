class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, windowCount = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            windowCount[ord(s2[i]) - ord('a')] += 1

        if s1Count == windowCount:
            return True
        
        left = 0

        # Slide the window
        for right in range(len(s1), len(s2)):

            # Add new character
            windowCount[ord(s2[right]) - ord('a')] += 1

            # Remove left character
            windowCount[ord(s2[left]) - ord('a')] -= 1

            left += 1

            # Compare frequency arrays
            if s1Count == windowCount:
                return True

        return False