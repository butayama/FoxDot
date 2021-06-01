pattern1 = P[0, 1, 2, 3]
pattern2 = P[4, 5, 6, 7]

def change(a=0):
    if a%7 == 0:
        p1 >> pluck(Pvar([pattern1, pattern2], 4), dur=1/4)
    if a%13 == 0:
        p1 >> pluck(var([pattern1, pattern2], 4), dur=1/4)
        
var.counter = var(0)

@PlayerMethod
def test(self, a = 5):
    change(a)
    var.counter += 1
    print(var.counter)

@PlayerMethod
def test0(self):
    print(self.degree)

p1 >> pluck([0,4]).every(4, "test0")

p1 >> pluck([0,4,2]).every(4, "tset0", 4)

p2 >> pluck([[0,4,2],(2,5,7)]).every(4, "test", 0)

# And cancel it with
p2.never("test")

p1.never("test0")



