def max_pages_per_test_case(n, pages):
    # Sort the pages in descending order
    pages.sort(reverse=True)
    # The maximum sum of pages Alice can read is the sum of the two largest values
    return pages[0] + pages[1]

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        pages = list(map(int, data[index:index+n]))
        index += n
        results.append(max_pages_per_test_case(n, pages))
    
    for result in results:
        print(result)

# Example usage:
if __name__ == "__main__":
    main()
