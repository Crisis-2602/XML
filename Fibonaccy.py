import keyboard
import time

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
fib = fibonacci()
stop = False
print("Presiona ESC para detener la serie de Fibonacci.")
while not stop:
    try:
        if keyboard.is_pressed('esc'):
            stop = True
            print("Serie de Fibonacci detenida.")
    except:
        pass
    if not stop:
        time.sleep(1)
        print(next(fib))