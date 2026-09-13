class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        points1 = []
        points2 = []

        # Store coordinates of all 1s
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    points1.append((r, c))
                if img2[r][c] == 1:
                    points2.append((r, c))

        count = {}
        ans = 0

        # Try aligning every 1 in img1 with every 1 in img2
        for r1, c1 in points1:
            for r2, c2 in points2:
                shift = (r2 - r1, c2 - c1)

                count[shift] = count.get(shift, 0) + 1
                ans = max(ans, count[shift])

        return ans