import threading


class Counter(threading.Thread):
    counter = 0  # Shared global counter variable
    rounds = 100000  # Number of increments each thread will perform

    def run(self):
        for _ in range(self.rounds):
            Counter.counter += 1  # Increment the shared counter


thread1 = Counter()
thread2 = Counter()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"The final counter value is: {Counter.counter}")

# Final counter value is: 200000
