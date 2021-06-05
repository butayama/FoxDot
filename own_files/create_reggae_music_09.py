# https://foxdot.org/docs/player-attributes/


# http://studio.dubroom.org/tutorials-computerdub07.htm
# THE NYABINGHI RHYTHM


def csr(bpm=140, scale="chromatic",root="C"):
    Clock.bpm = bpm
    Scale.default = scale
    Root.default = root
    return

cl >> play("cc00", dur=1, sample=(0), pan=-0.5,room=0.3, verb=0.3, sus=0.5)

cl.stop()

#  open hi conga
hc >> play(PEuclid2(1,8,'0','c'), dur=1, sample=(4), pan=-0.55,room=0.5, verb=0.3, sus=0.5)

hc.stop()

# bongo low
bl >> play("bb00", dur=1, sample=(0), pan=-0.25,room=0.3, verb=0.2, sus=0.5)

bl.stop()

# bongo hi
bh >> play("[bbb0][b000]0", dur=[1, 1, 6], sample=(0), pan=-0.3,room=0.5, verb=0.2, sus=0.5)

bh.stop()


# crash cymba
cc >> play(PEuclid2(1,16,'0','C'), dur=1, sample=(0), amp=0.2, pan=0.5,room=0.0, verb=0.0, sus=0.2)

cc.stop()

# cowbell
cb >> play("[T0T0][T000]0", dur=[1, 1, 6], sample=(1), amp=0.1, pan=0.3,room=0.3, verb=0.2, sus=0.5)

cb.stop()

# hi-mid-tom
ht >> play("00M", dur=[2, 0.6, 1.4], sample=(4), pan=0.2, room=0.5, verb=0.5, sus=2)

ht.stop()


# low-mid-tom
mt >> play("00M0", dur=[3, 5], sample=(1), pan=0.2, room=0.5, verb=0.5, sus=2)

mt.stop()

# open hi-hat
oh >> play("00=", dur=[0.1, 3.9, 4], sample=(1), pan=0.45, room=0.5, verb=0.5, sus=2)

oh.stop()

# low tom
lt >> play("0mm0", dur=[0.1, 3.5, 0.4, 4], sample=(0), pan=0.2, room=0.5, verb=0.5, sus=2)

lt.stop()

#  close hi-hat
ch >> play("00--", dur=1, sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5)

ch.stop()

#  bass drum
bd >> play("X000", dur=1, sample=(0), pan=0.4, room=0.7, verb=0.7, sus=3)

bd.stop()



def nyabinghi():
    #  low conga
    cl >> play("cc00", dur=1, sample=(0), pan=-0.5,room=0.3, verb=0.3, sus=0.5)

    #  open hi conga
    hc >> play(PEuclid2(1,8,'0','c'), dur=1, sample=(4), pan=-0.55,room=0.5, verb=0.3, sus=0.5)

    # bongo low
    bl >> play("bb00", dur=1, sample=(1), pan=-0.25,room=0.3, verb=0.2, sus=0.5)

    # bongo hi
    bh >> play("[bbb0][b000]0", dur=[1, 1, 6], sample=(0), pan=-0.3,room=0.5, verb=0.2, sus=0.5)

    # crash cymba
    cc >> play(PEuclid2(1,16,'0','C'), dur=1, sample=(0), amp=0.2, pan=0.5,room=0.0, verb=0.0, sus=0.2)

    # cowbell
    cb >> play("[T0T0][T000]0", dur=[1, 1, 6], sample=(1), amp=0.1, pan=0.3,room=0.3, verb=0.2, sus=0.5)

    # hi-mid-tom
    ht >> play("00M", dur=[2, 0.6, 1.4], sample=(4), pan=0.2, room=0.5, verb=0.5, sus=2)

    # low-mid-tom
    mt >> play("00M0", dur=[3, 5], sample=(1), pan=0.2, room=0.5, verb=0.5, sus=2)

    # open hi-hat
    oh >> play("00=", dur=[0.1, 3.9, 4], sample=(1), pan=0.45, room=0.5, verb=0.5, sus=2)

    # low tom
    lt >> play("0mm0", dur=[0.1, 3.5, 0.4, 4], sample=(0), pan=0.2, room=0.5, verb=0.5, sus=2)

    #  close hi-hat
    ch >> play("00--", dur=1, sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5)

    #  bass drum
    bd >> play("X000", dur=1, sample=(0), pan=0.4, room=0.7, verb=0.7, sus=3)

    nyabinghi = Group(cl,hc,bl,bh,cc,cb,ht,mt,oh,lt,ch,bd)
    return nyabinghi

# http://studio.dubroom.org/tutorials-computerdub15.htm

# ___________________________________________________________________________________________________________
# PROGRAMMING A BASIC DRUM RHYTHM
# ___________________________________________________________________________________________________________

    # open hi-hat
oh >> play("=", dur=[0.5], sample=(1), pan=0.45, room=0.5, verb=0.5, sus=0.5, amp=PStep(8, 1))
print(PStep(8, 1))

def drum_rhythm():
    #  close hi-hat
    ch >> play("-", dur=0.5, sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5, amp=[1, 0.4])

    # open hi-hat
    oh >> play("=", dur=[0.5], sample=(1), pan=0.45, room=0.5, verb=0.5, sus=0.5, amp=PStep(8, 1))
    print(PStep(8, 1))

    # snare drum
    sd >> play("0i", dur=[2.0, 2.0], sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5, amp=1)

    # kick drum
    kd >> play("XXxXXx", dur=[2.0, 1.5, 0.5, 2.0, 1, 1], sample=(1), pan=0.45, room=0.5, verb=0.5, sus=0.5, amp=[1])
    drum_rhythm = Group(ch,oh,sd,kd)
    return drum_rhythm

# http://studio.dubroom.org/tutorials-computerdub16.htm
# ___________________________________________________________________________________________________________
# PROGRAMMING A BASSLINE ON TWO PIANO CHORDS
# ___________________________________________________________________________________________________________


def piano_rhythm():
    # melodic A Chord (piano synth is not recognized)
    pa >> prophet([_,(9,12,16),_,(9,12,16),_,_], dur=[rest(1),0.25,rest(1.75),0.25,rest(0.75),rest(4)], oct=5, pan=-0.2, room=0.5, verb=0.5, sus=0.15, amp=[2])
    # melodic E Chord (piano synth is not recognized)
    pe >> prophet([_,(4,7,11),_,(4,7,11),_], dur=[rest(5),0.25,rest(1.75),0.25,rest(0.75)], oct=5, pan=-0.2, room=0.5, verb=0.5, sus=0.15, amp=[2])
    piano_rhythm = Group(pa, pe)
    return piano_rhythm
    
bass_01 = Player()
bass_02 = Player()
bass_03 = Player()
bass_04 = Player()

bass_01_pitch = [_,9,_,9,9,16,12]
bass_01_dur = [1,0.75,0.25,0.5,0.5,0.5,0.5]

bass_02_pitch = [16,16,11,_,]
bass_02_dur = [1,1,1.5,0.5]

bass_03_pitch = [16,16,11,11]
bass_03_dur = [1,1,1,1]

bass_04_pitch = [15,16,16,11,11]
bass_04_dur = [0.5,0.5,1,1,1]

csr()
nyabinghi_group = nyabinghi()
drum_group = drum_rhythm()
piano_group = piano_rhythm()

piano_group.stop()

# c1 >> bass(bass_01_pitch + bass_02_pitch + bass_01_pitch + bass_03_pitch + bass_01_pitch + bass_02_pitch + bass_01_pitch + bass_04_pitch, dur=bass_01_dur + bass_02_dur + bass_01_dur + bass_03_dur + bass_01_dur + bass_02_dur + bass_01_dur + bass_04_dur, oct=4, pan=0.3, room=0.1, verb=0.1, sus=bass_01_dur + bass_02_dur + bass_01_dur + bass_03_dur + bass_01_dur + bass_02_dur + bass_01_dur + bass_04_dur, amp=1)

# c1.stop()

lead_pattern1 = P[_, _, (9,12,16), (9,12,16), _, _, (4,7,11), (4,7,11)]

lead_pattern2 = P[_, _, (4,7,11), (4,7,11), _, _, (9,12,16), _]

lead_pattern3 = P[_, _, (9,12,16), _, (4,7,11), _,_]

lead_pattern4 = P[_, _, (4,7,11), _, (9,12,16), (9,12,16),_,_]

lp1 = [lead_pattern1, lead_pattern2, lead_pattern3, lead_pattern4]

p1 >> marimba(Pvar([lp1[0], lp1[1]], 4), dur=0.5, sus=0.25, oct=5)


p1 >> marimba(Pvar([lp1[0], lp1[1]], 8), dur=0.5, sus=0.25, oct=5)

p1 >> star(Pvar([lp1[2], lp1[3]], 8), dur=0.5, sus=1, oct=5)

p1 >>   saw(Pvar([lp1[3], lp1[1]], 8), dur=0.5, sus=0.25, oct=5)

p1 >> marimba(Pvar([lp1[1], lp1[2]], 8), dur=0.5, sus=0.5, oct=5)

p1.stop()

def lead_change(a=0):
    if a%3 == 0:
        p1 >> prophet(Pvar([lp1[0], lp1[0]], 4), dur=0.5, sus=0.1, oct=5)
        # print("change 3")
    if a%5 == 0:
        p1 >>  prophet(Pvar([lp1[0], lp1[1]], 4), dur=0.5, sus=0.1, oct=5)
        # print("change 5")
    if a%7 == 0:
        p1 >> prophet(Pvar([lp1[0], lp1[2]], 4), dur=0.5, sus=0.1, oct=5)
        # print("change 7")
    if a%13 == 0:
        p1 >> prophet(Pvar([lp1[0], lp1[3]], 4), dur=0.5, sus=0.1, oct=5)
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

p3.stop()

p4 >> play("-t-t", amp=0.3).every(4, "test0", var.counter1)

p4.stop()

csr()
nyabinghi_group = nyabinghi()
drum_group = drum_rhythm()
piano_group = piano_rhythm()

nyabinghi_group.only()

drum_group.only()

piano_group.only()

nyabinghi_group.stop()

drum_group.stop()

piano_group.stop()

p1.stop()
p2.stop()
p3.stop()
p4.stop()

print(Clock)


# And cancel it with
p3.never("test")

p4.never("test0")

clock()
