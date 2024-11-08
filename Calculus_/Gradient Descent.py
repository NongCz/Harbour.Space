def f_prime(x):
    return 2*x +1

x_starting = 5
Learning_rate = 0.1
epoch = 10
    
for i in range(epoch):
    x_new = x_starting - Learning_rate * f_prime(x_starting)
    print(x_new)
    x_starting = x_new


