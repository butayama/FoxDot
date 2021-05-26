def verse():
    b1 >> bass([0,3], dur=4)
    p1 >> pluck([0,4], dur=1/2)
    d1 >> play("x--x--x-")
    Clock.future(16, chorus)
def chorus():
    b1 >> bass([0,4,5,3], dur=4)
    p1 >> pluck([0,4,7,9], dur=1/4)
    d1 >> play("x-o-")
    Clock.future(16, verse)
verse()   

TimeVar syntax var([list_of_values],[list_of_durations])

@PlayerMethod
def test(self):
    print(self.degree)

def f1():
    p1 >> pluck([0,4], dur=[2]).every(3, "test")
    
def f2():
    p1 >> pluck([6,2], dur=[1]).every(3, "test")


print(Clock)

print(Clock.latency)

a = Clock.now()

Clock.schedule(lambda: f1(), a + 4)

Clock.schedule(lambda: f2(), a + 8)


Clock.future(4, lambda: print("hello"))


# Tutorial 13: Advanced Clock

# To see what is scheduled to be played.
print(Clock)

# To see what the latency is
print(Clock.latency)

# The clock can schedule anything with a __call__ method using
# It takes an absolute time clue to schedule a functions
# Clock.schedule needs to know the beat to call something on
Clock.schedule()   # raises TypeError

# Schedule an event after a certain durations
# Clock.future needs to know how many beats ahead to call something
Clock.future()     # raises TypeError

# These are equivalent
Clock.schedule(lambda: print("hello"), Clock.now() + 4)
Clock.future(4, lambda: print("hello"))

# To schedule something else
Clock.schedule(lambda: print("hello "))

# We can call something every n beats
Clock.every(4, lambda: print("hello"))

# Get the current clock and add 2.  Useful for scheduling.
print(Clock.now() + 2)

# Issue command on the next bar
nextBar(Clock.clear)

# With a decorator
@nextBar
def change():
    Root.default=4
    Scale.default="minor"
    # etc etc

# You can create your own function, and decorate it, to be able
# to use it in an .every on a Player object
@PlayerMethod
def test(self):
    print(self.degree)

p1 >> pluck([0,4]).every(3, "test")

# And cancel it with
p1.never("test")
