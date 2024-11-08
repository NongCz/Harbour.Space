def gradient_descent_general_2d(func_expr, var_symbols, learning_rate=0.1, max_iterations=100):
    x, y = var_symbols
    
    grad_x_expr = sp.diff(func_expr, x)
    grad_y_expr = sp.diff(func_expr, y)
    
    grad_x = sp.lambdify([x, y], grad_x_expr)  
    grad_y = sp.lambdify([x, y], grad_y_expr)  
    func = sp.lambdify([x, y], func_expr)      
    
    x_val, y_val = 0, 0  
    for _ in range(max_iterations):
        x_val = x_val - learning_rate * grad_x(x_val, y_val)
        y_val = y_val - learning_rate * grad_y(x_val, y_val)

    return x_val, y_val, func(x_val, y_val)  

x, y = sp.symbols('x y')
func_expr = (x - 2)**2 + 2*(y - 3)**2
min_x, min_y, min_value = gradient_descent_general_2d(func_expr, (x, y))
print(f"Minimum point: x = {min_x}, y = {min_y}, f(x, y) = {min_value}")
