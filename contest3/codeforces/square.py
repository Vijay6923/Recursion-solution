def calculate_square_area(x_coords, y_coords):
    max_x = max(x_coords)
    min_x = min(x_coords)
    max_y = max(y_coords)
    min_y = min(y_coords)
    
    x_distance = max_x - min_x
    y_distance = max_y - min_y
    
    return max(x_distance, y_distance) ** 2


t = int(input())
for _ in range(t):
    x_coords = []
    y_coords = []
    for _ in range(4):
        x, y = map(int, input().split())
        x_coords.append(x)
        y_coords.append(y)
    print(calculate_square_area(x_coords, y_coords))
