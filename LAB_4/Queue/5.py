class Solution:
    def movesToStamp(self, stamp: str, target: str):
        n, m = len(target), len(stamp)
        s = list(target)
        result = []
        visited = [False] * n
        steps = 0
        def can_stamp(i):
            for j in range(m):
                if s[i + j] != '?' and s[i + j] != stamp[j]:
                    return False
            return True
        def stamp_at(i):
            for j in range(m):
                s[i + j] = '?'
            result.append(i)
        while steps < 10 * n:
            steps += 1
            progress = False
            for i in range(n - m + 1):
                if not visited[i] and can_stamp(i):
                    stamp_at(i)
                    visited[i] = True
                    progress = True
            if ''.join(s) == '?' * n:
                return result[::-1]
            if not progress:
                return []
        return []
solution = Solution()
print(solution.movesToStamp("abc", "ababc"))
print(solution.movesToStamp("abca", "aabcaca"))
