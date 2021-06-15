# include test file

def dr_xx():
    bassdrum >> play("X", dur=0.25, sample=(1), pan=0.4, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    snare >> play("i", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    rim >>  play("t", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    tom_hi >> play("M", dur=0.25, sample=(4), pan=0.4, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    tom_mid >> play("M", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    tom_lo >> play("m", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    crash_01 >> play("C", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    hh_close >> play("-", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    hh_open >> play("=", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    crash_02 >> play("#", dur=0.25, sample=(3), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    return

