class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        depth = 0
        ans = []

        for c in seq:
            if c == '(':
                depth += 1

            ans.append(depth % 2)

            if c == ')':
                depth -= 1

        return ans