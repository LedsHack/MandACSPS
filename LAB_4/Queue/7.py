class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dp = [float('-inf')] * n
        dp[0] = nums[0]
        for i in range(1, n):
            for j in range(max(0, i - k), i):
                dp[i] = max(dp[i], dp[j] + nums[i])
        return max(dp)
solution = Solution()
print(solution.maxSum([10, 2, -10, 5, 20], 2))
print(solution.maxSum([-1, -2, -3], 1))
print(solution.maxSum([10, -2, -10, -5, 20], 2))
