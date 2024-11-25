stack=[]
def push():
    if len(stack)==stack_limit:
        print("!! stack is full !!")
        print(stack)
        else:
        elmt=int(input("enter the element:"))
        stack.append(elmt)
        print(stack)
        def pop():
            if not stack:
                print("stack is empty")
                else:
                p_elmt=stack.pop()
                print("removed element:",p_elmt)
                print("current stack:",stack)

