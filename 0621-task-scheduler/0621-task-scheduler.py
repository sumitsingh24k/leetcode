class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        max_heap=[-val for key,val in freq.items()]
        heapq.heapify(max_heap)
        queue=deque()
        time=0
        while max_heap or queue:
            time+=1
            if max_heap:
                f=heapq.heappop(max_heap)+1
                if f!=0:
                    queue.append((f,time+n))
            if queue and queue[0][1]==time:
                heapq.heappush(max_heap,queue.popleft()[0])
        return time