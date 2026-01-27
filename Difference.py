class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2 = set(nums2)
        return [list(s1-s2), list(s2 - s1)]


# The time complexity of the below code in O(n**2)

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1 = []
        list2 = []
        flist = []
        for n in nums1:
            if n not in list1 and n not in nums2:
                list1.append(n)

        for n in nums2:
            if n not in list2 and n not in nums1:
                list2.append(n)
        
        flist.append(list1)
        flist.append(list2)

        return flist
        