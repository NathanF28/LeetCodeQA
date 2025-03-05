class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        print(parts)
        stack = []
        for part in parts:
            if part != "." and part != "":
                stack.append(part)
            if stack and part == "..":
                stack.pop()
                if stack:
                    stack.pop()
        return "/" + "/".join(stack)