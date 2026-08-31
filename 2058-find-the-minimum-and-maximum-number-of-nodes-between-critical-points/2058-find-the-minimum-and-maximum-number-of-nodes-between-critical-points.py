class Solution:
    def nodesBetweenCriticalPoints(self, head):
        prev = head
        curr = head.next

        index = 1
        first = -1
        last = -1
        min_dist = float('inf')

        while curr.next:
            next_node = curr.next

            # Check if curr is a critical point
            if ((curr.val > prev.val and curr.val > next_node.val) or
                (curr.val < prev.val and curr.val < next_node.val)):

                if first == -1:
                    # First critical point
                    first = index
                else:
                    # Distance from previous critical point
                    min_dist = min(min_dist, index - last)

                last = index

            prev = curr
            curr = next_node
            index += 1

        # Fewer than two critical points
        if first == last:
            return [-1, -1]

        max_dist = last - first

        return [min_dist, max_dist]