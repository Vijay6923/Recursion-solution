def min_screens(x, y):
    screens_for_y = (y + 1) // 2
    remaining_cells_after_y = (screens_for_y * 15) - (y * 4)
    x_left = max(0, x - remaining_cells_after_y)
    screens_for_x = (x_left + 14) // 15
    total_screens = screens_for_y + screens_for_x
    return total_screens

def main():
    t = int(input())
    results = []
    for _ in range(t):
        x, y = map(int, input().split())
        results.append(min_screens(x, y))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
