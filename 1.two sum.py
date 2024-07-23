nums = [2,7,9,11]
target = 9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if target == nums[i]+nums[j]:
            output = [i,j]
print(output)