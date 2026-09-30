class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        length=sum(nums)
        if length%k!=0:
            return False

        target =length//k
        nums.sort(reverse=True)
        sides=[0]*k

        def back_track(i):
            if i==len(nums):
                return True

            for j in range(k):
                if sides[j] + nums[i] <=target:
                    sides[j]+=nums[i]
                    if back_track(i+1):
                        return True
                    sides[j]-=nums[i]
                if sides[j]==0:
                    break
            return False

        return back_track(0)


        