def fox_once(n=0,stop=11):
    print(n)
    if (n <= stop):
        # f1 >> loop('foxdot',n,dur=1) 
        f1 >> loop('foxdot', dur=[Clock.next_bar(), seconds(5.36)]).after(seconds(5.36), "stop")    
    else:
        f1.stop()
        return
    Clock.future(1,fox_once, args=(n + 1,stop))


seconds = Clock.seconds_to_beats
fox_once(0,seconds(5.36))
