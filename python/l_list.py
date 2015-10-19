class Node:

    def __init__(self, data, nextNode):
        if data is not None:
            self.data = data
        else:
             self.data = None

        if nextNode is not None:
            self.nextNode = nextNode
        else:
            self.nextNode = None

    def appendToTail(self, node):
        nodeToAppend = node
        tailNode = self

        while tailNode.nextNode is not None:
            tailNode = tailNode.nextNode

        tailNode.nextNode = nodeToAppend

    def printNodes(self):
        currentNode = self

        while currentNode is not None:

            if currentNode.nextNode is not None:
                print "Node: %s ->" % currentNode.data,
            else:
                print "Node: %s" % currentNode.data

            currentNode = currentNode.nextNode


das_list = Node("wunderbar", None)

das_list.printNodes()

yo = Node("yo", None)

das_list.appendToTail(yo)

das_list.printNodes()
