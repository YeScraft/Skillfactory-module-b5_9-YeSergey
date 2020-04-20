import sys

def Stopwatch(NUM_RUNS = 10):
    def decorator(func):
        import time
        def wrapper(number):
            avg_time = 0
            for _ in range(NUM_RUNS):
                t0 = time.time()
                func(number)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= NUM_RUNS
            return "Выполнение в среднем заняло %.5f секунд" % avg_time
        return wrapper
    return decorator

def main(number, i):
    @Stopwatch(i)
    def fibonacci(number):
        c = [1]
        n = 2
        i = 1
        while n < number:
            c.append(n)
            n = c[i-1]+c[i]
            i+=1
        print (sum(c))

    print(fibonacci(number))

if __name__ == "__main__":
    if len(sys.argv) > 1:# Выбор вывода: по умолчанию, либо с введением параметров.
        main(number = int(sys.argv[1]), i = int(sys.argv[2]))
    else:
        main(number = 4000000, i = 3)

""" 
Запуск в cmd:
"python hw_5_9_function.py"               - для вывода c значениями по умолчанию,
"python hw_5_9_function.py number i"      - для вывода с введением параметров (целочисленные значения)."""