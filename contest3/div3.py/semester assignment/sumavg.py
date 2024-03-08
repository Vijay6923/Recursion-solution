# from collections import Counter

# def print_statistics(numbers):
#     min_num = min(numbers)
#     max_num = max(numbers)
#     sum_num = sum(numbers)
#     avg_num = sum_num / len(numbers)
#     mode_num = Counter(numbers).most_common(1)[0][0]
    
#     print(f"min, max, sum, average and mode after addition of {numbers[-1]} is {min_num}, {max_num}, {sum_num}, {avg_num}, {mode_num}.")

# def main():
#     n = int(input("Enter the number of elements in the stream: "))
#     stream = list(map(int, input("Enter the stream of numbers: ").split()))

#     numbers = []
#     for i in range(n):
#         numbers.append(stream[i])
#         print_statistics(numbers)

# if __name__ == "__main__":
#     main()
from collections import Counter

def print_statistics(lst):
    if not lst:
        return "No elements in the list."
    
    minimum = min(lst)
    maximum = max(lst)
    total = sum(lst)
    average = total / len(lst)
    mode = Counter(lst).most_common(1)[0][0]
    
    return f"min, max, sum, average and mode after addition of {lst[-1]} is {minimum}, {maximum}, {total}, {average}, {mode}."

def main():
    lst = []
    n = int(input("Enter the number of elements in the stream: "))
    stream = list(map(int, input("Enter the stream of numbers separated by space: ").split()))
    
    for num in stream:
        lst.append(num)
        print(print_statistics(lst))

if __name__ == "__main__":
    main()
