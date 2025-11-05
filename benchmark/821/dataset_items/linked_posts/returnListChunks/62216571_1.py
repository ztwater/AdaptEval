import chunker

chunk_size = 3

for it in (range(100, 107),
          range(100, 109)):

    print("\nITERABLE TO CHUNK: {}".format(it))
    print("CHUNK SIZE: {}".format(chunk_size))

    for option in chunker.PartialChunkOptions.__members__.values():
        print("\noption {} used".format(option))
        try:
            for chunk in chunker.chunker(it, chunk_size, on_partial=option):
                print(chunk)
        except chunker.PartialChunkException:
            print("PartialChunkException was raised")
    print("")
