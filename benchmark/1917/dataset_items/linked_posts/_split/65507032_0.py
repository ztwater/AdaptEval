def chunk(iterable, count): # returns a *generator* that divides `iterable` into `count` of contiguous chunks of similar size
    assert count >= 1
    return (iterable[int(_*len(iterable)/count+0.5):int((_+1)*len(iterable)/count+0.5)] for _ in range(count))

print("Chunk count:  ", len(list(         chunk(range(105),10))))
print("Chunks:       ",     list(         chunk(range(105),10)))
print("Chunks:       ",     list(map(list,chunk(range(105),10))))
print("Chunk lengths:",     list(map(len, chunk(range(105),10))))

print("Testing...")
for iterable_length in range(100):
    for chunk_count in range(1,100):
        chunks = list(chunk(range(iterable_length),chunk_count))
        assert chunk_count == len(chunks)
        assert iterable_length == sum(map(len,chunks))
        assert all(map(lambda _:abs(len(_)-iterable_length/chunk_count)<=1,chunks))
print("Okay")
