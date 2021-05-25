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

p1 >> pluck([0,4]).every(3, "test")

p1.never("test")

print(Clock)

print(Clock.latency)

Clock.schedule(lambda: print("hello"), Clock.now() + 4)

Clock.future(4, lambda: print("hello"))
