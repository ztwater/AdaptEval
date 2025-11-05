>>> timeit.timeit('len(set(s1))<=1', 's1=[1]*5000', number=10000)
1.4383411407470703
>>> timeit.timeit('len(set(s1))<=1', 's1=[1]*4999+[2]', number=10000)
1.4765670299530029
>>> timeit.timeit('s1.count(s1[0])==len(s1)', 's1=[1]*5000', number=10000)
0.26274609565734863
>>> timeit.timeit('s1.count(s1[0])==len(s1)', 's1=[1]*4999+[2]', number=10000)
0.25654196739196777
