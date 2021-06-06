# https://foxdot.org/docs/player-attributes/


# http://studio.dubroom.org/tutorials-computerdub07.htm
# THE NYABINGHI RHYTHM


def csr(bpm=140, scale="chromatic",root="C"):
    Clock.bpm = bpm
    Scale.default = scale
    Root.default = root
    return

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

def drum_rhythm(a=0):
    #  close hi-hat
    ch >> play("-", dur=0.5, sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5, amp=[1, 0.4])

    # open hi-hat
    oh >> play("=", dur=[0.5], sample=(1), pan=0.45, room=0.5, verb=0.5, sus=0.5, amp=PStep(8, 1))

    # snare drum
    if a != 7:
        sd >> play("0i", dur=[2.0, 2.0], sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5, amp=1)
    else:
        sd >> play("0ii", dur=[0.5,1.5,2.0], sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5, amp=1)    

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
    
def lead_change(a=0):
    lead_pattern1 = P[_, _, (9,12,16), (9,12,16), _, _, (4,7,11), (4,7,11)]
    lead_pattern2 = P[_, _, (4,7,11), _, _, _, (9,12,16), _]
    lead_pattern3 = P[_, _, (4,7,11), (4,7,11), _, _, (9,12,16), (9,12,16)]
    lead_pattern4 = P[_, _, (9,12,16), _, _, _, (4,7,11), _]
    lp1 = [lead_pattern1, lead_pattern2, lead_pattern3, lead_pattern4]
    if a == 0:
        p1 >> prophet(lp1[0], sus=0.15, oct=5)
        # print("change 0")
    elif a == 8:
        p1 >> prophet(lp1[1], sus=0.15, oct=5)
        # print("change 8")
    elif a == 16:
        p1 >> prophet(lp1[2], sus=0.15, oct=5)
        # print("change 16")
    elif a == 24:
        p1 >> prophet(lp1[3], sus=0.15, oct=5)
        # print("change 24")     
    lead_player = Group(p1)    
    return lead_player

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
       
        
def bass_change(a=0):
    while a == int(number):
        pass
    else:    
        a = int(number)
        print(a)
        # p2 >> bass(bass_pitch_pattern[int(number)], dur=bass_dur_pattern[int(number)], oct=4, amp=0.5)

        
counter = list(range(0,8))
count_8_beats = var(counter)
count_32_beats = var(list(range(0,32)))

@PlayerMethod
def drum(self, a = 0):
    drum_group = drum_rhythm(a)

@PlayerMethod
def lead(self, a = 0):
    lead_group = lead_change(a)
    # print("lead: ", a)

@PlayerMethod
def bass(self, a = 0):
    bass_change(a)

# _______________________________________________________________________________________________________
# Start playing
# _______________________________________________________________________________________________________
csr()

nyabinghi_group = nyabinghi()
piano_group = piano_rhythm()
p3 >> play("_").every(4, "lead", count_32_beats)
p4 >> play("_").every(4, "bass", count_8_beats)
p5 >> play("_", amp=0.3).every(4, "drum", count_8_beats)

# _______________________________________________________________________________________________________
# only playing
# _______________________________________________________________________________________________________

nyabinghi_group.only()
drum_group.only()
piano_group.only()
lead_group.only()
bass_group.only()
drum_group.only()

# _______________________________________________________________________________________________________
# Concel functions
# _______________________________________________________________________________________________________
p3.never("lead")

p4.never("bass")

p5.never("drum")

# _______________________________________________________________________________________________________
# Stop playing
# _______________________________________________________________________________________________________

nyabinghi_group.stop()
drum_group.stop()
piano_group.stop()
p1.stop()
p2.stop()
p3.stop()
p4.stop()
p5.stop()

print(Clock)
