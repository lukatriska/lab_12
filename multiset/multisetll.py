from node import *        

# A class implementing Multiset as a linked list.

class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def traversal(self):
        """
        Traverse through the whole list printing its items along the way.
        :return: None
        """
        curNode = self._head
        while curNode is not None:
            if hasattr(curNode, 'data'):
                print(curNode.data)
            else:
                print(curNode)
            curNode = curNode.next

    def unorderedSearch(self, target):
        """
        Searches for the target.
        :param target: item you want to find
        :return: True if item is in the list, False if not 
        :rtype: 
        """
        target = str(target)
        curNode = self._head
        while curNode is not None:
            if curNode.item == target:
                return True
            curNode = curNode.next
        return False

    def remove_all(self):
        """
        Removes all items from the list.
        :return: 
        :rtype: 
        """
        self._head = None

    def split_half(self, head):
        counter, counter_2, counter_3 = 0, 0, 0
        curNode = self._head
        while curNode is not None:
            counter += 1
            curNode = curNode.next
        half_1 = int(counter/2)
        first_half = self._head
        curNode = self._head
        while curNode is not None:
            counter_2 += 1
            if counter_2 == half_1 + 1:
                second_half = curNode
            curNode = curNode.next
        return first_half.item, second_half.item

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

