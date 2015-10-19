from array import *

class Stack:

    def __init__(self,size):
        self.stack_a = []
        if size > 0:
            self.stack_a.extend([None]*size)
        self.top = 0

    def empty(self):
        return self.stack_a[0] is None

    def printList(self):
        if self.empty():
            print "the list is empty"
        else:
            print "The list has:",
            for item in das_stack.stack_a:
                print item,
            print ""


    def push(self, item):
        if self.empty():
            self.stack_a[self.top] = item
        else:
            if self.top >= len(self.stack_a):
                self.stack_a.append(item)
            else:
                self.stack_a[self.top + 1] = item
            self.top = self.top + 1

        print item,
        print " was added to the stack"

    def pop(self):
        if self.empty():
            return "Error"

        element_to_pop = self.stack_a[self.top]
        self.stack_a[self.top] = None
        self.top -= 1

        print element_to_pop,
        print " was popped"
        return element_to_pop

    def peek(self):
        print "Peepin',",
        print self.stack_a[self.top]



das_stack = Stack(5)

das_stack.printList()

das_stack.push("lol")
das_stack.push("rofl")

das_stack.printList()

das_stack.pop()

das_stack.printList()

das_stack.peek()

# print das_stack.top
# print das_stack.stack_a[0]
# print das_stack.empty()
# print das_stack.stack_a
# print das_stack.top
