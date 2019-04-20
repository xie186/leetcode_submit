
class Solution:
    def twoSumHash(self, nums, target):
        if len(nums) < 2:
            pass
        tempDict = {nums[0] : 0}
        for i in range(1, len(nums)):
            checkNum = target-nums[i]
            if(checkNum in tempDict.keys()):
                return [i,tempDict[checkNum]]
            else:
                tempDict[nums[i]] = i
                
    def twoSum(self, nums, target):
        '''
        The brute force approach is simple. Loop through each element xx and find 
        if there is another value that equals to target - xtarget−x.
        '''
        for i in range(0, len(nums)): 
            #print("i:" + str(i))
            for j in range(i + 1, len(nums)):
                #print(str(i) + " " + str(j) + ":" + str(nums[j]))
                if(nums[j] == target - nums[i]):
                    return [i, j]
