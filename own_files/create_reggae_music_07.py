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

    nyabinghi = Group(c1,hc,b1,bh,cc,cb,ht,mt,oh,lt,ch,bd)
    return nyabinghi

# http://studio.dubroom.org/tutorials-computerdub15.htm

# ___________________________________________________________________________________________________________
# PROGRAMMING A BASIC DRUM RHYTHM
# ___________________________________________________________________________________________________________
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
    piano_rythm = Group(pa, pe)
    return piano_rythm
    
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

c1 >> bass(bass_01_pitch + bass_02_pitch + bass_01_pitch + bass_03_pitch + bass_01_pitch + bass_02_pitch + bass_01_pitch + bass_04_pitch, dur=bass_01_dur + bass_02_dur + bass_01_dur + bass_03_dur + bass_01_dur + bass_02_dur + bass_01_dur + bass_04_dur, oct=4, pan=0.3, room=0.1, verb=0.1, sus=bass_01_dur + bass_02_dur + bass_01_dur + bass_03_dur + bass_01_dur + bass_02_dur + bass_01_dur + bass_04_dur, amp=1)

c1.stop()

print((bass_01_pitch + bass_02_pitch, bass_01_dur + bass_02_dur))

bass_01 >> bass(bass_01_pitch, dur=bass_01_dur, oct=4, pan=0.3, room=0.1, verb=0.1, sus=bass_01_dur)

bass_02 >> bass(bass_02_pitch, dur=bass_02_dur, oct=4, pan=0.3, room=0.1, verb=0.1, sus=bass_02_dur)

bass_03 >> bass(bass_03_pitch, dur=bass_03_dur, oct=4, pan=0.3, room=0.1, verb=0.1, sus=bass_03_dur)

bass_04 >> bass(bass_04_pitch, dur=bass_04_dur, oct=4, pan=0.3, room=0.1, verb=0.1, sus=bass_04_dur)

bass_04.stop()


x1 >> play("BBCXoXoXoXoxoOXXCOOXX", dur=1/2)

x1.stop()


pitch_change = var([bass_01_pitch, bass_02_pitch, bass_03_pitch, bass_04_pitch], 4)

dur_change = var([bass_01_dur, bass_02_dur, bass_03_dur, bass_04_dur], 4)

print(dur_change)

a = (pitch_change)

b = (dur_change)

c1 >> bass(Pvar([bass_01_pitch], 7), dur=1)

print(a, b)

pattern1 = P[0, 1, 2, 3]
pattern2 = P[4, 5, 6, 7]

print(Pvar([pattern1, pattern2], 4))

p1 >> pluck(Pvar([pattern1, pattern2], 4), dur=1)

bass_01 >> bass([_,9,_,9,9,16,12], dur=[rest(1),0.75,rest(0.25),0.5,0.5,0.5,0.5], oct=4, pan=0.3, room=0.1, verb=0.1, sus=[rest(1),0.75,rest(0.25),0.5,0.5,0.5,0.5])


bass_A0_01 >> bass([_,9,_,9,9,_], dur=[rest(1),0.75,rest(0.25),0.5,0.5,1], oct=4, pan=0.3, room=0.1, verb=0.1, sus=[rest(1),0.75,rest(0.25),0.5,0.5,1])
bass_B0_01 >> bass([_], dur=[rest(4)])
bass_D1s_01 >> bass([_], dur=[rest(4)])
bass_E1_01 >> bass([_,16,_], dur=[rest(3.0),0.5,rest(0.5)], oct=4, pan=0.3, room=0.1, verb=0.1, sus=[rest(3.0),0.5,rest(0.5)])
bass_C1_01 >> bass([_,12], dur=[rest(3.5),0.5], oct=4, pan=0.3, room=0.1, verb=0.1, sus=[rest(3.5),0.5])

bass_A0_01 >> bass([_], dur=[rest(4)])
bass_B0_01 >> bass([_,11,_], dur=[rest(2),1.5,rest(0.5)], oct=4, pan=0.3, room=0.1, verb=0.1, sus=[rest(2),1.5,rest(0.5)])
bass_D1s_01 >> bass([_], dur=[rest(4)])
bass_E1_01 >> bass([16,16,_], dur=[1,1,rest(2)], oct=4, pan=0.3, room=0.1, verb=0.1, sus=[1,1,rest(2)])
bass_C1_01 >> bass([_], dur=[rest(4)])

bass_A0_01 >> bass([_], dur=[rest(4)])
bass_B0_01 >> bass([_,11,11], dur=[rest(2),1,1], oct=4, pan=0.3, room=0.1, verb=0.1, sus=[rest(2),1,1])
bass_D1s_01 >> bass([_], dur=[rest(4)])
bass_E1_01 >> bass([16,16,_], dur=[1,1,rest(2)], oct=4, pan=0.3, room=0.1, verb=0.1, sus=[1,1,rest(2)])
bass_C1_01 >> bass([_], dur=[rest(4)])

bass_A0_01 >> bass([_], dur=[rest(4)])
bass_B0_01 >> bass([_,11,11], dur=[rest(2),1,1], oct=4, pan=0.3, room=0.1, verb=0.1, sus=[rest(2),1,1])
bass_D1s_01 >> bass([15,_], dur=[0.5,rest(3.5)], oct=4, pan=0.3, room=0.1, verb=0.1, sus=[0.5,rest(3.5)])
bass_E1_01 >> bass([_,16,16,_], dur=[0.5,0.5,1,rest(2)], oct=4, pan=0.3, room=0.1, verb=0.1, sus=[0.5,0.5,1,rest(2)])
bass_C1_01 >> bass([_], dur=[rest(4)])
