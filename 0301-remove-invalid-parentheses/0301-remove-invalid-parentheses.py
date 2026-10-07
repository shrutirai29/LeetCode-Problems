from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str):
        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        result = []
        queue = deque([s])
        visited = {s}
        found = False

        while queue:
            current = queue.popleft()

            if is_valid(current):
                result.append(current)
                found = True

            # Once we find valid strings at this level,
            # don't generate strings with more removals.
            if found:
                continue

            for i in range(len(current)):
                # Only remove parentheses, never letters
                if current[i] not in "()":
                    continue

                new_string = current[:i] + current[i + 1:]

                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return result