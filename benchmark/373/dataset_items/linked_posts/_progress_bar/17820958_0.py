import sys
def prg(prog, fillchar, emptchar):
    fillt = 0
    emptt = 20
    if prog < 100 and prog > 0:
        prog2 = prog/5
        fillt = fillt + prog2
        emptt = emptt - prog2
        sys.stdout.write("\r[" + str(fillchar)*fillt + str(emptchar)*emptt + "]" + str(prog) + "%")
        sys.stdout.flush()
    elif prog >= 100:
        prog = 100
        prog2 = prog/5
        fillt = fillt + prog2
        emptt = emptt - prog2
        sys.stdout.write("\r[" + str(fillchar)*fillt + str(emptchar)*emptt + "]" + str(prog) + "%" + "\nDone!")
        sys.stdout.flush()
    elif prog < 0:
        prog = 0
        prog2 = prog/5
        fillt = fillt + prog2
        emptt = emptt - prog2
        sys.stdout.write("\r[" + str(fillchar)*fillt + str(emptchar)*emptt + "]" + str(prog) + "%" + "\nHalted!")
        sys.stdout.flush()
