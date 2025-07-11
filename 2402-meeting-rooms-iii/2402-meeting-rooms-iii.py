class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_count = defaultdict(int)
        free_table = defaultdict(list)
        time_table = []
        map = {}
        meetings.sort()
        print(meetings)
        heap = []
        for i in range(n):
            heappush(heap,i)
        time = meetings[0][0]
        i = 0
        while i < len(meetings):
            while time_table and time >= time_table[0][0]:
                num = heappop(time_table)
                heappush(heap,num[1])
            while i < len(meetings) and heap and meetings[i][0] <= time:
                room = heappop(heap)
                room_count[room]+=1
                duration = meetings[i][1] - meetings[i][0]
                end = duration + time
                free_table[end].append(room)
                heappush(time_table, [end,room])
                map[i] = room
                i+=1
            if heap:
                if i < len(meetings):
                    time = meetings[i][0]
            elif time_table:
                node = time_table[0]
                time = node[0]
            else:
                time+=1
        final = sorted(room_count.items(), key = lambda item : item[1],reverse = True)
        _max = final[0][1]
        ans_heap = []
        for key,value in final:
            if value == _max:
                heappush(ans_heap,key)
            else:
                break
        return heappop(ans_heap)

            
            
            




