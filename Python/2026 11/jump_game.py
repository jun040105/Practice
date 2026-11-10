def canJump(nums):
    
    max_jump = 0

    for i in range (len(nums)):
        max_jump = max(max_jump, i + nums[i])

        if max_jump < i+1:
            return False

        if max_jump == len(nums)-1:
            return True