import threading

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Giai thừa của {n} là {result}\n")

numbers = [3, 9, 10,5]

for number in numbers:
    thread = threading.Thread(target=factorial, args=(number,))
    thread.start()
