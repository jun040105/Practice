def maxArrayValue(self, nums):
    
    best = nums[-1]
    current = nums[-1]

    for i in range(len(nums)-2, -1, -1):

        if nums[i] <= current:
            current += nums[i]
        else: 
            current = nums[i]
            
        if best < current:
            best = current
        
    return best