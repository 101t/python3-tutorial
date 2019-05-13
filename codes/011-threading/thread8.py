import threading
import logging

def my_function(name="Threading is Awesome"):
    logging.info(name)

if __name__ == '__main__':
    print("Welcome to threading with Timer")
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    x = threading.Timer(5.1, my_function)
    x.start()