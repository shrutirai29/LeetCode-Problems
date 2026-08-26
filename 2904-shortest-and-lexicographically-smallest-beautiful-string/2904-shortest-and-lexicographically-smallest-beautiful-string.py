class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        # Store positions of all 1s
        ones = [i for i, ch in enumerate(s) if ch == '1']

        # Not enough 1s
        if len(ones) < k:
            return ""

        ans = ""

        # Consider every group of k consecutive 1s
        for i in range(len(ones) - k + 1):
            start = ones[i]
            end = ones[i + k - 1]

            curr = s[start:end + 1]

            # Choose shortest, and lexicographically smallest on tie
            if not ans or len(curr) < len(ans) or (
                len(curr) == len(ans) and curr < ans
            ):
                ans = curr

        return ans