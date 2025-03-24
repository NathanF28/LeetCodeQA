class Solution:
    def validStrings(self, n: int) -> List[str]:
        possible = []

        def backtrack(path):
            if len(path) == n:
                possible.append("".join(path[:]))
                return
            for binary in "01":
                if binary == "0":
                    if len(path) > 0 and binary == path[-1]:
                        continue
                path.append(binary)
                backtrack(path)
                path.pop()
        backtrack([])
        return possible
