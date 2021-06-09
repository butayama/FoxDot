# https://foxdot.org/docs/player-attributes/


# http://studio.dubroom.org/tutorials-computerdub07.htm
# THE NYABINGHI RHYTHM

# include files:
# https://stackoverflow.com/questions/714881/how-to-include-external-python-code-to-use-in-other-files

# Windows:
with open(r'E:\GitHub\FoxDot\own_files\nyabinghi.py') as f: exec(f.read())

# Debian:
# with open('/home/uwe/PycharmProjects/FoxDot/own_files/include_test.py') as f: exec(f.read())    

# include_message("Include function text from include_test loaded")
# print(message)

def csr(bpm=140, scale="chromatic",root="C"):
    Clock.bpm = bpm
    Scale.default = scale
    Root.default = root
    return


# http://studio.dubroom.org/tutorials-computerdub15.htm
# ___________________________________________________________________________________________________________
# PROGRAMMING A BASIC DRUM RHYTHM
# ___________________________________________________________________________________________________________

def drum_rhythm(a=0, b=0):
    a = var.counter
    # print("drum_rhythm a = ", a, "   b = ", b)
    # dr_group.stop()
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
    return

# ___________________________________________________________________________________________________________
# PROGRAMMING A DRUM Roll
# ___________________________________________________________________________________________________________


def drum_roll(b=0):
    # print("drum_roll b = ", b)
    if b == 0:
        drum_group.stop()
        dr_random() 
    elif b == 4:
        drum_group.stop()
        dr_random()             
    elif b == 8:
        drum_group.stop()
        dr_random()
    elif b == 12:
        drum_group.stop()
        dr_random()      
    elif b == 16:
        drum_group.stop()
        dr_random()
    elif b == 20:
        drum_group.stop()
        dr_random()          
    else:
        dr_00()
        # dr_group.stop()     
    return
    

# ___________________________________________________________________________________________________________
# PROGRAMMING A DRUM Track
# http://studio.dubroom.org/tutorials-computerdub18.htm
# ___________________________________________________________________________________________________________

bassdrum = Player()
snare = Player()
rim = Player()
tom_hi = Player()
tom_mid = Player()
tom_lo = Player()
crash_01 = Player()
hh_close = Player()
hh_open = Player()
crash_02 = Player()



def dr_00():
    bassdrum >> play("X", dur=0.25, sample=(1), pan=0.4, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    snare >> play("i", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    rim >>  play("t", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    tom_hi >> play("M", dur=0.25, sample=(4), pan=0.4, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    tom_mid >> play("M", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    tom_lo >> play("m", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    crash_01 >> play("C", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    hh_close >> play("-", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    hh_open >> play("=", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    crash_02 >> play("#", dur=0.25, sample=(3), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    return

def dr_08():
    bassdrum >> play("X", dur=0.25, sample=(1), pan=0.4, room=0.7, verb=0.7, sus=3, amp=[1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0])
    snare >> play("i", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
    rim >>  play("t", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    tom_hi >> play("M", dur=0.25, sample=(4), pan=0.4, room=0.7, verb=0.7, sus=3, amp=[0,0,1,0.8,0.6,0,0,0,0,0,0,0,0,0,0,0])
    tom_mid >> play("M", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0.6,0,0,0,0,0,0,0,0,0])
    tom_lo >> play("m", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0.6,0.8,1,0,0,0,0,0])
    crash_01 >> play("C", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    hh_close >> play("-", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    hh_open >> play("=", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    crash_02 >> play("#", dur=0.25, sample=(3), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])


def dr_16():
    bassdrum >> play("X", dur=0.25, sample=(1), pan=0.4, room=0.7, verb=0.7, sus=3, amp=[1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0])
    snare >> play("i", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0])
    rim >>  play("t", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    tom_hi >> play("M", dur=0.25, sample=(4), pan=0.4, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,1,0,0.8,0,0,0,0,0,0,0,0,0])
    tom_mid >> play("M", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0.8,0.6,0,0,0,0,0,0,0])
    tom_lo >> play("m", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0.6,0,0,0,0,0])
    crash_01 >> play("C", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
    hh_close >> play("-", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    hh_open >> play("=", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    crash_02 >> play("#", dur=0.25, sample=(3), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
    return


def dr_random():
    bassdrum >> play("X", dur=0.25, sample=(1), pan=0.4, room=0.7, verb=0.7, sus=3,  amp=PwRand([0,1,0.8,0.6],[14,1,1,1])[:16])
    snare >> play("i", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,    amp=PwRand([0,1,0.8,0.6],[9,3,1,3])[:16])
    rim >>  play("t", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,     amp=PwRand([0,1,0.8,0.6],[8,1,1,1])[:16])
    tom_hi >> play("M", dur=0.25, sample=(4), pan=0.4, room=0.7, verb=0.7, sus=3,    amp=PwRand([0,1,0.8,0.6],[14,1,1,1])[:16])
    tom_mid >> play("M", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,  amp=PwRand([0,1,0.8,0.6],[14,1,1,1])[:16])
    tom_lo >> play("m", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3,   amp=PwRand([0,1,0.8,0.6],[9,3,1,3])[:16])
    crash_01 >> play("C", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0])
    hh_close >> play("-", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=PwRand([0,1,0.8,0.6],[8,1,1,1])[:16])
    hh_open >> play("=", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,  amp=PwRand([0,1,0.8,0.6],[12,1,1,0])[:16])
    crash_02 >> play("#", dur=0.25, sample=(3), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
    return
    



def dr_random_01():
    bassdrum >> play("X", dur=0.25, sample=(1), pan=0.4, room=0.7, verb=0.7, sus=3,  amp=PwRand([0,1,0.8,0.6],[14,1,1,1])[:16])
    snare >> play("i", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,    amp=PwRand([0,1,0.8,0.6],[9,3,1,3])[:16])
    rim >>  play("t", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,     amp=PwRand([0,1,0.8,0.6],[8,1,1,1])[:16])
    tom_hi >> play("M", dur=0.25, sample=(4), pan=0.4, room=0.7, verb=0.7, sus=3,    amp=PwRand([0,1,0.8,0.6],[14,1,1,1])[:16])
    tom_mid >> play("M", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,  amp=PwRand([0,1,0.8,0.6],[14,1,1,1])[:16])
    tom_lo >> play("m", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3,   amp=PwRand([0,1,0.8,0.6],[9,3,1,3])[:16])
    crash_01 >> play("C", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=PwRand([0,1,0.8,0.6],[15,1,0,0])[:16])
    hh_close >> play("-", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=PwRand([0,1,0.8,0.6],[8,1,1,1])[:16])
    hh_open >> play("=", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,  amp=PwRand([0,1,0.8,0.6],[12,1,1,0])[:16])
    crash_02 >> play("#", dur=0.25, sample=(3), pan=0.45, room=0.7, verb=0.7, sus=3, amp=PwRand([0,1,0.8,0.6],[15,1,0,0])[:16])
    return

# http://studio.dubroom.org/tutorials-computerdub16.htm
# ___________________________________________________________________________________________________________
# PROGRAMMING A BASSLINE ON TWO PIANO CHORDS
# ___________________________________________________________________________________________________________

def piano_rhythm():
    # melodic A Chord (piano synth is not recognized)
    pa >> prophet([_,(9,12,16),_,(9,12,16),_,_], dur=[rest(1),0.25,rest(1.75),0.25,rest(0.75),rest(4)], oct=5, pan=-0.2, room=0.5, verb=0.5, sus=0.15, amp=[0.8])
    # melodic E Chord (piano synth is not recognized)
    pe >> prophet([_,(4,7,11),_,(4,7,11),_], dur=[rest(5),0.25,rest(1.75),0.25,rest(0.75)], oct=5, pan=-0.2, room=0.5, verb=0.5, sus=0.15, amp=[0.8])
    return
    
lead_pattern_C_1 = P[(0,4,9), _, (0,4,9), _, _, _, (0,4,9), _]
lead_pattern_B_2 = P[_, _, (-1,4,7), _, _, _, (-1,4,7), _]
lead_pattern_C_3 = P[_, _, (0,4,9), _, _, _, (0,4,9), _]
lead_pattern_B_4 = P[_, _, (-1,4,7), _, (4,7,11), _, (-1,4,7), _]
lead_pattern_B_8 = P[_, _, (-1,4,7), _, (4,7,11), (4,7,11), (-1,4,7), _]

lp1 = [lead_pattern_C_1, lead_pattern_B_2, lead_pattern_C_3, lead_pattern_B_4, lead_pattern_C_3, lead_pattern_B_2, lead_pattern_C_3, lead_pattern_B_8]

csr()

   
def lead_change(a=0):
    # print(int(var.counter))
    p1 >> charm(lp1[int(var.counter)], dur=0.5, pan=0.35, room=0.5, verb=0.5, sus=0.15, oct=4, amp=1.5)
    return

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
        # print(a)
        p2 >> bass(bass_pitch_pattern[int(number)], dur=bass_dur_pattern[int(number)], oct=4, amp=0.9, pan=-0.6, room=0.1, verb=0.9, sus=0.9)
    return

        
var.counter = var(list(range(0,8)))
var.track_counter = var(list(range(0,24)))
var.counter1 = var(0)


counter_loop_info = Player()

@PlayerMethod
def counter_info(self):
    print(var.counter, var.track_counter, var.counter1)

@PlayerMethod
def drum_loop(self, a = 0, b = 0):
    drum_rhythm(a, b)

@PlayerMethod
def drum_loop_2(self, b = 0):
    drum_roll(b)

@PlayerMethod
def lead_loop(self, a = 0):
    lead_change(a)
    # print("lead_loop: ", a)

@PlayerMethod
def bass_loop(self, a = 0):
    bass_change(a)
    var.counter1 += 1
    # print("bass_loop: ", var.counter1)
    

nyabinghi_group = Group(cl,hc,bl,bh,cc,cb,ht,mt,oh,lt,ch,bd)
piano_group = Group(pa, pe)
lead_group = Group(p3)
bass_group = Group(p4) 
drum_group = Group(ch,oh,sd,kd)
drum_bass_group = Group(ch,oh,sd,kd,p4)
drum_bass_piano_group = Group(ch,oh,sd,kd,p4,pa,pe)

dr_group = Group(bassdrum, snare, rim, tom_hi, tom_mid, tom_lo, crash_01, hh_close, hh_open, crash_02)    

# _______________________________________________________________________________________________________
# start playing
# _______________________________________________________________________________________________________
csr()
nyabinghi_rhythm()
piano_rhythm()
p3 >> play("_").every(4, "lead_loop", 0)
p4 >> play("_").every(4, "bass_loop", var.counter1)
p5 >> play("_", amp=0.3).every(4, "drum_loop", var.counter, var.track_counter)
p6 >> play("_", amp=0.3).every(4, "drum_loop_2", var.track_counter)
# counter_loop_info >> play("_").every(4, "counter_info")

# dr_00()
# dr_08()
# dr_16()
dr_random()


dr_random_01()

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
dr_group.stop()


# _______________________________________________________________________________________________________
# Concel functions
# _______________________________________________________________________________________________________
p3.never("lead")

p4.never("bass")

p5.never("drum")


# _______________________________________________________________________________________________________
# only playing
# _______________________________________________________________________________________________________

nyabinghi_group.only()
drum_group.only()
piano_group.only()
lead_group.only()
bass_group.only()
drum_group.only()
drum_bass_group.only()
drum_bass_piano_group.only()

# _______________________________________________________________________________________________________
# echo playing
# _______________________________________________________________________________________________________

piano_group = piano_rhythm()

piano_group.pan = [0.25]
piano_group.fmod = 0
piano_group.vib=0
piano_group.vibdepth=0.5
piano_group.slide=0
piano_group.bend=0
piano_group.chop=0
piano_group.coarse=0
piano_group.dist=0.5
piano_group.shape=0.8

piano_group.drive=[linvar([0, 1], 0.1)]
piano_group.drive=[0.3]

piano_group.echo=[linvar([0, 5], 0.25)]
piano_group.echotime=[linvar([0, 5], 0.25)]
piano_group.room=0.8
piano_group.cut=0
piano_group.formant=2
piano_group.tremolo=0
piano_group.pshift=[linvar([0, 5], 0.25)]
piano_group.pshift=[0]
piano_group.glide=[linvar([0, 5], 0.25)]
piano_group.glide=[0]
piano_group.every(4, "stutter", 4)
piano_group.every(8, "stutter", 0)
piano_group.
piano_group.
piano_group.
piano_group.




print(Clock)
