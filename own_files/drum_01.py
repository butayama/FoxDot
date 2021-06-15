
def dr_00():
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

def dr_08():
    bassdrum >> play("X", dur=0.25, sample=(1), pan=0.4, room=0.7, verb=0.7, sus=3, amp=[1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    snare >> play("i", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0])
    rim >>  play("t", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    tom_hi >> play("M", dur=0.25, sample=(4), pan=0.4, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,1 ,0.8 ,0.6 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    tom_mid >> play("M", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0.6 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    tom_lo >> play("m", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0.6 ,0.8 ,1 ,0 ,0 ,0 ,0 ,0])
    crash_01 >> play("C", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    hh_close >> play("-", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    hh_open >> play("=", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    crash_02 >> play("#", dur=0.25, sample=(3), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0])
    return

def dr_16():
    bassdrum >> play("X", dur=0.25, sample=(1), pan=0.4, room=0.7, verb=0.7, sus=3, amp=[1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,1 ,0 ,0 ,0])
    snare >> play("i", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0])
    rim >>  play("t", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    tom_hi >> play("M", dur=0.25, sample=(4), pan=0.4, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,1 ,0 ,0.8 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    tom_mid >> play("M", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0.8 ,0.6 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    tom_lo >> play("m", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0.6 ,0 ,0 ,0 ,0 ,0])
    crash_01 >> play("C", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    hh_close >> play("-", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    hh_open >> play("=", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    crash_02 >> play("#", dur=0.25, sample=(3), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0])
    return


def dr_random():
    bassdrum >> play("X", dur=0.25, sample=(1), pan=0.4, room=0.7, verb=0.7, sus=3,  amp=PwRand([0 ,1 ,0.8 ,0.6] ,[14 ,1 ,1 ,1])[:16])
    snare >> play("i", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,    amp=PwRand([0 ,1 ,0.8 ,0.6] ,[9 ,3 ,1 ,3])[:16])
    rim >>  play("t", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,     amp=PwRand([0 ,1 ,0.8 ,0.6] ,[8 ,1 ,1 ,1])[:16])
    tom_hi >> play("M", dur=0.25, sample=(4), pan=0.4, room=0.7, verb=0.7, sus=3,    amp=PwRand([0 ,1 ,0.8 ,0.6] ,[14 ,1 ,1 ,1])[:16])
    tom_mid >> play("M", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,  amp=PwRand([0 ,1 ,0.8 ,0.6] ,[14 ,1 ,1 ,1])[:16])
    tom_lo >> play("m", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3,   amp=PwRand([0 ,1 ,0.8 ,0.6] ,[9 ,3 ,1 ,3])[:16])
    crash_01 >> play("C", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    hh_close >> play("-", dur=0.25, sample=(0), pan=0.45, room=0.7, verb=0.7, sus=3, amp=PwRand([0 ,1 ,0.8 ,0.6] ,[8 ,1 ,1 ,1])[:16])
    hh_open >> play("=", dur=0.25, sample=(1), pan=0.45, room=0.7, verb=0.7, sus=3,  amp=PwRand([0 ,1 ,0.8 ,0.6] ,[12 ,1 ,1 ,0])[:16])
    crash_02 >> play("#", dur=0.25, sample=(3), pan=0.45, room=0.7, verb=0.7, sus=3, amp=[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0])
    return

def dr_random_01_gen():
    amp_list = []
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[14 ,1 ,1 ,1])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[9 ,3 ,1 ,3])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[8 ,1 ,1 ,1])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[14 ,1 ,1 ,1])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[14 ,1 ,1 ,1])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[9 ,3 ,1 ,3])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[15 ,1 ,0 ,0])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[8 ,1 ,1 ,1])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[12 ,1 ,1 ,0])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[15 ,1 ,0 ,0])[:16])
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
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[14 ,1 ,1 ,1])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[9 ,3 ,1 ,3])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[8 ,1 ,1 ,1])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[14 ,1 ,2 ,3])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[14 ,1 ,3 ,3])[:16])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[9 ,3 ,4 ,2])[:16])
    amp_list.append([0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
    amp_list.append(PwRand([0 ,1 ,0.8 ,0.6] ,[8 ,8 ,8 ,8])[:16])
    amp_list.append([0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0])
    amp_list.append([0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0])
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
