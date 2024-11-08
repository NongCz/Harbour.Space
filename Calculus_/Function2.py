import sympy as sp

def gradient_descent_general_1d(func_expr, var_symbol, learning_rate=0.1, max_iterations=100):
    
    grad_expr = sp.diff(func_expr, var_symbol)
    grad = sp.lambdify(var_symbol, grad_expr)
    func = sp.lambdify(var_symbol, func_expr)  
    
    x = 0  
    for _ in range(max_iterations):
        x = x - learning_rate * grad(x)  

    return x, func(x)  

x = sp.symbols('x')
func_expr = x**2 + x + 1
min_x, min_value = gradient_descent_general_1d(func_expr, x)
print(f"Minimum point: x = {min_x}, f(x) = {min_value}")
