class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def reverse_number(l: Optional[ListNode]) -> int:
    n = 0
    multiplyer = 1
    while l is not None:
        n += l.val * multiplyer
        multiplyer *= 10
        l = l.next
    return n
def MakingAnswer(num3):
    answer = ListNode()  
    curr = answer  
    while num3 != 0:
        curr.next = ListNode(num3 % 10)  
        curr = curr.next 
        num3 //= 10 
    if not answer.next:  
        answer.next = ListNode(0)  
    return answer.next 

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = reverse_number(l1)
        num2 = reverse_number(l2)
        num3 = num1+num2
        Answer = MakingAnswer(num3) 
        return Answer
        