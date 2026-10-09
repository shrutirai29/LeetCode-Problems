class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        need = 0

        for ch in s:
            if ch == '(':
                need += 2

                # If need is odd, we have one unmatched ')'
                # that needs another ')' before this '('.
                if need % 2 == 1:
                    ans += 1
                    need -= 1

            else:
                need -= 1

                # Too many ')'
                if need < 0:
                    ans += 1
                    need = 1

        # Add missing ')' characters
        ans += need

        return ans