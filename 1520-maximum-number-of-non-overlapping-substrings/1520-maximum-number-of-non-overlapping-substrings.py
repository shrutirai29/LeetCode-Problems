class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        n = len(s)
        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence of each character
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Generate valid substrings
        for c in range(26):
            if last[c] == -1:
                continue

            l = first[c]
            r = last[c]
            valid = True
            i = l

            while i <= r:
                x = ord(s[i]) - ord('a')

                if first[x] < l:
                    valid = False
                    break

                r = max(r, last[x])
                i += 1

            if valid:
                intervals.append((l, r))

        # Greedy: choose intervals ending earliest
        intervals.sort(key=lambda x: (x[1], -x[0]))

        ans = []
        prev_end = -1

        for l, r in intervals:
            if l > prev_end:
                ans.append(s[l:r + 1])
                prev_end = r

        return ans