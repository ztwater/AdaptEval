>>> AA=range(10,21);SS=3
>>> [AA[i:i+SS] for i in range(len(AA))[::SS]]
[[10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20]]
# or [range(10, 13), range(13, 16), range(16, 19), range(19, 21)] in py3
