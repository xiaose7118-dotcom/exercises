# -*- coding: utf-8 -*-
# @File  : 删除有序数组中的重复项 II.py
# @Author: liaojunfei
# @Date  : 2025/11/27
"""
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使得出现次数超过两次的元素只出现两次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3。 不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前七个元素被修改为 0, 0, 1, 1, 2, 3, 3。不需要考虑数组中超出新长度后面的元素。
"""

def remove_num(nums):
    cur = dict()
    new_list = []
    for num in nums:
        if not cur.get(num,None) or cur.get(num,0) < 2:
            cur[num] = cur.get(num,0) + 1
            new_list.append(num)
    return len(new_list),new_list


if __name__ == '__main__':
    print(remove_num([0,0,1,1,1,1,2,3,3]))
    print(remove_num([1,1,1,2,2,3]))