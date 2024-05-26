def max_expression_value(a, b, c):
    # Calculate all possible values
    result1 = a + b + c
    result2 = a * b * c
    result3 = (a + b) * c
    result4 = a * (b + c)
    result5 = a + (b * c)
    result6 = (a * b) + c
    
    # Find and return the maximum value
    return max(result1, result2, result3, result4, result5, result6)
 
# Example usage
a = int(input())
b = int(input())
c = int(input())
 
print(max_expression_value(a, b, c))