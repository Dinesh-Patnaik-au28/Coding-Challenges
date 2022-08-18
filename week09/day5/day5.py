#Q-2 ) Convert Binary Number in a Linked List to Integer: (5 marks)
#https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
#(Easy)
#Given head which is a reference node to a singly-linked list. The value of each
#node in the linked list is either 0 or 1. The linked list holds the binary
#representation of a number.
#Return the decimal value of the number in the linked list.
#Example 1:
#Input: head = [1,0,1]
#Output: 5
#Explanation: (101) in base 2 = (5) in base 10
List = [1,0,1]
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        while head:
            num = (num<<1) | head.val
            head = head.next
        return num



#Q-3 ) Middle of the Linked List (5 marks)
#https://leetcode.com/problems/middle-of-the-linked-list/
#(Medium)
#Given a non-empty, singly linked list with head node head, return a middle node
#of linked list.
#If there are two middle nodes, return the second middle node.
#Example 1:
#Input: [1,2,3,4,5]
#Output: Node 3 from this list (Serialization: [3,4,5])
#The returned node has value 3. (The judge's serialization of this node is
#[3,4,5]).
#Note that we returned a ListNode object ans, such that:
#ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next
#= NULL.
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            fast=fast.next.next
            slow=slow.next
        return slow      
