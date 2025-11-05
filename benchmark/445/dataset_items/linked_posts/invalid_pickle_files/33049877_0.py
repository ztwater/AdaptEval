# save data to a file
with open('myfile.pickle','wb') as fout:
    pickle.dump([1,2,3],fout)

# read data from a file
with open('myfile.pickle') as fin:
    print pickle.load(fin)

# output
>> [1, 2, 3]
