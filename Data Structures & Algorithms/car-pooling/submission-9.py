class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        diff = [0] * 1002
        for p, s, e in trips:
            diff[s] += p
            diff[e] -= p
        load = 0
        for d in diff:
            load += d
            if load > capacity:
                return False
        return True