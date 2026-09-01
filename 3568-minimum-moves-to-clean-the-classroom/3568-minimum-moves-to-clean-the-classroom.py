from collections import deque
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        litter = {}
        start = None
        litter_count = 0

        # Find starting position and assign a bit to every litter cell
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = litter_count
                    litter_count += 1

        # No litter to collect
        if litter_count == 0:
            return 0

        target_mask = (1 << litter_count) - 1

        # (row, col, collected_mask, remaining_energy, moves)
        queue = deque([
            (start[0], start[1], 0, energy, 0)
        ])

        # best[(row, col, mask)] = maximum energy seen
        best = {
            (start[0], start[1], 0): energy
        }

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, mask, remaining, moves = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check boundaries and obstacles
                if (
                    nr < 0 or nr >= m or
                    nc < 0 or nc >= n or
                    classroom[nr][nc] == 'X'
                ):
                    continue

                # Cannot make a move without energy
                if remaining == 0:
                    continue

                new_energy = remaining - 1
                new_mask = mask

                # Collect litter
                if (nr, nc) in litter:
                    bit = litter[(nr, nc)]
                    new_mask |= (1 << bit)

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # All litter collected
                if new_mask == target_mask:
                    return moves + 1

                state = (nr, nc, new_mask)

                # Only continue if we reached this state
                # with more remaining energy
                if best.get(state, -1) >= new_energy:
                    continue

                best[state] = new_energy
                queue.append(
                    (nr, nc, new_mask, new_energy, moves + 1)
                )

        return -1