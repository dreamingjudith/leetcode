from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 64 ms, 14.4 MB
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = current = ListNode(0)
        carry = 0

        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            current.next = ListNode(carry % 10)
            current = current.next

            carry = carry // 10

        return dummy.next


def make_listnode(input_list):
    head = cur = ListNode(input_list[0])

    for i in input_list[1:]:
        cur.next = ListNode(i)
        cur = cur.next

    return head


if __name__ == '__main__':
    s = Solution()

    l1 = [9, 9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]

    input1 = make_listnode(l1)
    input2 = make_listnode(l2)

    ret = s.addTwoNumbers(input1, input2)
    ans = list()
    while ret:
        ans += [ret.val]
        ret = ret.next
    print(ans)
