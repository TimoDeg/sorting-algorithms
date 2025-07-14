nums = [ 0, 1, 4, 2, 6, 3, 8, 9, 9, 5]

for i in range(len(nums)):
    for j in range(len(nums) -1 - i):
        current_num = nums[j]
        next_num = nums[j + 1]

        if (current_num > next_num):
            nums[j] = next_num
            nums[j + 1] = current_num
            
print(nums)    
