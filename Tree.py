class TreeNode():
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class Tree():
    def __init__(self, root=None):
        self.root = root

    # I frist assume there's no duplicate value in BST
    def insert(self, value):
        temp = TreeNode(value)
        if self.root == None:
            self.root = temp
        else:
            ptr = self.root
            while True:

                if temp.value > ptr.value and ptr.right == None:
                    ptr.right = temp
                    break
                elif temp.value > ptr.value and ptr.right != None:
                    ptr = ptr.right
                elif temp.value < ptr.value and ptr.left == None:
                    ptr.left = temp
                    break
                elif temp.value < ptr.value and ptr.left != None:
                    ptr = ptr.left



    def lookup(self, value):
        if self.root == None:
            return None
        else:
            ptr = self.root
            while True:

                if ptr.value == value:
                    return ptr
                elif value > ptr.value and ptr.right == None:
                    return None
                elif value > ptr.value and ptr.right != None:
                    ptr = ptr.right
                elif value < ptr.value and ptr.left == None:
                    return None
                elif value < ptr.value and ptr.left != None:
                    ptr = ptr.left

    def preorderTraversal(self):
        res=  []
        if self.root == None:
            return res
        res.append(self.root.value)

        if self.root.left != None:
            templ = Tree(self.root.left)
            res += templ.preorderTraversal()
        if self.root.right != None:
            tempr = Tree(self.root.right)
            res += tempr.preorderTraversal()
        return res

    def remove(self, value):
        """targetNode = self.lookup(value)
        if  targetNode == None:
            print("the value isn't exist!")
            return None
        parentNode = self.root
        while True:

            if parentNode.right == targetNode or parentNode.left == targetNode or parentNode.value == value:
                break

            if parentNode.value > value:
                parentNode = parentNode.left
            else:
                parentNode = parentNode.right

        if parentNode == targetNode:   # this part handle if remove node = root node
            pass

        if targetNode.left == None and targetNode.right == None:
            if parentNode.value > targetNode.value:
                parentNode.left = None
            else:
                parentNode.right = None
        elif targetNode.left == None and targetNode.right != None:
            if parentNode.value > targetNode.value:
                parentNode.left = targetNode.right
            else:
                parentNode.right = targetNode.right
        elif targetNode.left != None and targetNode.right == None:
            if parentNode.value > targetNode.value:
                parentNode.left = targetNode.left
            else:
                parentNode.right = targetNode.left
        else:
            newNode = targetNode.right"""


        # find parent node and target node
        if self.root.value == value:
            # if remove node == root , no need to find parent node
            pass

        else:
            # we first assume that remove value exist in the tree
            # find both parent node and target node
            parentNode = self.root
            if self.root.value > value:
                targetNode = self.root.left
            else:
                targetNode = self.root.right

            while True:

                if targetNode.value == value:
                    break

                parentNode = targetNode
                if targetNode.value > value:
                    targetNode = targetNode.left
                else:
                    targetNode = targetNode.right


        if targetNode.left == None and targetNode.right == None:
            # no children
            if parentNode.value > targetNode.value:
                parentNode.left = None
            else:
                parentNode.right = None
        elif targetNode.left != None and targetNode.right == None:
            # only got left children
            if parentNode.value > targetNode.value:
                parentNode.left = targetNode.left
            else:
                parentNode.right = targetNode.left
            targetNode.left = None
        elif targetNode.left == None and targetNode.right != None:
            # only got right children
            if parentNode.value > targetNode.value:
                parentNode.left = targetNode.right
            else:
                parentNode.right = targetNode.right
            targetNode.right = None
        else:
            # complicated situation , has both left node and right node

            # case 1:
            if targetNode.right.left != None:
                newTargetNode = targetNode.right.left
                newParentNode = targetNode.right
                while True:

                    if newTargetNode.left == None:
                        break

                    newParentNode = newTargetNode
                    newTargetNode = newTargetNode.left

                # use newTarget and newParent to traverse until the latest left children
                newParentNode.left = newTargetNode.right
                newTargetNode.left = targetNode.left
                newTargetNode.right = targetNode.right
                if parentNode.value > targetNode.value:
                    parentNode.left = newTargetNode
                else:
                    parentNode.right = newTargetNode
                targetNode.left = None
                targetNode.right = None
            else:
                if parentNode.value > targetNode.value:
                    targetNode.right.left = targetNode.left
                    parentNode.left = targetNode.right
                    targetNode.left = None
                else:
                    targetNode.right.left = targetNode.left
                    targetNode.left = None
                    parentNode.right = targetNode.right
                    targetNode.right = None











