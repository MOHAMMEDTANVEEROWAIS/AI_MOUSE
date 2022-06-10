

global lw
rw = input('enter right winger : ')
st = input('enter striker : ')
lwm = input('enter left winger midfielder : ')
alm = input('enter attacking left winger : ')
am = input('enter attacking midfielder : ')
arm = input('enter attacking right winger : ')
rwm = input('enter fight winger midfielder : ')
cdrm = input('enter central defensive right midfielder : ')
cdm = input('enter central defensive midfielder : ')
cdlm = input('enter central defensive right midfielder : ')
rwb = input('enter right winger back : ')
rb = input('enter right back : ')
cb = input('enter center back : ')
lb = input('enter left back : ')
lwb = input('enter left winger back: ')

def func_lw():
   lw = input('enter left winger : ')
   print(lw)
# func_lw()

# lw = input('enter left winger : ')
    

# rw = input('enter right winger : ')
def func_rw():
    print(rw)



def func_st():
    st = input('enter striker : ')
    print(st)


def func_lwm():
    # lwm = input('enter left winger midfielder : ')
    print(lwm)


def func_alm():
    # alm = input('enter attacking left winger : ')
    print(alm)


def func_am():
    # am = input('enter attacking midfielder : ')
    print(am)


def func_arm():
    # arm = input('enter attacking right winger : ')
    print(arm)


def func_rwm():
    # rwm = input('enter fight winger midfielder : ')
    print(rwm)


def func_cdrm():
    # cdrm = input('enter central defensive right midfielder : ')
    print(cdrm)


def func_cdm():
    # cdm = input('enter central defensive midfielder : ')
    print(cdm)


def func_cdlm():
    # cdlm = input('enter central defensive right midfielder : ')
    print(cdlm)


def func_rwb():
    # rwb = input('enter right winger back : ')
    print(rwb)


def func_rb():
    # rb = input('enter right back : ')
    print(rb)


def func_cb():
    # cb = input('enter center back : ')
    print(cb)


def func_lb():
    # lb = input('enter left back : ')
    print(lb)


def func_lwb():
    # lwb = input('enter left winger back: ')
    print(lwb)



# create a list to store the positions and then use if statements to perform the respective functions
emplist = []
for element in range(10):
    take = input(": ")
    emplist.append(take)

for display in emplist:
    if element == 'lw':
        func_lw()
    elif element == 'rw':
        func_rw()
    elif element == 'st':
        func_st()
    elif element == 'am':
        func_am()
    elif element == 'alm':
        func_alm()
    elif element == 'lwm':
        func_lwm()
    elif element == 'arm':
        func_arm()
    elif element == 'rwm':
        func_rwm()
    elif element == 'cdm':
        func_cdm()
    elif element == 'cdrm':
        func_cdrm()
    elif element == 'cdlm':
        func_cdlm()
    elif element == 'rwb':
        func_rwb()
    elif element == 'rb':
        func_rb()
    elif element == 'cb':
        func_cb()
    elif element == 'lb':
        func_lb()
    elif element == 'lwb':
        func_lwb()
    break


formation = [[lw, 0, st, 0, rw], [lwm, alm, am, arm, rwm], [0, cdlm, cdm, cdrm, 0], [lwb, lb, cb, rb, rwb]]

for image in formation:
    for pixel in image:
        if (pixel != 0):
            print('player', end="")
        else:
            print(' ', end="")
            print('')
    # matrix elements are strings'''
