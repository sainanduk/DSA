class BST:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val is None:
            self.val = val
            return
        if val < self.val:
            if self.left is None:
                self.left = BST(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BST(val)
            else:
                self.right.insert(val)

    def search(self, val, count=0):
        if self.val == val:
            return self, count
        if val < self.val:
            if self.left:
                count += 1
                return self.left.search(val, count)
        elif self.val < val:
            if self.right:
                count += 1
                return self.right.search(val, count)
        return None 

    def delete(self, val):
        if self is None:
            return self
        if val < self.val:
            self.left = self.left.delete(val)
        elif self.val < val:
            self.right = self.right.delete(val)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            else:
                temp = self.right.minimum()
                self.val = temp.val
                self.right = self.right.delete(temp.val)
        return self


    def minimum(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def printtree(self):
        if self is None:
            return
        if self.left:
            self.left.printtree()
        print(self.val)
        if self.right:
            self.right.printtree()

if __name__ == "__main__":
    obj = BST(7)
    obj.insert(5)
    obj.insert(12)
    obj.insert(4)
    obj.insert(6)
    obj.insert(10)
    obj.insert(15)
    obj.insert(9)
    obj.insert(11)
    obj.insert(14)
    obj.insert(16)
    obj.printtree()
    print("_______________")
    obj.delete(12)
    obj.printtree()