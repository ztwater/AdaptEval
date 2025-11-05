import numpy as np
        
def opa(a, b):
    aT = a.mean(0)
    bT = b.mean(0)
    A = a - aT 
    B = b - bT
    aS = np.sum(A * A)**.5
    bS = np.sum(B * B)**.5
    A /= aS
    B /= bS
    U, _, V = np.linalg.svd(np.dot(B.T, A))
    aR = np.dot(U, V)
    if np.linalg.det(aR) < 0:
        V[1] *= -1
        aR = np.dot(U, V)
    aS = aS / bS
    aT-= (bT.dot(aR) * aS)
    aD = (np.sum((A - B.dot(aR))**2) / len(a))**.5
    return aR, aS, aT, aD 
        
def gpa(v, n=-1):
    if n < 0:
        p = avg(v)
    else:
        p = v[n]
    l = len(v)
    r, s, t, d = np.ndarray((4, l), object)
    for i in range(l):
        r[i], s[i], t[i], d[i] = opa(p, v[i]) 
    return r, s, t, d

def avg(v):
    v_= np.copy(v)
    l = len(v_) 
    R, S, T = [list(np.zeros(l)) for _ in range(3)]
    for i, j in np.ndindex(l, l):
        r, s, t, _ = opa(v_[i], v_[j]) 
        R[j] += np.arccos(min(1, max(-1, np.trace(r[:1])))) * np.sign(r[1][0]) 
        S[j] += s 
        T[j] += t 
    for i in range(l):
        a = R[i] / l
        r = [np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]
        v_[i] = v_[i].dot(r) * (S[i] / l) + (T[i] / l) 
    return v_.mean(0)
