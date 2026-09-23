class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    
        res = []
        subset = []
        self.target = target

        candidates.sort()

        def dfs(i):
            if sum(subset)>self.target:
                return


            if i == len(candidates):
                if sum(subset) == self.target:
                    res.append(subset.copy())
                return

            # Include candidates[i]
            subset.append(candidates[i])
            dfs(i + 1)
            subset.pop()

            # Don't include candidates[i]
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1)

        dfs(0)
        return res
    

