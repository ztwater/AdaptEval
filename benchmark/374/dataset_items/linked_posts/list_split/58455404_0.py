def chunkIt(seq, num):
    steps = int(len(seq) / float(num))
    out = []
    last = 0.0

    while last < len(seq):
        if len(seq) - (last + steps) < steps:
            until = len(seq)
            steps = len(seq) - last
        else:
            until = int(last + steps)
        out.append(seq[int(last): until])
        last += steps
return out
