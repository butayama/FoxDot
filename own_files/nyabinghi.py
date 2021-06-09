# https://foxdot.org/docs/player-attributes/


# http://studio.dubroom.org/tutorials-computerdub07.htm
# THE NYABINGHI RHYTHM

# include files:
# https://stackoverflow.com/questions/714881/how-to-include-external-python-code-to-use-in-other-files

# Windows:
# with open(r'E:\GitHub\FoxDot\own_files\nyabinghi.py') as f: exec(f.read())

# Debian:
# with open('/home/uwe/PycharmProjects/FoxDot/own_files/include_test.py') as f: exec(f.read())    

# include_message("Include function text from include_test loaded")
# print(message)

def nyabinghi_rhythm():
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

    # close hi-hat
    ch >> play("00--", dur=1, sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5)

    #  bass drum
    bd >> play("X000", dur=1, sample=(0), pan=0.4, room=0.7, verb=0.7, sus=3)
    return

def nyabinghi_rhythm_01():
    #  low conga
    cl >> play("cc0c", dur=1, sample=(0), pan=-0.5,room=0.3, verb=0.3, sus=0.5)

    #  open hi conga
    hc >> play(PEuclid2(1,8,'0','c'), dur=1, sample=(4), pan=-0.55,room=0.5, verb=0.3, sus=0.5)

    # bongo low
    bl >> play("bbb0", dur=1, sample=(1), pan=-0.25,room=0.3, verb=0.2, sus=0.5)

    # bongo hi
    bh >> play("[00b0][b0bb]0", dur=[1, 1, 6], sample=(0), pan=-0.3,room=0.5, verb=0.2, sus=0.5)

    # crash cymba
    cc >> play(PEuclid2(1,16,'0','C'), dur=1, sample=(0), amp=0.2, pan=0.5,room=0.0, verb=0.0, sus=0.2)

    # cowbell
    cb >> play("[T0T0][T0TT]0", dur=[1, 1, 6], sample=(1), amp=0.1, pan=0.3,room=0.3, verb=0.2, sus=0.5)

    # hi-mid-tom
    ht >> play("M0M", dur=[2, 0.6, 1.4], sample=(4), pan=0.2, room=0.5, verb=0.5, sus=2)

    # low-mid-tom
    mt >> play("M00M", dur=[3, 5], sample=(1), pan=0.2, room=0.5, verb=0.5, sus=2)

    # open hi-hat
    oh >> play("00=", dur=[0.1, 3.9, 4], sample=(1), pan=0.45, room=0.5, verb=0.5, sus=2)

    # low tom
    lt >> play("m0m0", dur=[0.1, 3.5, 0.4, 4], sample=(0), pan=0.2, room=0.5, verb=0.5, sus=2)

    # close hi-hat
    ch >> play("-0--", dur=1, sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5)

    #  bass drum
    bd >> play("X0XX", dur=1, sample=(0), pan=0.4, room=0.7, verb=0.7, sus=3)

def nyabinghi_rhythm_02():
    #  low conga
    cl >> play(PEuclid2(5, 16, "0", "c"), dur=1, sample=(0), pan=-0.5,room=0.3, verb=0.3, sus=0.5)

    #  open hi conga
    hc >> play(PEuclid2(3,8,'0','c'), dur=1, sample=(4), pan=-0.55,room=0.5, verb=0.3, sus=0.5)

    # bongo low
    bl >> play(PEuclid2(9,16,"0","b"), dur=1, sample=(1), pan=-0.25,room=0.3, verb=0.2, sus=0.5)

    # bl >> play("bbb0", dur=1, sample=(1), pan=-0.25,room=0.3, verb=0.2, sus=0.5)

    # bongo hi
    # bh >> play(PEuclid2(17,32,"0","b"), dur=[1, 1, 6], sample=(0), pan=-0.3,room=0.5, verb=0.2, sus=0.5)
    bh >> play("[bbb0][b0b0]b", dur=[1, 1, 6], sample=(0), pan=-0.3,room=0.5, verb=0.2, sus=0.5)

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
    lt >> play("0mm0", dur=[0.1, 3.5, 0.4, 4], sample=(0), pan=0.2, room=0.5, verb=0.5, sus=2)

    # close hi-hat
    ch >> play("-0-0", dur=1, sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5)

    #  bass drum
    bd >> play("X000", dur=1, sample=(0), pan=0.4, room=0.7, verb=0.7, sus=3)

def nyabinghi_rhythm_random():
    #  low conga
    cl >> play("cc0c", dur=1, sample=(0), pan=-0.5,room=0.3, verb=0.3, sus=0.5)

    #  open hi conga
    hc >> play(PEuclid2(1,8,'0','c'), dur=1, sample=(4), pan=-0.55,room=0.5, verb=0.3, sus=0.5)

    # bongo low
    bl >> play("bbb0", dur=1, sample=(1), pan=-0.25,room=0.3, verb=0.2, sus=0.5)

    # bongo hi
    bh >> play("[00b0][b0bb]0", dur=[1, 1, 6], sample=(0), pan=-0.3,room=0.5, verb=0.2, sus=0.5)

    # crash cymba
    cc >> play(PEuclid2(1,16,'0','C'), dur=1, sample=(0), amp=0.2, pan=0.5,room=0.0, verb=0.0, sus=0.2)

    # cowbell
    cb >> play("[T0T0][T0TT]0", dur=[1, 1, 6], sample=(1), amp=0.1, pan=0.3,room=0.3, verb=0.2, sus=0.5)

    # hi-mid-tom
    ht >> play("M0M", dur=[2, 0.6, 1.4], sample=(4), pan=0.2, room=0.5, verb=0.5, sus=2)

    # low-mid-tom
    mt >> play("M00M", dur=[3, 5], sample=(1), pan=0.2, room=0.5, verb=0.5, sus=2)

    # open hi-hat
    oh >> play("00=", dur=[0.1, 3.9, 4], sample=(1), pan=0.45, room=0.5, verb=0.5, sus=2)

    # low tom
    lt >> play("m0m0", dur=[0.1, 3.5, 0.4, 4], sample=(0), pan=0.2, room=0.5, verb=0.5, sus=2)

    # close hi-hat
    ch >> play("-0--", dur=1, sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5)

    #  bass drum
    bd >> play("X0XX", dur=1, sample=(0), pan=0.4, room=0.7, verb=0.7, sus=3)

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

# close hi-hat
ch >> play("00--", dur=1, sample=(0), pan=0.45, room=0.5, verb=0.5, sus=0.5)

#  bass drum
bd >> play("X000", dur=1, sample=(0), pan=0.4, room=0.7, verb=0.7, sus=3)

