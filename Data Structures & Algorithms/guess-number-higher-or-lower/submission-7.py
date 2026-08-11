class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            middle = left + (right - left) // 2
            chosen = guess(middle)

            if chosen == -1:
                # middle is higher than target
                right = middle - 1

            elif chosen == 1:
                # middle is lower than target
                left = middle + 1

            else:
                # middle == target
                return middle

        return -1