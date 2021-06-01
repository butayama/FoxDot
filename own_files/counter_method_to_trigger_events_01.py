lead_pattern1 = P[_, 2, _, 5, _, 5, _, 2]

lead_pattern2 = P[_, 4, _, 4, _, 7, _, 7]

lead_pattern3 = P[_, 7, _, 7, _, 2, _, 2]

lead_pattern4 = P[_, 5, _, 5, _, 7, _, 7]

bass_pattern1 = P[7, 9, 2, 4, _, 7, 2, 2]

bass_pattern2 = P[4, 9, _, 4, _, 7, 6, 2]

bass_pattern3 = P[0, 2, 5, 5, _, 4, 4, 2]

bass_pattern4 = P[4, 6, _, 4, _, 0, 4, 0]

def lead_change(a=0):
    if a%3 == 0:
        p1 >> nylon(Pvar([lead_pattern1, lead_pattern2], 4), dur=0.5, sus=0.25, oct=5)
        # print("change 3")
    if a%5 == 0:
        p1 >> star(Pvar([lead_pattern3, lead_pattern4], 4), dur=0.5, sus=0.25, oct=5)
        # print("change 5")
    if a%7 == 0:
        p1 >> saw(Pvar([lead_pattern2, lead_pattern4], 4), dur=0.5, sus=0.25, oct=5)
        # print("change 7")
    if a%13 == 0:
        p1 >> pads(Pvar([lead_pattern3, lead_pattern2], 4), dur=0.5, sus=0.25, oct=5)
        # print("change 13")        
        
def bass_change(a=0):
    if a%3 == 0:
        p2 >> dub(Pvar([bass_pattern1, bass_pattern2], 4), dur=0.5, oct=4)
        # print("bass 3")  
    if a%5 == 0:
        p2 >> soft(Pvar([bass_pattern1.shuffle(), bass_pattern3.shuffle()], 4), dur=0.5)
        # print("bass 5")   
    if a%7 == 0:
        p2 >> dbass(Pvar([bass_pattern1.reverse(), bass_pattern4.shuffle()], 4), dur=0.5)
        # print("bass 7")
    if a%13 == 0:
        p2 >> sawbass(Pvar([bass_pattern3.shuffle(), bass_pattern4.reverse()], 4), dur=0.5)
        # print("bass 13")         

var.counter = var(0)
var.counter1 = var(2)

@PlayerMethod
def test(self, a = 5):
    lead_change(a)
    var.counter += 1
    print("lead: ", var.counter)

@PlayerMethod
def test0(self, a = 5):
    bass_change(a)
    var.counter1 += 1
    print("bass: ", var.counter1)

p3 >> play("Xx__").every(4, "test", var.counter)

p4 >> play("-t-t").every(4, "test0", var.counter1)

# And cancel it with
p2.never("test")

p1.never("test0")
