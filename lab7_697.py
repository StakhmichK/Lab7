def reverse_sequence():
    x = int(input("Enter number: "))
    if x == 0:
        print() 
        print(0)
        return
    reverse_sequence()
    print(x)
reverse_sequence()