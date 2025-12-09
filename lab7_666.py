def sort_by_length(line):
    words = line.split()
    words_sorted = sorted(words, key=len)
    return " ".join(words_sorted)

line = input("Enter your statement: ")
result = sort_by_length(line)
print(result)  