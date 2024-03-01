def fibonacci(n):
    #write your code here         
    if n < 0 :
        return -1
    elif n == 0 :
        return 0
    elif n == 1 :
        return 1
    else : 
        fib = [0, 1]
        for n in range(2, n + 1):
            fib.append(fib[n - 1] + fib[n - 2])
        return fib[n]
        
if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')