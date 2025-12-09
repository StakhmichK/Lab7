def reverse_sequence():
    x = int(input())
    if x == 0:
        print() 
        print(0)
        return
    reverse_sequence()
    print(x)
reverse_sequence()