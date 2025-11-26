# -*- coding: utf-8 -*-
# @File  : 两数相加.py
# @Author: liaojunfei
# @Date  : 2025/11/25

"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。
示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

"""
from typing import List

def log(name):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{name} start')
            result = func(*args, **kwargs)
            print(f'{name} result: {result}')
            print(f'{name} end')
            return result
        return wrapper
    return decorator





@log('twoSum')
def twoSum(nums: List[int], target:int):
    for ind,num in enumerate(nums):
        for other_ind,other_num in enumerate(nums[ind+1:]):
            if num + other_num == target:
                return [ind,other_ind + ind + 1]







if __name__ == '__main__':
    print(twoSum([2,7,11,15],9))
    print(twoSum([3,2,4],6))