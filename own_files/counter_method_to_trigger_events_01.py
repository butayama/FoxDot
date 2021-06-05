from collections import deque

lead_pattern1 = P[_, 2, _, 5, _, 5, _, 2]

lead_pattern2 = P[_, 4, _, 4, _, 7, _, 7]

lead_pattern3 = P[_, 7, _, 7, _, 2, _, 2]

lead_pattern4 = P[_, 5, _, 5, _, 7, _, 7]

bass_pattern1 = P[7, 9, 2, 4, _, 7, 2, 2]

bass_pattern2 = P[4, 9, _, 4, _, 7, 6, 2]

bass_pattern3 = P[0, 2, 5, 5, _, 4, 4, 2]

bass_pattern4 = P[4, 6, _, 4, _, 0, 4, 0]

bass_01_pitch = P[_,9,_,9,9,16,12]
bass_01_dur = P[1,0.75,0.25,0.5,0.5,0.5,0.5]

p1 >> pluck([0, 1, 2, 3, 4, 5, 6, 7]).every(PRand([2, 4, 8]), "reverse")

d1 >> pluck([0, 1, 2, 3, 4, 5, 6, 7]).every(8, "reverse").every(5, "reverse", ident=1)

bass_test_pitch = deque[0,9,0,9,9,16,12]

for x in bass_test_pitch):
    print(x)
    
print(bass_test_pitch[1])

bass_02_pitch = P[16,16,11,_,]
bass_02_dur = P[1,1,1.5,0.5]

bass_03_pitch = P[16,16,11,11]
bass_03_dur = P[1,1,1,1]

bass_04_pitch = P[15,16,16,11,11]
bass_04_dur = P[0.5,0.5,1,1,1]

def lead_change(a=0):
    if a%3 == 0:
        p1 >> nylon(Pvar([lead_pattern1, lead_pattern2], 4), dur=0.5, sus=0.25, oct=5)
        # print("change 3")
    if a%5 == 0:
        p1 >> star(Pvar([lead_pattern3, lead_pattern4], 4), dur=1, sus=1, oct=5)
        # print("change 5")
    if a%7 == 0:
        p1 >> saw(Pvar([lead_pattern2, lead_pattern4], 4), dur=0.5, sus=0.25, oct=5)
        # print("change 7")
    if a%13 == 0:
        p1 >> bug(Pvar([lead_pattern3, lead_pattern2], 4), dur=0.5, sus=0.5, oct=5)
        print("change 13")        
        
bass_pitch_pattern = P[bass_01_pitch, bass_02_pitch, bass_01_pitch, bass_03_pitch, bass_01_pitch, bass_04_pitch]  
bass_dur_pattern = P[bass_01_dur, bass_02_dur, bass_01_dur, bass_03_dur, bass_01_dur, bass_04_dur]  

print(bass_pitch_pattern)

p2 >> dub(bass_pitch_pattern[0], dur=bass_dur_pattern[0], oct=4)

p1 >> bass(var([0,4,5,3],4), dur=2)
p2 >> pads().follow(p1) + [2,4,7] 

p2 >> pads().follow(b1).every(4, "rotate", 2) + [2, 4, 7]

You could then also do:

p3 >> pluck().follow(p2).every(4, "rotate", 2) + [0, 1, 2, 3]

number = var([1,2,1,3,1,4], 4)
print(number)
        
def bass_change(a=0):
    if number == 1:
        p2 >> bass(bass_01_pitch, dur=bass_01_dur, oct=4)
    elif number == 2:
        p2 >> bass(bass_02_pitch, dur=bass_02_dur, oct=4)    
    elif number == 3:
        p2 >> bass(bass_03_pitch, dur=bass_03_dur, oct=4) 
    elif number == 4:
        p2 >> bass(bass_04_pitch, dur=bass_04_dur, oct=4) 


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
p3.never("test")

p4.never("test0")
