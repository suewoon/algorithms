# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num_1, num_2 = 0, 0
        digit_1, digit_2 = 0, 0
        while l1.next:
            num_1 += l1.val*pow(10,digit_1)
            digit_1 += 1
            l1.val = l1.next.val
            l1.next = l1.next.next
        num_1 += l1.val*pow(10, digit_1)

        while l2.next:
            num_2 += l2.val*pow(10, digit_2)
            digit_2 += 1
            l2.val = l2.next.val
            l2.next = l2.next.next
        num_2 += l2.val*pow(10, digit_2)

        result_list = [ int(i) for i in str(num_1 + num_2) ]
        result_node = ListNode(val=result_list[-1])
        current_node = result_node
        result_list = result_list[:-1]

        while result_list:
            current_node.next = ListNode(result_list[-1])
            result_list = result_list[:-1]
            current_node = current_node.next

        return result_node
