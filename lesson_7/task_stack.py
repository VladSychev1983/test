class Stack:
    def __init__(self) -> None:
        self.stack_list: list = []
        self.open_brackets = ["[","{","("]
        self.close_brackets = ["]","}",")"]
    
    def is_empty(self):
        return False if len(self.stack_list) > 0 else True
    
    def push(self,item):
        self.stack_list.append(item)

    def pop(self):
        item = self.stack_list.pop(-1)
        return item
    
    def peek(self):
        last_item = self.stack_list[-1]
        return last_item
    
    def size(self):
        return len(self.stack_list)
    
    def check_brackets(self, brakets):
        for i in brakets:
            if i in self.open_brackets:
                self.push(i)
            elif i in self.close_brackets:
                pos = self.close_brackets.index(i)
                if(self.is_empty() == False) and \
                    (self.open_brackets[pos] == self.peek()):
                    self.pop()
                else:
                    return 'Not Balanced'
        return "Balanced" if self.size() == 0 else "Not Balanced"

myobj = Stack()

print(myobj.check_brackets('(((([{}]))))'))
print(myobj.check_brackets('[([])((([[[]]])))]{()}'))
print(myobj.check_brackets('{{[()]}}'))
print("")
print(myobj.check_brackets('{{[(])]}}'))
print(myobj.check_brackets('[[{())}]'))
print(myobj.check_brackets('}{}'))