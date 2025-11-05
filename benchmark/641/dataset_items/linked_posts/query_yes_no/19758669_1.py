#!/usr/bin/python3

def makeChoi(yeh, neh):
    accept = {}
    # for w in words:
    accept['yes'] = [ '', yeh, yeh.lower(), yeh.upper(), yeh.lower()[0], yeh.upper()[0] ]
    accept['no'] = [ neh, neh.lower(), neh.upper(), neh.lower()[0], neh.upper()[0] ]
    return accept

accepted = makeChoi('Yes', 'No')

def doYeh():
    print('Yeh! Let\'s do it.')

def doNeh():
    print('Neh! Let\'s not do it.')

choi = None
while not choi:
    choi = input( 'Please choose: Y/n? ' )
    if choi in accepted['yes']:
        choi = True
        doYeh()
    elif choi in accepted['no']:
        choi = True
        doNeh()
    else:
        print('Your choice was "{}". Please use an accepted input value ..'.format(choi))
        print( accepted )
        choi = None
