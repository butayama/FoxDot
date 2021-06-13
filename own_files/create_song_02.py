# https://foxdot.org/docs/player-attributes/


# http://studio.dubroom.org/tutorials-computerdub07.htm
# THE NYABINGHI RHYTHM

# include files:
# https://stackoverflow.com/questions/714881/how-to-include-external-python-code-to-use-in-other-files

import platform
h = platform.uname()[1]
print(h)
# Windows DESKTOP-0AVFOFJ
if h == "DESKTOP-0AVFOFJ": 
    with open(r'E:\GitHub\FoxDot\own_files\nyabinghi.py') as f: exec(f.read())
    with open(r'E:\GitHub\FoxDot\own_files\amp_list_dr_random_01.py') as f: exec(f.read())
    with open(r'E:\GitHub\FoxDot\own_files\amp_list_dr_random_02.py') as f: exec(f.read())
# Debian - akoya:
elif h == "akoya-buster":    
    with open(r'/home/uwe/PycharmProjects/FoxDot/own_files/nyabinghi.py') as f: exec(f.read())
    with open(r'/home/uwe/PycharmProjects/FoxDot/own_files/amp_list_dr_random_01.py') as f: exec(f.read())
    with open(r'/home/uwe/PycharmProjects/FoxDot/own_files/amp_list_dr_random_02.py') as f: exec(f.read())


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
    if b == 8:
        drum_group.stop()
        dr_08()
    elif b == 16:
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
dr_group = Group(bassdrum, snare, rim, tom_hi, tom_mid, tom_lo, crash_01, hh_close, hh_open, crash_02)

nyabinghi_group = Group(cl,hc,bl,bh,cc,cb,ht,mt,oh,lt,ch,bd)
piano_group = Group(pa, pe)
lead_group = Group(p3)
bass_group = Group(p4)
drum_group = Group(ch,oh,sd,kd)
drum_bass_group = Group(ch,oh,sd,kd,p4)
drum_bass_piano_group = Group(ch,oh,sd,kd,p4,pa,pe)


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
    
def dr_random_01_gen():
    amp_list = []
    amp_list.append(PwRand([0,1,0.8,0.6],[14,1,1,1])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[9,3,1,3])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[8,1,1,1])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[14,1,1,1])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[14,1,1,1])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[9,3,1,3])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[15,1,0,0])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[8,1,1,1])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[12,1,1,0])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[15,1,0,0])[:16])
    return amp_list
    
var.amp_list_01_number = var(0)

def dr_random_01(amp_list=[]):
    if not amp_list:
        amp_list = dr_random_01_gen()
    var.amp_list_01_number += 1
    print(f"amp_list01_{var.amp_list_01_number} = {amp_list}")
    bassdrum >> play("X", dur=0.25, sample=(1), pan=0.4, room=0.7, verb=0.7, sus=3,  amp=amp_list[0])
    snare >> play("i", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,    amp=amp_list[1])
    rim >>  play("t", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,     amp=amp_list[2])
    tom_hi >> play("M", dur=0.25, sample=(4), pan=0.4, room=0.7, verb=0.7, sus=3,    amp=amp_list[3])
    tom_mid >> play("M", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,  amp=amp_list[4])
    tom_lo >> play("m", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3,   amp=amp_list[5])
    crash_01 >> play("C", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=amp_list[6])
    hh_close >> play("-", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=amp_list[7])
    hh_open >> play("=", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,  amp=amp_list[8])
    crash_02 >> play("#", dur=0.25, sample=(3), pan=0.45, room=0.7, verb=0.7, sus=3, amp=amp_list[9])
    return


# print(Clock.now())
# Clock.schedule(lambda: print(Clock.now()), Clock.now() + 4)

def dr_random_02_gen():
    amp_list = []
    amp_list.append(PwRand([0,1,0.8,0.6],[14,1,1,1])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[9,3,1,3])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[8,1,1,1])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[14,1,2,3])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[14,1,3,3])[:16])
    amp_list.append(PwRand([0,1,0.8,0.6],[9,3,4,2])[:16])
    amp_list.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    amp_list.append(PwRand([0,1,0.8,0.6],[8,8,8,8])[:16])
    amp_list.append([0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0])
    amp_list.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    return amp_list

var.amp_list_02_number = var(0)

def dr_random_02(amp_list=[]):
    if not amp_list:
        amp_list = dr_random_02_gen()
    var.amp_list_02_number += 1
    print(f"amp_list02_{var.amp_list_02_number} = {amp_list}")
    bassdrum >> play("X", dur=0.25, sample=(1), pan=0.4, room=0.7, verb=0.7, sus=3,  amp=amp_list[0])
    snare >> play("i", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,    amp=amp_list[1])
    rim >>  play("t", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,     amp=amp_list[2])
    tom_hi >> play("M", dur=0.25, sample=(4), pan=0.4, room=0.7, verb=0.7, sus=3,    amp=amp_list[3])
    tom_mid >> play("M", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,  amp=amp_list[4])
    tom_lo >> play("m", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3,   amp=amp_list[5])
    crash_01 >> play("C", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=amp_list[6])
    hh_close >> play("-", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=amp_list[7])
    hh_open >> play("=", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,  amp=amp_list[8])
    crash_02 >> play("#", dur=0.25, sample=(3), pan=0.45, room=0.7, verb=0.7, sus=3, amp=amp_list[9])
    return

amp_list01_11 = [P[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], P[0.6, 0, 1, 0, 0, 1, 0, 0.8, 0.6, 0, 0, 1, 0, 0, 0, 0], P[0, 0, 1, 0, 0, 0, 0.6, 0.8, 0, 0, 0, 0, 0, 0, 0, 0], P[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1], P[0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], P[1, 1, 0, 0.8, 0, 0, 0.6, 1, 0, 0, 0.6, 0, 0, 0, 0, 0], P[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], P[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0.8, 0, 0], P[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], P[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0]]

print(amp_list01_11[5])

csr()
dr_random_01()
dr_random_02()
# dr_group.stop()
    
# def dr_list_play(dr_collection_01=amp_list01, dr_collection_02=amp_list02):
#     print(a)           
# dr_list_play()  

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

list_01_counter = var(list(range(0, len(amp_list01)))) 
list_02_counter = var(list(range(0, len(amp_list02))))          
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

@PlayerMethod
def amp_list_loop(self, amp_list = amp_list01, list_nr = 1):
    if list_nr == 1:
        dr_random_01(amp_list[int(list_01_counter)])
    elif list_nr == 2:
        dr_random_02(amp_list[int(list_02_counter)])        

amp_list02_var = Pvar(amp_list02, 4) 
# print(amp_list02_var)
dr_random_02(amp_list02[1])    

# _______________________________________________________________________________________________________
# start playing according to a planned schedule
# _______________________________________________________________________________________________________
csr()
number_of_song_measures = 128

notes_to_play = ("xabcdefghij")


def pluck_a_note(note_x="x"):
    p1 >> play(note_x, dur=4)


def song_init(i_bar):
    def increase_bar(k_bar, j_increment):
        if isinstance(k_bar, tuple):
            j_bar = k_bar[0]
        else:
            j_bar = k_bar   
        print(f"j_bar = {j_bar}")
        j_bar += j_increment
        j_beat = j_bar + j_increment * Clock.bars()
        return j_bar, j_beat
    # Start with silence set Clock tempo, scale and root note
    if i_bar < 2:
        csr()
    # Begin with a one bar drum intro
    elif i_bar == 2:
        dr_08()
    # Start drum loop
    elif i_bar == 3:
        p5 >> play("_", amp=0.3).every(4, "drum_loop", var.counter, var.track_counter)
        dr_group.stop()
        # Start lead_loop
    elif i_bar == 4:
        p3 >> play("_").every(4, "lead_loop", 0) 
        # Start piano 
    elif i_bar == 5:
        piano_rhythm()
    # Start Nyabinghi
    elif i_bar == 12:
        nyabinghi_rhythm()
    elif i_bar == 16:
        p4 >> play("_").every(4, "bass_loop", var.counter1)   
    elif i_bar == 20:
        dr_08()      
    # Stop drum intro
    elif i_bar == 21:
        dr_group.stop()     
    else:
        # i_bar = increase_bar(i_bar, 1)
        # Stop song
        if i_bar > 28:
            Clock.clear()
            return
    i_bar, i_beat = increase_bar(i_bar, 1)
    print(i_bar)
    Clock.future(4, song_init, args=([i_bar]))

Clock.clear()

Clock.set_time(0)
song_init(0)

piano_rhythm()

p4 >> play("_").every(4, "bass_loop", var.counter1) 


 









# _______________________________________________________________________________________________________
# start playing
# _______________________________________________________________________________________________________
csr()
nyabinghi_rhythm()
nyabinghi_rhythm_01()
nyabinghi_rhythm_02()
piano_rhythm()
p3 >> play("_").every(4, "lead_loop", 0)
p4 >> play("_").every(4, "bass_loop", var.counter1)
p5 >> play("_", amp=0.3).every(4, "drum_loop", var.counter, var.track_counter)
p6 >> play("_", amp=0.3).every(4, "drum_loop_2", var.track_counter)
p7 >> play("_", amp=0.3).every(4, "amp_list_loop", amp_list01, 1)
p7.stop()
p8 >> play("_", amp=0.3).every(4, "amp_list_loop", amp_list02, 2)
# counter_loop_info >> play("_").every(4, "counter_info")

# dr_00()
# dr_08()
# dr_16()

nyabinghi_group.dur=2

dr_random()
dr_group.dur=2

dr_random_01()
dr_group.dur=2

dr_random_02()
dr_group.dur=2

nyabinghi_group.dur=1

dr_random()
dr_group.dur=1

dr_random_01()
dr_group.dur=1

dr_random_02()
dr_group.dur=1

nyabinghi_group.dur=0.5

dr_random()
dr_group.dur=0.5

dr_random_01()
dr_group.dur=0.5

dr_random_02()
dr_group.dur=0.5

nyabinghi_group.dur=0.25

dr_random()
dr_group.dur=0.25

dr_random_01()
dr_group.dur=0.25

dr_random_02()
dr_group.dur=0.25

#  low conga
cl >> play(PEuclid2(7, 16, "0", "c"), dur=1, sample=(0), pan=-0.5,room=0.3, verb=0.3, sus=0.5)

#  open hi conga
hc >> play(PEuclid2(5,8,'0','c'), dur=1, sample=(4), pan=-0.55,room=0.5, verb=0.3, sus=0.5)

# bongo low
bl >> play(PEuclid2(9,16,"0","b"), dur=1, sample=(1), pan=-0.25,room=0.3, verb=0.2, sus=0.5)

# bl >> play("bbb0", dur=1, sample=(1), pan=-0.25,room=0.3, verb=0.2, sus=0.5)

# bongo hi
# bh >> play(PEuclid2(17,32,"0","b"), dur=[1, 1, 6], sample=(0), pan=-0.3,room=0.5, verb=0.2, sus=0.5)
bh >> play("[bbb0][bb0b]0", dur=[1, 1, 6], sample=(0), pan=-0.3,room=0.5, verb=0.2, sus=0.5)

# crash cymba
cc >> play(PEuclid2(1,16,'0','C'), dur=1, sample=(0), amp=0.2, pan=0.5,room=0.0, verb=0.0, sus=0.2)

# cowbell
cb >> play(PEuclid2(13,32,"0","T"), dur=[1, 1, 6], sample=(1), amp=0.1, pan=0.3,room=0.3, verb=0.2, sus=0.5)

# hi-mid-tom
ht >> play(PEuclid2(7,24,"0","M"), dur=[2, 0.6, 1.4], sample=(4), pan=0.2, room=0.5, verb=0.5, sus=2)

# low-mid-tom
mt >> play("MM0M", dur=[3, 5], sample=(1), pan=0.2, room=0.5, verb=0.5, sus=2)

# open hi-hat
oh >> play("-0=", dur=[0.1, 3.9, 4], sample=(1), pan=0.45, room=0.5, verb=0.5, sus=2)

# low tom
lt >> play("mm00", dur=[0.1, 3.5, 0.4, 4], sample=(0), pan=0.2, room=0.5, verb=0.5, sus=2)

# close hi-hat
ch >> play("-0-0", dur=1, sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5)

#  bass drum
bd >> play("XX00", dur=1, sample=(0), pan=0.4, room=0.7, verb=0.7, sus=3)
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

p6.never("drum_loop_2")

p7.never("amp_list_loop")

p7.never("amp_list_loop")
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
