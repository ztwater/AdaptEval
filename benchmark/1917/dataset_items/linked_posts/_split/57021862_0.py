def chunkify(tab, num):
    return [tab[i*num: i*num+num] for i in range(len(tab)//num+(1 if len(tab)%num else 0))]
