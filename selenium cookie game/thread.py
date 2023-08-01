import threading

def hello_world():
    threading.Timer(6.0, hello_world).start() # called every minute
    print("Hello, World!")

hello_world()
print("hi")
hello_world()