class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window_size=len(cardPoints)-k
        total=sum(cardPoints)
        if k==len(cardPoints):
            return total
        start_val=sum(cardPoints[:window_size])
        max_val = total - start_val

        for i in range(window_size,len(cardPoints)):
            start_val=start_val+cardPoints[i]-cardPoints[i-window_size]
            max_val=max(total-start_val,max_val)
        return max_val

