class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lsize=len(nums)
        for i in range(lsize):
            for j in range(lsize):
                if nums[i]+nums[j]==target and i!=j:
                    return [i,j]
        print("no existing solution ")

def main():
       nums1=[2, 7, 11, 15]
       Sol1=Solution()
       print(Sol1.twoSum(nums1,9))
       
if __name__ == '__main__':
    main()   