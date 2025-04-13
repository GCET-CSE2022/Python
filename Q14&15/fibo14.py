def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    series = []
 
    if n >= 0:
        series.append(0)  # F(0) = 0
    if n >= 1:
        series.append(1)  # F(1) = 1
    
    # Generate the Fibonacci series for n > 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        series.append(b)
    
    return series
