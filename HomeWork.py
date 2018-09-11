#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest import TestCase
from ddt import ddt, data, unpack


class Node(object):
    """ Node of Linked list """

    def __init__(self, value=None):
        """ Initially the node has neither value nor link to next element defined. """
        self.value = value
        self.next = None


class LinkedList(object):
    """ Linked lists manipulation methods. """

    def __init__(self):
        """ Initially the head of the Linked List isn't defined (zero length by default). """
        self.head = None

    def size(self):
        """ Get length of the Linked list.

        :return: integer representing number of elements in the Linked list
        """
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def remove_middle(self):
        """ Removes middle element of the Linked list.

        Note: If the Linked list has even number of elements, no element is removed.
        """
        # zero elements
        if self.head is None:
            return

        # one element
        if self.head.next is None:
            self.head = None
            return

        # more than one element
        # here two pointers are used: the fast one to reach the end of the structure and to determine odd/even length
        # and the slow one to reach the middle element at the same iteration when fast pointer reaches end of structure
        slow = self.head
        fast = self.head
        previous = None

        while fast and fast.next:
            fast = fast.next.next
            previous = slow
            slow = slow.next

        # if the fast pointer is defined, the list has odd length and we are going to remove the middle item
        # for even length of the list we'll leave the list untouched
        if fast:
            previous.next = slow.next


class TestData(object):
    """ Class holding the test data. """
    def __init__(self):
        """ Linked lists with different lengths are defined here.
        Expected results are defined by ordinary list to ease readability.
        """
        super(TestData, self).__init__()

        self.list0 = LinkedList()
        self.expected_list0_items = []

        self.list1 = LinkedList()
        self.list1.head = Node(1)
        self.expected_list1_items = []

        self.list2 = LinkedList()
        self.list2.head = Node(1)
        self.list2_item2 = Node("ahoj")
        self.list2.head.next = self.list2_item2
        self.expected_list2_items = [1, "ahoj"]

        self.list3 = LinkedList()
        self.list3.head = Node(1)
        self.list3_item2 = Node([1, u'hic sunt leones', 666])
        self.list3.head.next = self.list3_item2
        self.list3_item3 = Node(3)
        self.list3_item2.next = self.list3_item3
        self.expected_list3_items = [1, 3]

        self.list4 = LinkedList()
        self.list4.head = Node("a")
        self.list4_item2 = Node("b")
        self.list4.head.next = self.list4_item2
        self.list4_item3 = Node("c")
        self.list4_item2.next = self.list4_item3
        self.list4_item4 = Node("d")
        self.list4_item3.next = self.list4_item4
        self.expected_list4_items = ["a", "b", "c", "d"]

        self.list5 = LinkedList()
        self.list5.head = Node(1)
        self.list5_item2 = Node(2)
        self.list5.head.next = self.list5_item2
        self.list5_item3 = Node(3)
        self.list5_item2.next = self.list5_item3
        self.list5_item4 = Node(4)
        self.list5_item3.next = self.list5_item4
        self.list5_item5 = Node(5)
        self.list5_item4.next = self.list5_item5
        self.expected_list5_items = [1, 2, 4, 5]


@ddt
class DDTests(TestCase):
    """ Data Driven tests. """

    @data((TestData().list0, TestData().expected_list0_items),
          (TestData().list1, TestData().expected_list1_items),
          (TestData().list2, TestData().expected_list2_items),
          (TestData().list3, TestData().expected_list3_items),
          (TestData().list4, TestData().expected_list4_items),
          (TestData().list5, TestData().expected_list5_items))
    @unpack
    def test_different_list_lengths(self, llist, expected):
        """ Takes provided Linked list and removes the middle element.
        Then modified Linked list is compared with expected result.
        """
        llist.remove_middle()
        self.assertEqual(llist.size(), len(expected))
        current_result = llist.head
        ii = 0
        while current_result:
            if current_result.value == expected[ii]:
                current_result = current_result.next
                ii += 1
            else:
                raise AssertionError
