def gradient_descent_f1(learning_rate=0.1, max_iterations=100):
    
    def f(x):
        return x**2 + x + 1

    def df(x):  
        return 2*x + 1

    x = 0  
    for _ in range(max_iterations):
        x = x - learning_rate * df(x)  

    return x, f(x)  


min_x, min_value = gradient_descent_f1()
print(f"Minimum point: x = {min_x}, f(x) = {min_value}")