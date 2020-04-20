import sys
import time

class Stopwatch():
    def __init__(self, NUM_RUNS=3):
        self.NUM_RUNS = NUM_RUNS

    def __enter__(self):
        return self
    
    def __call__(self, *args, **kwargs):
        self.func = args[0]
        self.mode = "calling"
        avg_time = 0
        for _ in range(self.NUM_RUNS):
            t0 = time.time()
            print(self.func)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= self.NUM_RUNS
        return "Выполнение в среднем заняло %.5f секунд" % avg_time

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self
    
def fibonacci(number):
    c = [1]
    n = 2
    i = 1
    while n < number:
        c.append(n)
        n = c[i-1]+c[i]
        i+=1
    return sum(c)

def main(number, i):
    with Stopwatch(i) as sw:
        print(sw((fibonacci(number))))

if __name__ == "__main__":
    if len(sys.argv) > 1:# Выбор вывода: по умолчанию, либо с введением параметров.
        main(number = int(sys.argv[1]), i = int(sys.argv[2]))
    else:
        main(number = 4000000, i = 3)

""" 
Запуск в cmd:
"python hw_5_9_with.py"               - для вывода c значениями по умолчанию,
"python hw_5_9_with.py number i"      - для вывода с введением параметров (целочисленные значения)."""