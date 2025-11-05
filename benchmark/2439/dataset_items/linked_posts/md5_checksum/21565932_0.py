$ ./sum_methods.py
crc32_mmap(filename) 0.0241742134094
crc32_read(filename) 0.0219960212708
subprocess.check_output(['cksum', filename]) 0.0553209781647
md5sum_mmap(filename) 0.0286180973053
md5sum_read(filename) 0.0311000347137
subprocess.check_output(['md5sum', filename]) 0.0332629680634
$ time md5sum /tmp/test.data.300k
d3fe3d5d4c2460b5daacc30c6efbc77f  /tmp/test.data.300k

real    0m0.043s
user    0m0.032s
sys     0m0.010s
$ stat -c '%s' /tmp/test.data.300k
11890400
