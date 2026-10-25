class Stack:

    def __init__(self): #constructor
        self.stack_List = []

    def push(self, elem): #We call these methods, functions inside a class
        self.stack_List.append(elem)

    def pop(self):
        if len(self.stack_List) > 0:
            val = self.stack_List[-1]
            del self.stack_List[-1]
            return val

        else:
            print("Stack is empty")

book_stack = Stack()
book_stack.push("Madol Duwa")
book_stack.push("Gaga Addara")
book_stack.pop()

game_stack = Stack()
game_stack.push("GTA")
game_stack.push("assian")
book_stack.pop()