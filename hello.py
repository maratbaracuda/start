def print_hello():
    print("Hello")
class Stack():
    def __init__(self, lst = None):
        if lst is None:
            lst = []
        self.lst = lst

if __name__ == '__main__':
    print_hello()
    stack = Stack([1, 2, 3])
    print(stack.lst)