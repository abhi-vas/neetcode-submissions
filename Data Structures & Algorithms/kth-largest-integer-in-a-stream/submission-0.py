class KthLargest:
    def heapify(self,size,k):
        l=2*k+1
        r=2*k+2
        largest=k
        if l<size and self.nums[l] > self.nums[largest]:
            largest=l
        if r<size and self.nums[r] > self.nums[largest]:
            largest=r
        if largest!=k:
            self.nums[k],self.nums[largest]=self.nums[largest],self.nums[k]
            self.heapify(size,largest)

    def build_heap(self):
        n=((len(self.nums)//2) -1)
        for i in range(n,-1,-1):
            self.heapify(len(self.nums),i)
    def insert(self,val):
        self.nums.append(val)
        index=len(self.nums)-1
        while index>0:
            parent=(index-1)//2
            if self.nums[index] > self.nums[parent]:
                self.nums[index],self.nums[parent]=self.nums[parent],self.nums[index]
                index=parent
            else:
                break
    def delete(self):
        l=len(self.nums)-1
        self.nums[0],self.nums[l]=self.nums[l],self.nums[0]
        item=self.nums.pop()
        self.heapify(len(self.nums),0)
        return item



    def __init__(self, k: int, nums: List[int]):
        self.k=k
        self.nums=nums
        self.build_heap()

    def add(self, val: int) -> int:
        self.insert(val)
        nums=[]
        for i in range(self.k):
            item=self.delete()
            nums.append(item)
        for val in nums:
            self.insert(val)
        return item

        
