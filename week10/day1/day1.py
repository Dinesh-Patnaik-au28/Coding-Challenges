# #Q-1 ) Delete Node in a Linked List
# #https://leetcode.com/problems/delete-node-in-a-linked-list/
# #(5 marks)
# #(Medium)
# #Write a function to delete a node in a singly-linked list. You will not be given
# #access to the head of the list, instead you will be given access to the node
# #to be deleted directly.
# #It is guaranteed that the node to be deleted is not a tail node in the list.
# #Example 1:
# #Input: head = [4,5,1,9], node = 5
# #Output: [4,1,9]
# #Explanation: You are given the second node with value 5, the linked list
# #should become 4 -> 1 -> 9 after calling your function.
class Solution:
    def deleteNode(self, node):
        node.val,node.next=node.next.val,node.next.next
# #Q-2 )Remove Duplicates from Sorted List (5 marks)
# #https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# #(Easy)
# #Given the head of a sorted linked list, delete all duplicates such that each
# #element appears only once. Return the linked list sorted as well.
# #Example 1:
# #Input: head = [1,1,2]
# #Output: [1,2]
# #Example 2:
# #Input: head = [1,1,2,3,3]
# #Output: [1,2,3]
ListNode = [1,1,2]
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        mem = set()
        prev = None
        curr = head
        while curr:
            if curr.val in mem:
                prev.next = curr.next
            else:
                mem.add(curr.val)
                prev = curr
            curr = curr.next
        return head
# #Q-3 ) Merge In Between Linked Lists (5 marks)
# #https://leetcode.com/problems/merge-in-between-linked-lists/ (Medium)
# #You are given two linked lists: list1 and list2 of sizes n and m respectively.
# #Remove list1's nodes from the ath node to the bth node, and put list2 in their
# #place.
# #The blue edges and nodes in the following figure incidate the result:
# #Build the result list and return its head.
# #Example 1:
# #Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# #Output: [0,1,2,1000000,1000001,1000002,5]
# #Explanation: We remove the nodes 3 and 4 and put the entire list2 in their
# #place. The blue edges and nodes in the above figure indicate the result.
ListNode = [0,1,2,3,4,5]
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head=list1
        c=0
        while(c<=b):
            if c==a-1:
                prev=list1
                list1=list1.next
                prev.next=list2
            else:
                list1=list1.next
            c+=1
        while(list2.next):
            list2=list2.next
        list2.next=list1
        return head                