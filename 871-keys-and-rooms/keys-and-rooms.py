class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited =  [0] * len(rooms)
        visited[0] = 1
        n = len(rooms)
        keys = set()
        def bfs(room): 
            next = []
            for key in room:
                if key not in keys:
                    visited[key] = 1
                    keys.add(key)
                    next.extend(rooms[key])
            if len(next) != 0:
                bfs(next)
        bfs(rooms[0]) 
        return len(visited) == sum(visited)