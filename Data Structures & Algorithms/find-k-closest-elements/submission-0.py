class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        left = 0
        right = k - 1
        # First window
        min_distance = 0

        for i in range(k):
            min_distance += abs(arr[i] - x) #cause this is starting , makes sense #already in ascending order

        best_left = 0

        # Slide the window
        for right in range(k, n):
            current_distance = min_distance
            current_distance += abs(arr[right] - x)
            current_distance -= abs(arr[right - k] - x)

            if current_distance < min_distance:
                min_distance = current_distance
                best_left = right - k + 1

        return arr[best_left:best_left + k]