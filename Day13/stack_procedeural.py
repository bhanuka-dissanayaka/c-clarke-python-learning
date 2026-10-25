stack = [] #Stack is a last in first out data structure - LIFO

def push(elem):
    stack.append(elem)

def pop():
    if len(stack) != 0:
        last_data = stack[-1]
        del stack[-1]
        return last_data
    print("NO data to delete")
    return None

if __name__ == "__main__":
    data = input("Input :")
    push(elem=data)

    pop()