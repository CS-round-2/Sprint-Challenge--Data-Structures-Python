class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#! Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        elif value >= self.value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

#! Return True if the tree contains the value
    def contains(self, target):
        if target < self.value:
            return self.left.contains(target) if self.left else False
        elif target > self.value:
            return self.right.contains(target) if self.right else False
        else:
            return True

#! Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

#! Call the function `fn` on the value of each node
    def for_each(self, fn):
        self.value = fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)