def bass_bar_01(run=1):
    a0 >> bass([_,5,_,5,5,_], dur=[rest(1),0.75,rest(0.25),0.5,0.5,1])
    e1 >> bass([_,9,_], dur=[rest(3.0),0.5,rest(0.5)])
    c1 >> bass([_,7], dur=[rest(3.5),0.5])
    bass_bar_01_g = Group(a0, e1, c1)
    if run:
        return bass_bar_01_g
    else:
        bass_bar_01_g.stop()
        return bass_bar_01_g        
    
bass_group = bass_bar_01(1)

bass_group.oct=4

bass_group.stop()

bass_bar_01()

c1.stop()

e1.stop()
