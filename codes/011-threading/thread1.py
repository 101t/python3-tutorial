import time
import threading
import logging

def thread_function(name):
	logging.info("Starting Thread %s" % name)
	time.sleep(3)
	logging.info("Ending Thread %s" % name)


if __name__ == '__main__':
	logging.basicConfig(format="%(asctime)s %(message)s", level=logging.INFO, datefmt="%H:%M:%S")
	x = threading.Thread(target=thread_function, args=("Hi",), daemon=True)
	#thread_function("Hi")
	x.start()