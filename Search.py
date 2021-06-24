"""
linear search
binary search  (useful when data is put in a binary search tree)
BFS (traversal or search)  pros : shortest path , closer nodes  cons: more memories
DFS (traversal or search)  pros : less memory , does path exist(maze) cons: can get slow
如果樹很深  就用 BFS XD 因為DFS很花時間
如果樹很寬  就用 DFS 因為BFS可能會佔用掉太多 memory

BFS implementation >> iterate , recursive
DFS implementation >> inorder , preorder , postorder
"""
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

    def get(self):
        return self.root

    def BFSUsingIterate(self):
        currentNode = self.root
        res = []
        queue = []
        if currentNode == None:
            return res
        else:
            #res.append(currentNode.value)
            queue.append(currentNode)

        while True:
            if len(queue) <= 0:
                break
            res.append(queue[0].value)
            if queue[0].left != None:
                queue.append(queue[0].left)
            if queue[0].right != None:
                queue.append(queue[0].right)
            queue = queue[1:]
        return res

    def BFSUsingRecursive(self, thisChild):
        if len(thisChild) == 0:
            return []
        nextChild = []
        res = []
        for c in thisChild:
            if c != None:
                res.append(c.value)
                if c.left != None:
                    nextChild.append(c.left)
                if c.right != None:
                    nextChild.append(c.right)
        return res + self.BFSUsingRecursive(nextChild)

    def DFSUsingPreorder(self, node):
        res = []
        if node == None:
            return res
        res.append(node.value)
        if node.left != None:
            res += self.DFSUsingPreorder(node.left)
        if node.right != None:
            res += self.DFSUsingPreorder(node.right)
        return res

    def DFSUsingInorder(self, node):
        res = []
        if node == None:
            return res
        if node.left != None:
            res += self.DFSUsingInorder(node.left)
        res.append(node.value)
        if node.right != None:
            res += self.DFSUsingInorder(node.right)
        return res

    def DFSUsingPostorder(self, node):
        res = []
        if node == None:
            return res
        if node.left != None:
            res += self.DFSUsingPostorder(node.left)
        if node.right != None:
            res += self.DFSUsingPostorder(node.right)
        res.append(node.value)
        return res






tree = Tree();
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

print(tree.preorderTraversal())
print(tree.BFSUsingIterate())
print(tree.BFSUsingRecursive([tree.root]))

print(tree.DFSUsingPreorder(tree.root))
print(tree.DFSUsingInorder(tree.root))
print(tree.DFSUsingPostorder(tree.root))





