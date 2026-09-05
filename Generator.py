'''#def square_gen(n):
    for i in range(n):
        yield i * i

# example usage:
# for val in square_gen(5):
#     print(val)'''

'''def squares(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

print(squares(5))'''

def fibonacci_gen(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for num in fibonacci_gen(10):        
    print(num)
    