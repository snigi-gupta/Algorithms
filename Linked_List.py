# Complete Linked List Implementation

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        newnode = ListNode(val)

        if self.head is None:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode

    def printnode(self):
        current = self.head
        while current.next:
            print(f' {current.val} ->', end=" ")
            current = current.next
        print(f' {current.val}')

    def prepend(self, val):
        newnode = ListNode(val)

        if self.head is None:
            self.head = newnode
            return
        newnode.next = self.head
        self.head = newnode

    def append_at_pos(self, val, preval):
        newnode = ListNode(val)
        current = self.head
        found = False
        while current.next:
            if current.val == preval:
                newnode.next = current.next
                current.next = newnode
                found = True
            current = current.next

        if not found:
            print(f'{preval} not found, cannot insert {val}')

    def removenode(self, val):
        current = self.head
        if current and current.val == val:
            self.head = current.next
            current = None
            return
        prevnode = None
        while current and current.val != val:
            prevnode = current
            current = current.next
        if current is None:
            print(f'{val} was not found, could not delete')
            return
        prevnode.next = current.next
        current = None

    def remove_from_pos(self, pos):
        current = self.head
        if pos == 0:
            self.head = current.next
            current = None
            return
        count = 0
        prevnode = None
        while current and count != pos:
            prevnode = current
            current = current.next
            count += 1

        if current is None:
            print(f'No element was found at {pos} position, could not delete')
            return

        prevnode.next = current.next
        current = None

    def len_iterative(self):
        current = self.head
        count = 0
        while current:
            current = current.next
            count += 1
        print(f'Length: {count}')

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, val1, val2):

        # nothing to swap
        if val1 == val2:
            print(f'There is nothing to swap')
            return

        prevnode1 = None
        current1 = self.head
        while current1 and current1.val != val1:
            prevnode1 = current1
            current1 = current1.next

        if current1 is None:
            print(f'{val1} was not found, cannot swap')
            return

        prevnode2 = None
        current2 = self.head
        while current2 and current2.val != val2:
            prevnode2 = current2
            current2 = current2.next

        if current2 is None:
            print(f'{val2} was not found, cannot swap')
            return


        if prevnode1:
            prevnode1.next = current2
        else:
            self.head = current2

        if prevnode2:
            prevnode2.next = current1
        else:
            self.head = current1

        current1.next, current2.next = current2.next, current1.next

    def reverse_iterative(self):
        current = self.head
        prevnode = None
        while current:
            nextnode = current.next
            current.next = prevnode
            prevnode = current
            current = nextnode
        self.head = prevnode

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)


if __name__ == "__main__":
    linkedList = LinkedList()
    # insert elements
    linkedList.append(1)
    linkedList.append(2)
    linkedList.append(3)
    linkedList.append(4)

    # print elements
    linkedList.printnode()

    # insert at the beginning
    linkedList.prepend(0)
    linkedList.printnode()

    # insert at a position
    linkedList.append_at_pos(2.5, 2)
    linkedList.printnode()
    linkedList.append_at_pos(6, 5)
    linkedList.printnode()

    # delete head node
    linkedList.removenode(0)
    linkedList.printnode()
    # delete a node
    linkedList.removenode(2.5)
    linkedList.printnode()
    linkedList.removenode(3.5)
    linkedList.printnode()

    # delete at a position
    linkedList.remove_from_pos(0)
    linkedList.printnode()
    linkedList.remove_from_pos(1)
    linkedList.printnode()

    # get length of list by iterative method
    linkedList.len_iterative()

    # get length of list by recursive method
    result = linkedList.len_recursive(linkedList.head)
    print(f'Length by Recursion: {result}')

    # swap two elements that exist
    linkedList.append(1)
    linkedList.append(3)
    linkedList.swap_nodes(1, 4)
    linkedList.printnode()

    # swap two elements where one element is head
    linkedList.swap_nodes(2, 1)
    linkedList.printnode()

    # swap two elements where both elements are same
    linkedList.swap_nodes(2, 2)
    linkedList.printnode()

    # swap two elements where both elements are not present
    linkedList.swap_nodes(5, 6)
    linkedList.printnode()

    # reverse a linked list
    linkedList.reverse_iterative()
    linkedList.printnode()

