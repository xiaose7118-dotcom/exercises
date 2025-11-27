# -*- coding: utf-8 -*-
# @File  : 多数元素.py
# @Author: liaojunfei
# @Date  : 2025/11/27
"""
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。
示例 1：

输入：nums = [3,2,3]
输出：3
示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2
"""

def get_most_num(nums):
    new_num,cur = 0,0
    tmp = dict()
    for num in nums:
        if not tmp.get(num,None):
            tmp[num] = 1
        else:
            tmp[num] += 1
            if cur < tmp[num]:
                cur = tmp[num]
                new_num = num
    return new_num





if __name__ == '__main__':
    print(get_most_num([3,2,3]))
    print(get_most_num([2,2,1,1,1,2,2]))