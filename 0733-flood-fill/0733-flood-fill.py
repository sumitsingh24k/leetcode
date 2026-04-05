class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited=set()
        direction=[(1,0),(-1,0),(0,1),(0,-1)]
        original=image[sr][sc]
        queue=deque([(sr,sc)])
        image[sr][sc]=color
        r,c=len(image),len(image[0])
        if original == color:
            return image
        while queue:
            row,col=queue.popleft()
            for dr,dc in direction:
                nr,nc=dr+row,dc+col
                if 0<=nr<r and 0<=nc<c and image[nr][nc]==original:
                    image[nr][nc]=color
                    queue.append([nr,nc])
        return image