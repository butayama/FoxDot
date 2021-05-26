
var.chords = var([0,1,5,3],5)

# var.chords = var([0,1,5,3],linvar([1,1],12))

bd >> glass((0,2,4,5), dur=[6,2,3,4,5], sus = 4, echo = 0.75, room = 0.8, echotime=4, oct=3, vib=4, slide=0.5, slidedelay=0.5, bend=0.5, hpf=linvar([0,2000],32), hpr=linvar([1,0.1],28), mix=0.8)

bd.stop()

a1 >> pluck((0,2,4,5), dur=[6,2,3,4,5], sus = 4, echo = 0.75, room = 0.8, echotime=4, oct=3, vib=4, slide=0.5, slidedelay=0.5, bend=0.5, hpf=linvar([0,2000],32), hpr=linvar([1,0.1],28), mix=0.8)

a1.stop()

a2 >> varsaw((0,2,4,5), dur=[6,2,3,4,5], sus = 4, echo = 0.75, room = 0.8, echotime=4, oct=3, vib=4, slide=0.5, slidedelay=0.5, bend=0.5, hpf=linvar([0,2000],32), hpr=linvar([1,0.1],28), mix=0.8)

a2.stop()

a3 >> charm((0,2,4,5), dur=[6,2,3,4,5], sus = 4, echo = 0.75, room = 0.8, echotime=4, oct=3, vib=4, slide=0.5, slidedelay=0.5, bend=0.5, hpf=linvar([0,2000],32), hpr=linvar([1,0.1],28), mix=0.8)

a3.stop()

a4 >> soprano((0,2,4,5), dur=[6,2,3,4,5], sus = 4, echo = 0.75, room = 0.8, echotime=4, oct=3, vib=4, slide=0.5, slidedelay=0.5, bend=0.5, hpf=linvar([0,2000],32), hpr=linvar([1,0.1],28), mix=0.8)

a4.stop()

a5 >> bell((0,2,4,5), dur=[6,2,3,4,5], sus = 4, echo = 0.75, room = 0.8, echotime=4, oct=3, vib=4, slide=0.5, slidedelay=0.5, bend=0.5, hpf=linvar([0,2000],32), hpr=linvar([1,0.1],28), mix=0.8)

a5.stop()


a6 >> klank((0,2,4,5), dur=[6,2,3,4,5], sus = 4, echo = 0.75, room = 0.8, echotime=4, oct=3, vib=4, slide=0.5, slidedelay=0.5, bend=0.5, hpf=linvar([0,2000],32), hpr=linvar([1,0.1],28), mix=0.8)

a6.stop()


a7 >> feel((0,2,4,5), dur=[6,2,3,4,5], sus = 4, echo = 0.75, room = 0.8, echotime=4, oct=5, vib=4, slide=0.5, slidedelay=0.5, bend=0.5, hpf=linvar([1000,2000],32), mix=0.8, tremolo=2)

a7.stop()

a8 >> ambi(var.chords + [0,2,4,5,2,4,2,5,8,11,12,2,4,0,5], dur=2, sus = 3, echo = 3, room = 0.8, echotime=4, oct=5, vib=0, slide=0, slidedelay=0, bend=0, mix=0.5, tremolo=0.5, amp=0.5)

a8.stop()

a9 >> marimba(var.chords + [0,2,4,5], dur=[1], sus = 4, echo = 4, room = 0.8, echotime=2, oct=5, vib=0, slide=0, slidedelay=0, bend=0, mix=0.8, tremolo=0, amp=10)

a9.stop()

b1 >> snick((0,2,4,5), dur=[6,2,3,4,5], sus = 4, echo = 0.75, room = 0.8, echotime=4, oct=5, vib=4, slide=0.5, slidedelay=0.5, bend=0.5, hpf=linvar([1000,2000],32), mix=0.8, tremolo=2)

b1.stop()


b2 >> sinepad((0,2,4,5), dur=[6,2,3,4,5], sus = 4, echo = 0.75, room = 0.8, echotime=4, oct=5, vib=4, slide=0.5, slidedelay=0.5, bend=0.5, hpf=linvar([1000,2000],32), mix=0.8, tremolo=2)

b2.stop()


b3 >> donk((0,2,4,5), dur=[6,2,3,4,5], sus = 2, echo = 0.75, room = 0.8, echotime=6, oct=6, vib=4, slide=0.5, slidedelay=0.5, bend=0.5, mix=0.8, tremolo=5, amp=5)

b3.stop()



