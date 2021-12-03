class Stack:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.elements = [None] * self.maxsize
        self.top = -1

    '''
        push(data):
        1. Check whether the stack is full. If full, display appropriate message
        2. If not,
        a. increment top by one
        b. Add the element at top position in the elements array

    '''

    def isfull(self):
        if self.top == self.maxsize - 1:
            return True
        return False

    def push(self,data):
        if self.isfull():
            return "Stack is full"
        else:
            self.top +=1
            self.elements[self.top] = data
            return f"Element {data} has been inserted at position {self.top}"

    def isempty(self):
        if self.top == -1:
            return True
        return False

    def pop(self):
        if self.isempty():
            return "Stack is empty"
        else:
            data = self.elements[self.top]
            self.top -= 1
            return f"Element {data} has been popped from the stack"

    def display(self):
        if self.isempty():
            return "Stack is empty...nothing to display"
        else:
            index = self.top
            while index >= 0:
                print(self.elements[index])
                index -= 1


if __name__ == "__main__":
    mystack = Stack(2)
    while True:

        print("\select an option: ")
        print("1.Push ; 2.Pop; 3.Size of Stack; 4.Display; 5.Exit")

        do = int(input("enter your choice: "))

        if do==1:
            data = int(input("Enter element to be inserted: "))
            result = mystack.push(data)
            print(result)

        elif do==2:
            result = mystack.pop()
            print(result)

        elif do==3:
            print(f"Maxsize of stack is {mystack.maxsize}")

        elif do==4:
            result = mystack.display()
            print(result)

        elif do==5:
            print("Program exited.....")
            exit()

        else:
            print("Choose correct option....")



# mystack = Stack(2)
# print(mystack.push(67))
# print(mystack.push(1))
# print(mystack.push(6))
# print(mystack.pop())
