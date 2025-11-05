import humanize

disk_sizes_list = [1, 100, 999, 1000,1024, 2000,2048, 3000, 9999, 10000, 2048000000, 9990000000, 9000000000000000000000]
for size in disk_sizes_list:
    natural_size = humanize.naturalsize(size)
    binary_size = humanize.naturalsize(size, binary=True)
    print(f" {natural_size} \t| {binary_size}\t|{size}")
