from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int,
                    queries: List[List[int]]) -> List[int]:

        n = len(nums)

        # Make segment tree size a power of 2
        size = 1
        while size < n:
            size *= 2

        # prod[node] = product of entire segment % k
        prod = [1 % k] * (2 * size)

        # cnt[r][node] =
        # number of non-empty prefixes of this segment
        # whose product % k == r
        cnt = [[0] * (2 * size) for _ in range(k)]

        # -------------------------
        # Build leaf nodes
        # -------------------------
        for i in range(n):
            p = nums[i] % k
            node = size + i

            prod[node] = p
            cnt[p][node] = 1

        # -------------------------
        # Merge function
        # -------------------------
        def pull(node):
            left = node * 2
            right = left + 1

            # Product of whole segment
            prod[node] = (prod[left] * prod[right]) % k

            # Start with all prefixes from left
            for r in range(k):
                cnt[r][node] = cnt[r][left]

            # Add prefixes that start in left
            # and continue into right
            lp = prod[left]

            for r in range(k):
                cnt[(lp * r) % k][node] += cnt[r][right]

        # -------------------------
        # Build tree
        # -------------------------
        for node in range(size - 1, 0, -1):
            pull(node)

        # -------------------------
        # Point update
        # -------------------------
        def update(pos, value):
            node = size + pos
            p = value % k

            prod[node] = p

            # Clear previous counts
            for r in range(k):
                cnt[r][node] = 0

            cnt[p][node] = 1

            node //= 2

            while node:
                pull(node)
                node //= 2

        # -------------------------
        # Merge two segment results
        # -------------------------
        def merge(A, B):
            # A = (product, counts)
            # B = (product, counts)

            ap, ac = A
            bp, bc = B

            new_p = (ap * bp) % k
            new_c = ac[:]

            for r in range(k):
                new_c[(ap * r) % k] += bc[r]

            return new_p, new_c

        # -------------------------
        # Range query [l, n-1]
        # -------------------------
        def query(l):
            left_result = (1 % k, [0] * k)
            right_result = (1 % k, [0] * k)

            l += size
            r = size + n - 1

            while l <= r:
                if l & 1:
                    # This segment comes before everything
                    # already collected on the right side.
                    left_result = merge(left_result, (
                        prod[l],
                        [cnt[x][l] for x in range(k)]
                    ))
                    l += 1

                if not (r & 1):
                    # This segment comes before right_result
                    rnode = (
                        prod[r],
                        [cnt[x][r] for x in range(k)]
                    )
                    right_result = merge(rnode, right_result)
                    r -= 1

                l //= 2
                r //= 2

            result = merge(left_result, right_result)
            return result

        # -------------------------
        # Process queries
        # -------------------------
        answer = []

        for index, value, start, x in queries:

            # Persistent update
            update(index, value)

            # Prefixes of nums[start:]
            _, counts = query(start)

            answer.append(counts[x])

        return answer