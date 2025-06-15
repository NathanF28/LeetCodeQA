class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        window = deque()
        for i in range(k):
            window.append(arr[i])
        for i in range(k,len(arr)):
            first = window[0]
            last = window[-1]
            cand = abs(arr[i] - x)
            furthest = max(abs(x-first),abs(x-last))
            if cand < furthest:
                if cand < abs(x-first):
                    window.popleft()
                    window.append(arr[i])
                else:
                    window.pop()
                    window.append(arr[i])
        return list(window)
    
    
    