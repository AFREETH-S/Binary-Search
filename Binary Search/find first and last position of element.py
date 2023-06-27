class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        mid=len(nums)
        l,r = bisect_left(nums,target),bisect_right(nums,target)
        st,end=-1,-1
        if l<mid and target==nums[l]: st=l
        if nums[r-1]==target: end=r-1
        return [st,end]
            
