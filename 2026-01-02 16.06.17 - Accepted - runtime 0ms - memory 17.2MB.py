class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(mins, secs):
            if mins < 0 or secs < 0 or mins > 99 or secs > 99:
                return float('inf')
            s = str(mins * 100 + secs)
            cur = str(startAt)
            total = 0
            for c in s:
                if c != cur:
                    total += moveCost
                    cur = c
                total += pushCost
            return total
        
        mins, secs = divmod(targetSeconds, 60)
        # Try two ways: normal or transfer 1 minute to 60 seconds
        return min(cost(mins, secs), cost(mins - 1, secs + 60))