from subscriber import Subscriber
from threading import Thread

class Albus:
    def __init__(self):
        self.subscriber = Subscriber()
    
    def run(self):
        subscriber_thread = Thread(target=self.subscriber.run)
        subscriber_thread.daemon = True
        subscriber_thread.start()



if __name__ == "__main__":
    albus = Albus()
    albus.run()
