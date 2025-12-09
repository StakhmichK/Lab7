def first_last(nums):
    return [nums[0], nums[-1]]

line = input("Enter your numbers: ").split()
numbers = list(map(int, line))
result = first_last(numbers)
print("Your result is: ",result)