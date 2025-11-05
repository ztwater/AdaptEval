for input_batch in batch_iterator(sys.stdin, 10000):
    for line in input_batch:
        process(line)
    finalise()
