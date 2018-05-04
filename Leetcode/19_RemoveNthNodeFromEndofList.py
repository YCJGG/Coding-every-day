# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        node2 = ListNode(0)
        if head == None or head.next == None:
            return None
        node1 = head
        node2.next  = head
        i = 0 
        while(node1):
            i+=1
            node1 = node1.next
        #print(i)
        k = i - n 
        first = node2
        while(k > 0):
            k-=1
            first = first.next
        first.next = first.next.next
        return node2.next
            
## two pass methods 
#the first pass is to obtain the list length
# the second pass is to delete the target node