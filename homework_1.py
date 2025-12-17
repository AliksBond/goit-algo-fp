class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_list(head):
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


def insertion_sort(head):
    if not head:
        return None

    sorted_head = None
    current = head

    while current:
        next_node = current.next
        if not sorted_head or current.data < sorted_head.data:
            current.next = sorted_head
            sorted_head = current
        else:
            temp = sorted_head
            while temp.next and temp.next.data <= current.data:
                temp = temp.next
            current.next = temp.next
            temp.next = current
        current = next_node

    return sorted_head


def merge_sorted_lists(a, b):
    dummy = Node(0)
    tail = dummy

    while a and b:
        if a.data <= b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a if a else b
    return dummy.next


def add(head, value):
    if not head:
        return Node(value)
    node = head
    while node.next:
        node = node.next
    node.next = Node(value)
    return head


def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")


if __name__ == "__main__":
    l1 = None
    for v in [6, 2, 9, 1, 4]:
        l1 = add(l1, v)

    l2 = None
    for v in [0, 3, 5, 7]:
        l2 = add(l2, v)

    print_list(l1)
    l1 = reverse_list(l1)
    print_list(l1)
    l1 = insertion_sort(l1)
    print_list(l1)

    print_list(l2)
    merged = merge_sorted_lists(l1, l2)
    print_list(merged)
