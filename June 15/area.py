def find_area(i, j, n, a):
    
    if i < 0 or i >= n or j < 0 or j >= n or a[i][j] != 1:
        return 0
    a[i][j] = '0'
    
    area = 1
    area += find_area(i-1, j, n, a) 
    area += find_area(i+1, j, n, a)  
    area += find_area(i, j-1, n, a)  
    area += find_area(i, j+1, n, a)  
    
    return area

def count_islands_and_max_area(a):
    n = len(a)
    num_islands = 0
    max_area = 0
    
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                num_islands += 1
                current_area = find_area(i, j, n, a)
                max_area = max(max_area, current_area)
    
    return num_islands, max_area

a = [
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]


num_islands, max_area = count_islands_and_max_area(a)
print(f"Number of islands: {num_islands}")
print(f"Maximum area of an island: {max_area}")