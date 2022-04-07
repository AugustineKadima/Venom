'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

pseudocode
-----------
function
looop
find complement of numers in nums array
loop again
find whether complement exists in the array
create a new array and add the indices of the complement and current numer
return indices of complements
else return [-1, -1]
'''

def twoSum(nums, target):
    if len(nums) < 2: return [-1, -1]

    for i in range(len(nums)):
        complement = target - nums[i]
        for j in range(len(nums)):
            if (nums[j] == complement) and i != j:
                return [i, j]

    return [-1, -1]

result  = twoSum([3,2,4], 6)
print(result)

# time complexity = O(n^2)
# space complexity =  O(n)