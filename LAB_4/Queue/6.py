class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        window = []
        for i in range(len(nums)):
            if window and window[0] < i - k + 1:
                window.pop(0)
            while window and nums[window[-1]] < nums[i]:
                window.pop()
            window.append(i)
            if i >= k - 1:
                result.append(nums[window[0]])
        return result

solution = Solution()
print(solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(solution.maxSlidingWindow([1], 1))
