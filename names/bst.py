"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # print('>>>>>>>>> VALUE ', value)
        # take the current value of our node (self.value)
        # compare to the new value we want to insert
        # if new value < self.value
        if self.value > value:
            # if self.left is already taken by a node
            if self.left != None:
                # make that (left) node, call insert
                self.left.insert(value)
            else:
                # set the left to the new node with the new value
                self.left = BSTNode(value)

        # elif new value >= self.value
        elif self.value <= value:
            # if self.right is already taken by node
            if self.right != None:
                # make that (right) node call insert
                self.right.insert(value)
            # set the right child to the new node with new value
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value < target
        # found = False
        if self.value > target:
            # check the left substree
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        # elif current value >= target
        if self.value <= target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    # Return the maximum value found in the tree
    def get_max(self):
        # current = self

        # while(current.right):
        #     current = current.right
        # return current.value
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        if self.value is None:
            pass
        else:
            fn(self.value)
            if self.left is not None:
                self.left.for_each(fn)
            if self.right is not None:
                self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # create a queue for nodes
        queue = []
        # add the first node to the queue
        queue.append(self.value)
        # while queue is not empty
        while(len(queue) != 0):
            # remove the first node from the queue
            # print the removed node
            print(queue.pop(0))
            # add all children into the queue
            if self.left and self.right:

                queue.append(self.left)
                queue.append(self.right)
                return self.left.bft_print()
            else:
                pass

            if self.right:
                queue.append(self.right)
                return self.right.bft_print()
            else:
                pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    def dft_print(self):
        # create a stack for nodes
        # add the first node to the stack
        # while the stack is not empty
        # get the current node from the top of the stack
        # print that node
        # add all children to the stack
        # keep in mind, the order you add the children, will matter
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
'''
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
'''
