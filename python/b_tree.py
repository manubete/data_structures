class Node:
  def __init__(self,left,right,data):
    if data is None:
      self.data = None
    else:
      self.data = data

    if left is None:
        self.left = None
    else:
        self.left = left

    if right is None:
        self.right = None
    else:
        self.right = right

  def getLeftChild(self):
    return self.left

  def setLeftChild(self,node):
    self.left = node

  def getRightChild(self):
    return self.right

  def setRightChild(self,node):
    self.right = node

  def getData(self, level):
    print ("  |-- "*level) + "%r" % self.data


def inOrderTraversal(node, level):
  if node != None:
    inOrderTraversal(node.getLeftChild(), level + 1)
    node.getData(level)
    inOrderTraversal(node.getRightChild(), level + 1)

def preOrderTraversal(node, level):
  node.getData(level)
  if node.left != None:
    preOrderTraversal(node.getLeftChild(), level + 1)
  if node.right != None:
    preOrderTraversal(node.getRightChild(), level + 1)

def pos

##### TEST DRIVERS #######

nuNode = Node(None,None,"root")

nuLNode = Node(None,None,"left")
nuRNode = Node(None,None,"right")

nuNode.setLeftChild(nuLNode)
nuNode.setRightChild(nuRNode)

print 'INORDER' + "--"*10
inOrderTraversal(nuNode,0)

print 'PREORDER' + "--"*10
preOrderTraversal(nuNode,0)


