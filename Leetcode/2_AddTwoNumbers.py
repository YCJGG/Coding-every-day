# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
   def addTwoNumbers(self, l1, l2):
        resultNode = None
        add = 0
        while True:
            if l1.val == -1:
                l1.val = 0
            if l2.val == -1:
                l2.val = 0

            tSum = (l1.val + l2.val + add) % 10
            add = (l1.val + l2.val + add) / 10
            listn = ListNode(tSum)

            if resultNode == None:
                resultNode = listn
                flagNode = resultNode
            else:
                flagNode.next = listn
                flagNode = flagNode.next

            if l1.next != None:
                l1 = l1.next
            else:
                l1.val = -1

            if l2.next != None:
                l2 = l2.next
            else:
                l2.val = -1

            if l1.val == -1 and l2.val == -1:
                break

        if add != 0:
            listn = ListNode(add)
            flagNode.next = listn

        return resultNode


