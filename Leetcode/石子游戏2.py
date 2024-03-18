class Solution:
    @staticmethod
    def stoneGameII(piles):
        def dfs(now,idx,M,flag):
            for i in range(min(M+1,len(piles)-idx)):
                idx_t = idx + i
                if flag:
                    now += sum(piles[idx:idx_t])
                    flag = 0
                dfs(now,idx_t,M,flag)

        M = 1
        idx = 0
        flag = 1




print(Solution.stoneGameII([2,7,9,4,4]))