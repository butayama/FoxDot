# https://foxdot.org/docs/player-attributes/


# http://studio.dubroom.org/tutorials-computerdub07.htm
# THE NYABINGHI RHYTHM


def csr(bpm=140, scale="chromatic",root="C"):
    Clock.bpm = bpm
    Scale.default = scale
    Root.default = root
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
print(number)
        
        
def bass_change(a=0):
    while a == int(number):
        pass
    else:    
        a = int(number)
        print(a)
        p2 >> bass(bass_pitch_pattern[int(number)], dur=bass_dur_pattern[int(number)], oct=4, amp=0.5)



var.counter1 = var(0)

@PlayerMethod
def test0(self, a = 0):
    bass_change(a)
    var.counter1 += 1
    print("bass: ", var.counter1)


p4 >> play("-t-t").every(4, "test0", var.counter1)

# And cancel it with
p3.never("test")

p4.never("test0")

