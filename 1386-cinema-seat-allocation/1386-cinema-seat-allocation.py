class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}

        # Store reserved seats for each row
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        # Initially assume every row can fit 2 groups
        ans = 2 * n

        for row, seats in rows.items():
            # This row was counted as 2 groups,
            # so remove those 2 first.
            ans -= 2

            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            if left.isdisjoint(seats) and right.isdisjoint(seats):
                # Can fit two groups: 2-5 and 6-9
                ans += 2

            elif left.isdisjoint(seats):
                # Only left block works
                ans += 1

            elif right.isdisjoint(seats):
                # Only right block works
                ans += 1

            elif middle.isdisjoint(seats):
                # Only middle block works
                ans += 1

        return ans