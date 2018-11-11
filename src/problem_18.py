#!/usr/bin/env python
# _*_ coding:utf-8 _*_
def fourSum( nums, target):
    def findNsum(l, r, target, N, result, results):
        if r-l+1 < N or N < 2 or target < nums[l]*N or target > nums[r]*N:  # early termination
            return
        if N == 2: # two pointers solve sorted 2-sum problem
            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else: # recursively reduce N
            for i in range(l, r+1):
                if i == l or (i > l and nums[i-1] != nums[i]):
                    findNsum(i+1, r, target-nums[i], N-1, result+[nums[i]], results)

    nums.sort()
    results = []
    findNsum(0, len(nums)-1, target, 4, [], results)
    return results


#
def fourSum2( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    ln = len(nums)
    res = set()
    dict = {}
    if ln < 4:
        return []

    nums.sort()
    for p in range(ln):
        for q in range(p + 1, ln):
            if nums[p] + nums[q] not in dict:
                dict[nums[p] + nums[q]] = [(p, q)]
            else:
                dict[nums[p] + nums[q]].append((p, q))
    for i in range(ln):
        for j in range(i + 1, ln - 2):
            T = target - nums[i] - nums[j]
            if T in dict:
                for k in dict[T]:
                    if k[0] > j:
                        res.add((nums[i], nums[j], nums[k[0]], nums[k[1]]))
    return [list(i) for i in res]



if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]

    target = -1
    print(fourSum(nums,target))