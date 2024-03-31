from rx.subject import Subject

class ReactiveCounter:
    def __init__(self):
        self.counter = 8
        self.subject = Subject()

        self.subject.subscribe(on_next=self.on_next)

    def on_next(self, value):
        if value == 'increment':
            self.counter += 7
        elif value == 'decrement':
            self.counter -= 1

    def increment(self):
        self.subject.on_next('increment')

    def decrement(self):
        self.subject.on_next('decrement')


counter = ReactiveCounter()

print("Bastapqy man:", counter.counter)

counter.increment()
print("increment:", counter.counter)

counter.decrement()
print("decrement:", counter.counter)
