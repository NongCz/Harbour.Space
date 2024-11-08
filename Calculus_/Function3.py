def gradient_descent_f3(learning_rate=0.1, max_iterations=100):
    
    def f(x, y):
        return (x - 2)**2 + 2*(y - 3)**2

    def df_dx(x, y):
        return 2*(x - 2)

    def df_dy(x, y):
        return 4*(y - 3)

    x, y = 0, 0  
    for _ in range(max_iterations):
        x = x - learning_rate * df_dx(x, y)
        y = y - learning_rate * df_dy(x, y)

    return x, y, f(x, y)  

min_x, min_y, min_value = gradient_descent_f3()
print(f"Minimum point: x = {min_x}, y = {min_y}, f(x, y) = {min_value}")
