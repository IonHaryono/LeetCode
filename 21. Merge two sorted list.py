
# Definition for singly-linked list.
from heapq import merge


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        list1 = ListNode(val= 1, next= ListNode(val= 2, next= ListNode(val= 4, next= None)))
        list2= ListNode(val= 1, next= ListNode(val= 3, next= ListNode(val= 4, next= None)))

        final = dummy
        print(list1)
        print(list2)
        
        while list1 and list2:
            if list1.val <= list2.val:
                final.val = list1.val
                final, list1 = final.next, list1.next
                
            elif list1.val > list2.val:
                if list2 != None:
                    final.val = list2.val
                    final, list2 = final.next, list2.next

        
        return dummy.next  

solution = Solution()

print(solution.mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4]))

        