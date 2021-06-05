lead_pattern1 = P[_, _, (2,4,7), (2,4,7), _, _, (5,8,11), (5,8,11)]

lead_pattern2 = P[_, _, (4,6,8), (4,6,8), _, _, (7,9,11), (7,9,11)]

lead_pattern3 = P[_, _, (7,9,11), (7,9,11), _, _, (2,4,7), (2,4,7)]

lead_pattern4 = P[_, _, ((5,8,11), 5,8,11), _, _, (7,9,11), (7,9,11)]

lp1 = [lead_pattern1, lead_pattern2, lead_pattern3, lead_pattern4]

p1 >> marimba(Pvar([lp1[0], lp1[1]], 4), dur=0.5, sus=0.25, oct=5)


p1 >> marimba(Pvar([lp1[0], lp1[1]], 8), dur=0.5, sus=0.25, oct=5)

p1 >> star(Pvar([lp1[2], lp1[3]], 8), dur=0.5, sus=1, oct=5)

p1 >>   saw(Pvar([lp1[3], lp1[1]], 8), dur=0.5, sus=0.25, oct=5)

p1 >> marimba(Pvar([lp1[1], lp1[2]], 8), dur=0.5, sus=0.5, oct=5)

def lead_change(a=0):
    if a%3 == 0:
        p1 >> marimba(Pvar([lp1[0], lp1[1]], 4), dur=0.5, sus=0.1, oct=5)
        # print("change 3")
    if a%5 == 0:
        p1 >>  marimba(Pvar([lp1[2], lp1[3]], 4), dur=0.5, sus=0.1, oct=5)
        # print("change 5")
    if a%7 == 0:
        p1 >> marimba(Pvar([lp1[3], lp1[0]], 4), dur=0.5, sus=0.1, oct=5)
        # print("change 7")
    if a%13 == 0:
        p1 >> marimba(Pvar([lp1[1], lp1[2]], 4), dur=0.5, sus=0.1, oct=5)
        print("change 13")        


bass_pattern1 = P[7, 9, 2, 4, _, 7, 2, 2]

bass_pattern2 = P[4, 9, _, 4, _, 7, 6, 2]

bass_pattern3 = P[0, 2, 5, 5, _, 4, 4, 2]

bass_pattern4 = P[4, 6, _, 4, _, 0, 4, 0]


bass_01_pitch = P[_,9,_,9,9,16,12]
bass_01_dur = P[1,0.75,0.25,0.5,0.5,0.5,0.5]

bass_02_pitch = P[16,16,11,_,]
bass_02_dur = P[1,1,1.5,0.5]

bass_03_pitch = P[16,16,11,11]
bass_03_dur = P[1,1,1,1]

bass_04_pitch = P[15,16,16,11,11]
bass_04_dur = P[0.5,0.5,1,1,1]

        
bass_pitch_pattern = [bass_01_pitch, bass_02_pitch, bass_03_pitch, bass_04_pitch]  
bass_dur_pattern = [bass_01_dur, bass_02_dur, bass_03_dur, bass_04_dur]  


number = var([0,1,0,2,0,3], 4)
print(number)
        
        
def bass_change(a=0):
    while a == int(number):
        pass
    else:    
        a = int(number)
        print(a)
        p2 >> bass(bass_pitch_pattern[int(number)], dur=bass_dur_pattern[int(number)], oct=4, amp=0.5)



var.counter = var(0)
var.counter1 = var(0)

@PlayerMethod
def test(self, a = 0):
    lead_change(a)
    var.counter += 1
    print("lead: ", var.counter)

@PlayerMethod
def test0(self, a = 0):
    bass_change(a)
    var.counter1 += 1
    print("bass: ", var.counter1)

p3 >> play("Xx__").every(4, "test", var.counter)

p4 >> play("-t-t").every(4, "test0", var.counter1)

# And cancel it with
p3.never("test")

p4.never("test0")
