class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        window=len(cardPoints)-k
        start_sum=sum(cardPoints[:window])
        total=sum(cardPoints)
        max_val=total-start_sum
        if window==len(cardPoints):
            return sum(cardPoints)
        for i in range(window,len(cardPoints)):
            start_sum=start_sum+cardPoints[i]-cardPoints[i-window]
            max_val=max(total-start_sum,max_val)
        return max_val