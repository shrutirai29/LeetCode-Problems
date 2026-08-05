class Solution:
    def removeDuplicates(self, s: str) -> str:
        arr = []
        for a in s:
            if arr and a == arr[-1]:
                arr.pop()
            else:
                arr.append(a)

        return "".join(arr)