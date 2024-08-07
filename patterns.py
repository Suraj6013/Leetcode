n=5
def pattern1():
    for i in range(n):
        print('*' * n)
pattern1()

def pattern2():
    for i in range(1, n+1):
        print('*' * i)
pattern2()

def pattern3():
    for i in range(n, 0, -1):
        print('*' * i)
pattern3()