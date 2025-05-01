from typing import List
import bisect
import collections

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()

        def can_assign(k):
            task_deque = collections.deque(tasks[:k][::-1])
            w = workers[-k:]
            available_pills = pills
            i = k - 1

            for _ in range(k):
                if i >= 0 and w[i] >= task_deque[0]:
                    # Assign without pill
                    i -= 1
                    task_deque.popleft()
                elif available_pills > 0:
                    # Find the weakest worker that can do the task with a pill
                    j = bisect.bisect_left(w, task_deque[0] - strength, 0, i + 1)
                    if j > i:
                        return False
                    del w[j]
                    i -= 1
                    available_pills -= 1
                    task_deque.popleft()
                else:
                    return False
            return True

        lo, hi = 0, min(len(tasks), len(workers))
        ans = 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if can_assign(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
 