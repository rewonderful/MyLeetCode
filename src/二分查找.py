#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# def binarySearch(nums,target):
#     low = 0
#     high = len(nums)-1
#
#     while(low <= high):
#         mid = int((low + high) / 2)
#
#         if target == nums[mid]:
#             return mid
#         if target > nums[mid]:
#             low = mid+1
#         else:
#             high = mid - 1
#     return 0
def binarySearch(nums,target):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    return - 1


if __name__ == '__main__':
    nums = [1,2,3,4,5,9,11,13,222,333,444,555]
    target = 5
    print(binarySearch(nums,target))