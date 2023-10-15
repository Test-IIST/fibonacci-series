
# #always output through testIO.print() and sure to return testIO 
# def runner(testIO,n):
#     ## Enter Student code in this block
#     testIO.print(" ")                  
#     ##
#     return testIO
def generate_fibonacci(testIO, N):
    fib_sequence = []
    a, b = 0, 1
    for _ in range(N):
        fib_sequence.append(a)
        a, b = b, a + b
    testIO.print(",".join(map(str, fib_sequence)))
    return testIO

def runner(testIO, N):
    return generate_fibonacci(testIO, N)
