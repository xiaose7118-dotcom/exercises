# -*- coding: utf-8 -*-
# @File  : 两数之和.py
# @Author: liaojunfei
# @Date  : 2025/11/25
"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.
示例 2：

输入：l1 = [0], l2 = [0]
输出：[0]
示例 3：

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

"""
from typing import List
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList():
    def __init__(self):
        self.head = None
    def add(self, val):
        if self.head is None:
            self.head = Node(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(val)
    def print(self):
        tmp = []
        cur = self.head
        while cur:
            tmp.append(cur.val)
            cur = cur.next
        return tmp





def twoNumSum(l1:List[int], l2:List[int]):
    # 创建两个链表
    l1_list = LinkedList()
    for i in l1:
        l1_list.add(i)
    l2_list = LinkedList()
    for i in l2:
        l2_list.add(i)
    l1 = l1_list.print()
    l2 = l2_list.print()
    l1.reverse()
    l2.reverse()
    l1 = int(''.join(map(str, l1)))
    l2 = int(''.join(map(str, l2)))
    return str(l1 + l2)











if __name__ == '__main__':
    print(twoNumSum([2, 4, 3], [5, 6, 4]))