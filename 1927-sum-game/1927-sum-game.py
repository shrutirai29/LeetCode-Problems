class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(mid):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(mid, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # If the number of ? is the same,
        # Bob can always force equality.
        if left_q == right_q:
            return left_sum != right_sum

        # Bob wins only if the current difference
        # can exactly be compensated by the extra ?s.
        diff = left_sum - right_sum
        q_diff = left_q - right_q

        if diff * 2 == -9 * q_diff:
            return False

        return True