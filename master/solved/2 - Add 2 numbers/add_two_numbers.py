from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.get_number(l1)
        num2 = self.get_number(l2)
        list_number = self.get_list_from_int(num1 + num2)
        return self.recursive_list_node(list_number)

    def get_list_from_int(self, number: Optional[int]):
        str_number = str(number)
        return [int(char) for char in str_number]

    def recursive_list_node(self, list_number):
        if list_number:
            val = list_number[-1]
            if len(list_number) > 1:
                next_val = list_number[-2]
                next_node = ListNode(next_val, next=self.recursive_list_node(list_number[:-2]))
                return ListNode(val, next_node)
            else:
                return ListNode(val, None)

    def get_number(self, listnode=Optional[ListNode]):
        linked_values = []
        next_node = listnode.next
        if isinstance(listnode.val, int):
            # must be a valid number, we need to traverse the linked lists until we hit next=None
            linked_values.append(listnode.val)
            while next_node is not None:
                linked_values.append(next_node.val)
                next_node = next_node.next
            linked_values.reverse()
            return int(('').join(map(str, linked_values)))
        return 0


if __name__ == '__main__':
    number_425 = ListNode(val=5, next=ListNode(val=2, next=ListNode(val=4)))
    number_182 = ListNode(val=2, next=ListNode(val=8, next=ListNode(val=1)))
    solution = Solution()
    l1 = solution.addTwoNumbers(number_425, number_182)
    print(solution.get_number(l1))
